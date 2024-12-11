from rest_framework.exceptions import APIException, ValidationError  # type: ignore


class CannotDestroyResource(APIException):
    status_code = 403
    default_detail = "resource cannot be destroyed"
    default_code = "CANNOT.DESTROY"

    def __init__(self, detail=None, code=None):
        detail = detail if detail is not None else self.default_detail
        code = f"{self.default_code}.{code}" if code is not None else self.default_code
        super().__init__(detail=detail, code=code)


class CustomAPIError(APIException):
    status_code = 500
    default_detail = "An unexpected error occurred."
    default_code = "error"


class ObjectAlreadyExistError(APIException):
    status_code = 409
    default_detail = "Object already exists"
    default_code = "OBJECT.ALREADY.EXISTS"

    def __init__(self, detail=None, code=None):
        detail = detail if detail is not None else self.default_detail
        code = f"{self.default_code}.{code}" if code is not None else self.default_code
        super().__init__(detail=detail, code=code)


class APIClientException(APIException):
    default_detail = "an exception occurred while trying the request"
    default_code = "CLIENT.ERROR"

    def __init__(self, detail=None, code=None, status_code=None):
        self.status_code = status_code if status_code is not None else self.status_code
        detail = detail if detail is not None else self.default_detail
        code = f"{self.default_code}.{code}" if code is not None else self.default_code
        super().__init__(detail=detail, code=code)


class UserInactive(APIException):
    status_code = 403
    default_detail = "user is inactive"
    default_code = "USER.INACTIVE"

    def __init__(self, detail=None, code=None):
        detail = detail if detail is not None else self.default_detail
        code = code if code is not None else self.default_code
        super().__init__(detail=detail, code=code)


class InvalidCredentials(APIException):
    status_code = 400
    default_detail = "invalid email or password"
    default_code = "CREDENTIALS.INVALID"

    def __init__(self, detail=None, code=None):
        detail = detail if detail is not None else self.default_detail
        code = code if code is not None else self.default_code
        super().__init__(detail=detail, code=code)


class ResourceNotFound(APIException):
    status_code = 404
    default_detail = "resource not found"
    default_code = "RESOURCE.NOT.FOUND"

    def __init__(self, detail=None, code=None):
        detail = detail if detail is not None else self.default_detail
        code = code if code is not None else self.default_code
        super().__init__(detail=detail, code=code)
