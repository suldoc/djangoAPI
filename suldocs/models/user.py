from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from rest_framework import serializers


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    is_valid = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    def set_data(self, user_info):
        for key in user_info:
            setattr(self, key, user_info[key])


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "email",
            "is_valid",
            "is_deleted",
            "created_at",
            "updated_at",
        )
