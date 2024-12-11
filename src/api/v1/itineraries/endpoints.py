from .services import ItineraryService
from .serializers import ItinerarySerializer
from core.models import Itinerary

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions

from rest_framework_simplejwt.authentication import JWTAuthentication


class ItineraryViewSet(viewsets.ViewSet):
    """
    A ViewSet for managing itineraries using self.service.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ItinerarySerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ItineraryService

    def list(self, request):
        """
        Retrieve a list of all itineraries.
        """
        itineraries = self.service.list_itineraries()
        serializer = self.serializer_class(itineraries, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a single itinerary by its ID.
        """
        itinerary = self.service.get_itinerary_by_id(pk)
        serializer = self.serializer_class(itinerary)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new itinerary.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        itinerary = self.service.create_itinerary(request.user,
                                                  serializer.validated_data)
        return Response(
                self.serializer_class(itinerary).data,
                status=status.HTTP_201_CREATED
            )

    def update(self, request, pk=None):
        """
        Update an existing itinerary.
        """
        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        itinerary = self.service.update_itinerary(pk,
                                                  serializer.validated_data)
        return Response(self.serializer_class(itinerary).data)

    def destroy(self, request, pk=None):
        """
        Delete an itinerary by its ID.
        """
        success = self.service.delete_itinerary(pk)
        if not success:
            raise Exception("itinerary not deleted")
        return Response(
            {"detail": "Itinerary deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )

    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request):
        """
        Search for itineraries based on a query parameter
        (e.g., title or description).
        """
        query = request.query_params.get("q", "")
        itineraries = Itinerary.objects.filter(title__icontains=query)
        serializer = self.serializer_class(itineraries, many=True)
        return Response(serializer.data)
