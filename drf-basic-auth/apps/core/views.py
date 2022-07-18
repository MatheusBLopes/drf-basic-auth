from xml.dom import ValidationErr
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UpdateUserSerializer, ChangePasswordSerializer, RegisterSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from apps.core.models import UUIDUser as User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request):
        user = User.objects.filter(pk=request.auth["user_id"]).first()
        serializer = ChangePasswordSerializer(user, data=request.data)
        serializer.validate(request.data)

        if serializer.is_valid():
            serializer.update(user, request.data)
            return Response(status=status.HTTP_200_OK)


        return Response(data=serializer.errors["old_password"], status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )


    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)