from .serializers import UserSerializer
from .service import CustomerSerializer, CustomerService

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions


class UserViewSet(viewsets.ViewSet):
    """
    ViewSet for managing customers.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomerSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CustomerService

    def create(self, request):
        """
        Create a new customer using the service layer.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.service.create_customer(**serializer.validated_data)
        return Response(
            self.serializer_class(user).data, status=status.HTTP_201_CREATED
        )

    def retrieve(self, request, pk=None):
        """
        Retrieve a customer by ID.
        """
        user = self.service.get_customer_by_id(pk)
        return Response(
            self.serializer_class(user).data, status=status.HTTP_200_OK
            )

    def update(self, request, pk=None):
        """
        Update a customer's details using the service layer.
        """
        user = self.service.get_customer_by_id(pk)

        serializer = self.serializer_class(
            user, data=request.data, partial=True
            )
        serializer.is_valid(raise_exception=True)
        updated_user = self.service.update_customer(pk,
                                                    serializer.validated_data)
        return Response(
            self.serializer_class(updated_user).data, status=status.HTTP_200_OK
        )

    def list(self, request):
        """
        List all customers.
        """
        users = self.service.list_customers
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
