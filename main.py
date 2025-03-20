from enum import Enum


class DispatchType(str, Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def dimensions_validator(value: float) -> None:
    """Validates that the dimensions are greater than 0 and not None.

    Args:
        value: The value to validate.
    """
    if value is None or value <= 0:
        raise ValueError("Dimensions must be greater than 0.")

def sort(width: float, height: float, length: float, mass: float) -> DispatchType:
    """
    Sorts packages based on their volume and mass.

    Args:
        width: The width of the package in centimeters.
        height: The height of the package in centimeters.
        length: The length of the package in centimeters.
        mass: The mass of the package in kilograms.

    Returns:
        A string representing the stack where the package should be dispatched.
    """
    dimensions_validator(width)
    dimensions_validator(height)
    dimensions_validator(length)
    dimensions_validator(mass)

    volume = width * height * length
    bulky = (volume >= 1000000) or (width >= 150) or (height >= 150) or (length >= 150)
    heavy = mass >= 20
    return (
        DispatchType.REJECTED if bulky and heavy else DispatchType.SPECIAL if bulky or heavy else DispatchType.STANDARD
    )
