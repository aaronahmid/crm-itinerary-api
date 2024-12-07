from django.core.exceptions import ValidationError


# Validator for Location JSON field
def validate_location(value):
    """
    Validates the structure of the location JSON field.
    Expected keys: country, state, city (all strings).
    """
    required_keys = ["country", "state", "city"]
    if not isinstance(value, dict):
        raise ValidationError("Location must be a JSON object.")
    for key in required_keys:
        if key not in value:
            raise ValidationError(f"Missing '{key}' in location.")
        if not isinstance(value[key], str):
            raise ValidationError(f"'{key}' must be a string in location.")


# Validator for Pricing JSON field
def validate_pricing(value):
    """
    Validates the structure of the pricing JSON field.
    Expected keys: amount (float), currency (string), tax (float).
    """
    required_keys = ["amount", "currency", "tax"]
    if not isinstance(value, dict):
        raise ValidationError("Pricing must be a JSON object.")
    for key in required_keys:
        if key not in value:
            raise ValidationError(f"Missing '{key}' in pricing.")
    if not isinstance(value["amount"], (int, float)):
        raise ValidationError("'amount' must be a float or int in pricing.")
    if not isinstance(value["currency"], str):
        raise ValidationError("'currency' must be a string in pricing.")
    if not isinstance(value["tax"], (int, float)):
        raise ValidationError("'tax' must be a float or int in pricing.")


# Validator for Accommodation JSON field
def validate_accommodation(value):
    """
    Validates the structure of the accommodation JSON field.
    Expected keys: type (string), stars (integer), bedrooms (integer).
    """
    required_keys = ["type", "stars", "bedrooms"]
    if not isinstance(value, dict):
        raise ValidationError("Accommodation must be a JSON object.")
    for key in required_keys:
        if key not in value:
            raise ValidationError(f"Missing '{key}' in accommodation.")
    if not isinstance(value["type"], str):
        raise ValidationError("'type' must be a string in accommodation.")
    if not isinstance(value["stars"], int):
        raise ValidationError("'stars' must be an integer in accommodation.")
    if not isinstance(value["bedrooms"], int):
        raise ValidationError("'bedrooms' must be an integer in accommodation.")
