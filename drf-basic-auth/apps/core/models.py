from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class UUIDUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


