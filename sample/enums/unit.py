"""
"""

from enum import Enum

FACTOR = 2.2046

class Unit(Enum):
    POUNDS = 1
    KILOGRAMS = 2

def convert(weight: int, to_unit: Unit) -> float:
    """Convert a weight to the unit desired.

    This function convert the input weight into the "to_unit" unit
    considering 1kg = 2.2046lbs.

    Parameters
    ----------
    weight : int
        The weight to convert.
    to_unit : Unit
        The unit to which we want to convert.

    Raises
    ------
    TypeError
        In case the unit is unknown this function raises a TypeError.

    Returns
    -------
    float
        The converted weight.
    """
    converted_weight = 0.0

    if to_unit is Unit.POUNDS:
        converted_weight = weight * FACTOR
    elif to_unit is Unit.KILOGRAMS:
        converted_weight = weight / FACTOR
    else:
        raise TypeError("Unit unknown for conversion")

    return converted_weight
