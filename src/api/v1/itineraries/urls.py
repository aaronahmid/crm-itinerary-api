from .endpoints import ItineraryViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ItineraryViewSet, basename='itinerary')

urlpatterns = [
    # Other URLs...
] + router.urls
