#!/usr/bin/env python3
"""login serializer"""
from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the custom user model.
    Handles validation, serialization, and deserialization.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "created_at",
            "updated_at",
            "last_login",
            "password",
            "user_type"
        ]
        read_only_fields = [
            "id",
            "is_active",
            "is_staff",
            "created_at",
            "updated_at",
            "last_login",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
