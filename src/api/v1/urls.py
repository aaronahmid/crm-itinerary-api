from django.urls import path, include

urlpatterns = [
    path("auth/", include("api.v1.auth.urls")),
    path("itineraries/", include("api.v1.itineraries.urls")),
    path("customers/", include("api.v1.customers.urls")),
]
