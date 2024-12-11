from django.db import IntegrityError, transaction
from api.exceptions.errors import ObjectAlreadyExistError, ResourceNotFound
from core.models import Itinerary


class ItineraryService:
    """
    Service class for managing Itinerary operations.
    """

    @staticmethod
    @transaction.atomic
    def create_itinerary(user, data):
        """
        Create a new itinerary.

        Args:
            data (dict): Data to create an itinerary.

        Returns:
            Itinerary: The created itinerary instance.
        """
        try:
            itinerary = Itinerary.objects.create(created_by=user, **data)
        except IntegrityError:
            raise ObjectAlreadyExistError("similar object already created")
        return itinerary

    @staticmethod
    def get_itinerary_by_id(itinerary_id):
        """
        Retrieve an itinerary by its ID.

        Args:
            itinerary_id (UUID): The ID of the itinerary.

        Returns:
            Itinerary: The itinerary instance, or None if not found.
        """
        try:
            return Itinerary.objects.get(id=itinerary_id)
        except Itinerary.DoesNotExist:
            raise ResourceNotFound(f"itinerary does not exists: {itinerary_id}")

    @staticmethod
    def update_itinerary(itinerary_id, data):
        """
        Update an existing itinerary.

        Args:
            itinerary_id (UUID): The ID of the itinerary to update.
            data (dict): Data to update the itinerary.

        Returns:
            Itinerary: The updated itinerary instance, or None if not found.
        """
        itinerary = ItineraryService.get_itinerary_by_id(itinerary_id)
        if not itinerary:
            return None

        for key, value in data.items():
            setattr(itinerary, key, value)
        itinerary.save()
        return itinerary

    @staticmethod
    def delete_itinerary(itinerary_id):
        """
        Delete an itinerary by its ID.

        Args:
            itinerary_id (UUID): The ID of the itinerary to delete.

        Returns:
            bool: True if the itinerary was deleted, False otherwise.
        """
        itinerary = ItineraryService.get_itinerary_by_id(itinerary_id)
        if not itinerary:
            return False
        itinerary.delete()
        return True

    @staticmethod
    def list_itineraries():
        """
        Retrieve a list of all itineraries.

        Returns:
            QuerySet: A QuerySet of all itineraries.
        """
        return Itinerary.objects.all()
