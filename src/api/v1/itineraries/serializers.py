from rest_framework import serializers
from core.models import Itinerary


class ItinerarySerializer(serializers.ModelSerializer):
    """
    Serializer for the Itinerary model.
    Includes fields for nested or complex data like `pricing` and `details`.
    """

    class Meta:
        model = Itinerary
        fields = "__all__"

    # def validate_pricing(self, value):
    #     """
    #     Validate the `pricing` JSON field to ensure the required keys are present.
    #     """
    #     required_keys = {"currency", "amount"}
    #     if not isinstance(value, dict):
    #         raise serializers.ValidationError("Pricing must be a dictionary.")
    #     if not required_keys.issubset(value.keys()):
    #         raise serializers.ValidationError(
    #             f"Pricing must contain the keys: {required_keys}."
    #         )
    #     if not isinstance(value["amount"], (int, float)) or value["amount"] < 0:
    #         raise serializers.ValidationError("Amount must be a positive number.")
    #     return value

    # def validate_details(self, value):
    #     """
    #     Validate the `details` JSON field to ensure it contains valid information.
    #     """
    #     if not isinstance(value, dict):
    #         raise serializers.ValidationError("Details must be a dictionary.")
    #     # Add custom validation for expected keys in `details`, if any.
    #     return value

    # def validate(self, attrs):
    #     """
    #     Perform object-level validation.
    #     """
    #     start_date = attrs.get("start_date")
    #     end_date = attrs.get("end_date")

    #     if start_date and end_date and start_date > end_date:
    #         raise serializers.ValidationError("Start date must be before the end date.")

    #     return attrs
