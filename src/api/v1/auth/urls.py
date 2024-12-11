from .endpoints.login import LoginAPIView
from .endpoints.signup import SignupAPIView
from .endpoints.users import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")

# Define urlpatterns
urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("signup/", SignupAPIView.as_view(), name="signup"),
] + router.urls  # Append the router-generated URLs
