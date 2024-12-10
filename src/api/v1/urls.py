from django.urls import path, include
from .auth.endpoints.login import LoginView


endpoints = [
    path("auth/login/", LoginView.as_view(), name="login"),
]

urlpatterns = [
    path("v1/", include(endpoints, "v1"))
]
