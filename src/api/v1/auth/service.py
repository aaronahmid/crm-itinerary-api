from django.db import transaction
from django.db import IntegrityError
from django.utils.timezone import now
from core.models import User, Customer
from ...exceptions.errors import (
    ObjectAlreadyExistError,
    ResourceNotFound,
    CustomAPIError
)


class UserService:
    """
    Service class to handle business logic for User operations.
    """

    @staticmethod
    @transaction.atomic
    def create_user(email: str = None, first_name: str = None, last_name: str = None, password: str = None, user_type="CUSTOMER") -> User:
        """
        Create a new user.

        :param email: Email address of the user
        :param first_name: First name of the user
        :param last_name: Last name of the user
        :param password: User's password
        :return: The created User object

        Raises:
            IntegrityError
            CustomAPIError
        """
        try:
            print(password)
            user = User.objects.create_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )

            if user_type == "CUSTOMER":
                Customer.objects.create(
                    user=user, first_name=first_name, last_name=last_name
                )
            else:
                user.user_type = "STAFF"
                user.save()

            return user
        except IntegrityError as error:
            raise ObjectAlreadyExistError(str(error))
        except Exception as error:
            raise CustomAPIError(str(error))

    @staticmethod
    @transaction.atomic
    def update_user(user_id: str, **kwargs) -> User:
        """
        Update user details.

        :param user_id: ID of the user to update
        :param kwargs: Fields to update (e.g., first_name, last_name)
        :return: The updated User object

        Raises:
            ResourceNotFound
            CustomAPIError
        """
        try:
            user = User.objects.get(id=user_id)
            for field, value in kwargs.items():
                setattr(user, field, value)
            user.updated_at = now()
            user.save()
            return user
        except User.DoesNotExist:
            raise ResourceNotFound("user not found")
        except Exception as error:
            raise CustomAPIError(str(error))

    @staticmethod
    @transaction.atomic
    def deactivate_user(user_id: str) -> User:
        """
        Deactivate a user.

        :param user_id: ID of the user to deactivate
        :return: The deactivated User object
        """
        try:
            user = User.objects.get(id=user_id)
            user.is_active = False
            user.updated_at = now()
            user.save()
            return user
        except User.DoesNotExist:
            raise ResourceNotFound("user not found")
        except Exception as error:
            raise CustomAPIError(str(error))

    @staticmethod
    @transaction.atomic
    def activate_user(user_id: str) -> User:
        """
        Activate a user.

        :param user_id: ID of the user to activate
        :return: The activated User object

        Raises:
            ResourceNotFound
            CustomAPIError
        """
        try:
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.updated_at = now()
            user.save()
            return user
        except User.DoesNotExist:
            raise ResourceNotFound("user not found")
        except Exception as error:
            raise CustomAPIError(str(error))

    @staticmethod
    def get_user_by_email(email: str) -> User:
        """
        Retrieve a user by email.

        :param email: Email address of the user
        :return: The User object
        """
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            raise ResourceNotFound("user not found")
        except Exception as error:
            raise CustomAPIError(str(error))

    @staticmethod
    def get_user_by_id(user_id: str) -> User:
        """
        Retrieve a user by ID.

        :param user_id: ID of the user
        :return: The User object
        """
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise ResourceNotFound("user not found")
        except Exception as error:
            raise CustomAPIError(str(error))

    @staticmethod
    def list_users():
        """_summary_
        """
        return User.objects.all()
