from rest_flex_fields import FlexFieldsModelSerializer
from .models import Image, Product, Category, Company, ProductSize, ProductSite, Comment
from apps.core.models import UUIDUser as User
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']
        

class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
          'products': ('apps.reviews.ProductSerializer', {'many': True})
        }


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk', 'name']


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category': ('apps.reviews.CategorySerializer', {'many': True}),
            'sites': ('apps.reviews.ProductSiteSerializer', {'many': True}),
            'comments': ('apps.reviews.CommentSerializer', {'many': True}),
            'image': ('apps.reviews.ImageSerializer', {'many': True}),
        }


class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product': 'apps.reviews.CategorySerializer',
            'productsize': 'apps.reviews.ProductSizeSerializer',
            'company': 'apps.reviews.CompanySerializer',
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'apps.reviews.CategorySerializer',
            'user': 'apps.reviews.UserSerializer'
        }
