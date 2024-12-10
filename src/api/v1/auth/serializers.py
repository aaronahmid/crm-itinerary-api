#!/usr/bin/env python3
"""login serializer"""
from rest_framework import serializers
from src.core.models import User


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
        ]
        read_only_fields = [
            "id",
            "is_active",
            "is_staff",
            "created_at",
            "updated_at",
            "last_login",
        ]
