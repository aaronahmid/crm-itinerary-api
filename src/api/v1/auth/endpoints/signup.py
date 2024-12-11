from ..service import UserService
from ..serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class SignupAPIView(APIView):
    """
    API view for user signup.
    Delegates user creation to the UserService.
    """

    permission_classes = [permissions.AllowAny]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Use the service to create the user
        user = self.user_service.create_user(
            **serializer.validated_data
        )
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
