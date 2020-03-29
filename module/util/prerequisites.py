"""
Prerequisite functions to help and assert inputs and outputs condition and type
"""

from typing import Iterable, Type, TypeVar, Union, no_type_check

# create a type var to then tests if input type is the same as output type for example
type_x = TypeVar("type_x")
type_y = TypeVar("type_y", bound=Iterable)


# conditions
def require(condition: bool, message: str = "Requirement failed!"):
    """
    Test one condition

    Args:
        condition (bool): boolean condition
        message (str): custom message to add to the assert
    """
    assert condition, message


def require_one_in_all(
    collection_conditions: Iterable[bool],
    message: str = "Not even one requirement met!",
):
    """
    Require one condition in a collection of conditions

    Args:
        collection_conditions (Iterable): conditions to be tested
        message (str): custom message to add to the assert
    """
    assert any(collection_conditions), message


def require_all_in_all(
    collection_conditions: Iterable[bool],
    message: str = "Not all requirements met!",
):
    """
    Require all conditions in a collection of conditions

    Args:
        collection_conditions (Iterable): conditions to be tested
        message (str): custom message to add to the assert
    """
    assert all(collection_conditions), message


# types
@no_type_check
def require_type(variable: type_x, expected_type: Type) -> type_x:
    """
    Requite type of variable

    Args:
        variable: variable to be type tested
        expected_type: type to be expected

    Returns:
        If assert is True, it returns the variable
    """
    assert isinstance(
        variable, expected_type
    ), f"Expected type {expected_type}, got {type(variable)}!"

    return variable


@no_type_check
def require_one_of_types(variable: type_x, allowed_types: type_y) -> type_x:
    """
    Require one of the types specified

    Args:
        variable: variable to be type tested
        allowed_types: types allowed

    Returns:
        If assert is True, it returns the variable
    """
    assert any(
        isinstance(variable, allowed_type) for allowed_type in allowed_types
    ), f"Expected one of {allowed_types} types, got {type(variable)}!"

    return variable


@no_type_check
def require_all_of_type(iterable: type_y, expected_type: Type) -> type_y:
    """
    Require all objects from an iterable to be of the type specified

    Args:
        iterable: iterable of objects to be type tested
        expected_type: type allowed

    Returns:
        If assert is True, it returns the iterable passed
    """

    assert all(
        isinstance(variable, expected_type) for variable in iterable
    ), f"Expected all values in variable to be of type {expected_type}!"

    return iterable


@no_type_check
def require_type_or_none(
    variable: type_x, expected_type: Type
) -> Union[type_x, None]:
    """
    Require a type or None

    Args:
        variable: variable to be type tested
        expected_type: type allowed apart from None

    Returns:
        If assert is True, it returns the iterable passed
    """
    if variable is None:
        return None

    assert isinstance(
        variable, expected_type
    ), f"Expected type {expected_type}, got {type(variable)}!"

    return variable
