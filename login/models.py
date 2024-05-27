from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(blank=True, null=True, upload_to='static/')
    email = models.EmailField(unique=True)

    # Add unique related_name attributes
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')
