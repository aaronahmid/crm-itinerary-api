from api.exceptions.errors import UserInactive, InvalidCredentials
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Extract email and password explicitly from request.data
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            raise InvalidCredentials("Email and password are required.")

        # Pass email and password explicitly to `authenticate`
        user = authenticate(email=email, password=password)

        if user is not None:
            if not user.is_active:
                raise UserInactive("User account is inactive.")

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            update_last_login(None, user)  # Update the `last_login` field

            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                },
                status=status.HTTP_200_OK,
            )
        else:
            raise InvalidCredentials("Invalid email or password.")
