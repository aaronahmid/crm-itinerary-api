from ..serializers import UserSerializer
from ..service import UserService

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions

from rest_framework_simplejwt.authentication import JWTAuthentication


class UserViewSet(viewsets.ViewSet):
    """
    ViewSet for managing users.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    user_service = UserService

    def create(self, request):
        """
        Create a new user using the service layer.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.user_service.create_user(**serializer.validated_data)
        return Response(
            self.serializer_class(user).data, status=status.HTTP_201_CREATED
            )

    def retrieve(self, request, pk=None):
        """
        Retrieve a user by ID.
        """
        user = self.user_service.get_user_by_id(pk)
        return Response(
            self.serializer_class(user).data, status=status.HTTP_200_OK
            )

    def update(self, request, pk=None):
        """
        Update a user's details using the service layer.
        """
        user = self.user_service.get_user_by_id(pk)
        serializer = self.serializer_class(
            user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_user = self.user_service.update_user(user, **serializer.validated_data)
        return Response(
            self.serializer_class(updated_user).data, status=status.HTTP_200_OK
            )

    def list(self, request):
        """
        List all users.
        """
        users = self.user_service.list_users()
        print(users)
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def deactivate(self, request):
        """
        Deactivate a user account.
        """
        user_id = request.data.get("id")
        if not user_id:
            raise Exception("user id is required")
        UserService.deactivate_user(user_id)
