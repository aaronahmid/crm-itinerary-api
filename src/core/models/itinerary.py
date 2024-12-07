# Itinerary Model
import uuid

from django.db import models

from .customer import Customer
from .user import User

from .validators import (
    validate_location,
    validate_accommodation,
    validate_pricing
)


class Itinerary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="itineraries",
        blank=True, null=True
    )
    location = models.JSONField(serialize=True, null=True,
                                validators=[validate_location])  # Contains country, state, city
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pricing = models.JSONField(
        serialize=True, null=True, validators=[validate_pricing]
    )  # Contains amount, currency, tax
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="itineraries",
        blank=True,
        null=True,
    )
    interests = models.TextField(blank=True, null=True)  # Travel interests
    accommodation = models.JSONField(
        serialize=True, null=True, validators=[validate_accommodation]
    )  # Contains type, stars, bedrooms

    def __str__(self):
        return f"Itinerary for {self.customer.first_name}\
        {self.customer.last_name}"

    class Meta:
        verbose_name = "Itinerary"
        verbose_name_plural = "Itineraries"
