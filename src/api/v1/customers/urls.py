from .endpoints import CustomerViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", CustomerViewSet, basename="customers")

urlpatterns = [
    # Other URLs...
] + router.urls
