from django.db import IntegrityError, transaction

from ...exceptions.errors import (
    ObjectAlreadyExistError,
    ResourceNotFound
)
from core.models import Customer


class CustomerService:
    """
    Service class for managing Customer operations.
    """

    @staticmethod
    @transaction.atomic
    def create_customer(data):
        """
        Create a new customer.

        Args:
            data (dict): Data to create a customer.

        Returns:
            Customer: The created customer instance.
        """
        try:
            customer = Customer.objects.create(**data)
        except IntegrityError:
            raise ObjectAlreadyExistError("customer already exists")
        return customer

    @staticmethod
    def get_customer_by_id(customer_id):
        """
        Retrieve a customer by their ID.

        Args:
            customer_id (UUID): The ID of the customer.

        Returns:
            Customer: The customer instance, or None if not found.
        """
        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise ResourceNotFound("customer does not exists")

    @staticmethod
    @transaction.atomic
    def update_customer(customer_id, data):
        """
        Update an existing customer.

        :customer_id (UUID): The ID of the customer to update.
        :data (dict): Data to update the customer.

        Returns:
            Customer: The updated customer instance, or None if not found.
        """
        customer = CustomerService.get_customer_by_id(customer_id)

        for key, value in data.items():
            setattr(customer, key, value)
        customer.save()
        return customer

    @staticmethod
    def delete_customer(customer_id):
        """
        Delete a customer by their ID.

        Args:
            customer_id (UUID): The ID of the customer to delete.

        Returns:
            bool: True if the customer was deleted, False otherwise.
        """
        customer = CustomerService.get_customer_by_id(customer_id)
        customer.delete()
        return True

    @staticmethod
    def list_customers():
        """
        Retrieve a list of all customers.

        Returns:
            QuerySet: A QuerySet of all customers.
        """
        return Customer.objects.all()
