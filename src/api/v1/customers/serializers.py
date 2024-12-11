from ..auth.serializers import UserSerializer

from rest_framework import serializers
from core.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.
    Provides validation and ensures fields are correctly serialized.
    """
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = (
            'id',
            'user',
            'phone',
            'address',
            'birthday',
            'created_at'
            )
        read_only_fields = ["id", "created_at", "updated_at", "user"]
