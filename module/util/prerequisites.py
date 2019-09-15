"""
Prerequisite functions to help and assert inputs and outputs condition and type
"""

from typing import TypeVar, Collection, Type, Iterable, Union, no_type_check

# create a type var to then tests if input type is the same as output type for example
type_x = TypeVar("type_x")
types_xy = TypeVar("types_xy", bound=Iterable)


# conditions
def require(condition: bool, message: str = "Requirement failed!"):
    """
    Require for a condition

    :param condition: bool condition
    :param message: message to display in case of False condition
    """
    assert condition, message


def require_one_in_all(
    collection_conditions: Collection,
    message: str = "Not even one requirement met!",
):
    """
    Require for a condition in a collection

    :param collection_conditions: collection of conditions
    :param message: message to display in case no True condition
    """
    assert any(collection_conditions), message


def require_all_in_all(
    collection_conditions: Collection,
    message: str = "Not all requirements met!",
):
    """
    Require for a condition in a collection

    :param collection_conditions: collection of conditions
    :param message: message to display in case of False condition
    """
    assert all(collection_conditions), message


# types
@no_type_check
def require_type(variable: type_x, expected_type: Type) -> type_x:
    """
    Require that checks a variable type

    :param variable: variable to tests
    :param expected_type: expected variable type

    :return: the same inputted variable
    """
    assert isinstance(
        variable, expected_type
    ), f"Expected type {expected_type}, got {type(variable)}!"

    return variable


@no_type_check
def require_one_of_types(variable: type_x, allowed_types: types_xy) -> type_x:
    """
    Require that checks that a variable has an allowed type

    :param variable: variable to tests
    :param allowed_types: iterable with the allowed types

    :return: the same inputted variable
    """
    assert any(
        isinstance(variable, allowed_type) for allowed_type in allowed_types
    ), f"Expected one of {allowed_types} types, got {type(variable)}!"

    return variable


@no_type_check
def require_all_of_type(iterable: types_xy, expected_type: Type) -> types_xy:
    """
    Require to tests that all variables in iterable are of expected type

    :param iterable: iterable with variables to tests
    :param expected_type: expected type to tests

    :return: the same inputted iterable
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
    Require to tests if a variable is of some type or None

    :param variable: variable to tests
    :param expected_type: expected type of variable

    :return: the same inputted variable
    """
    if variable is None:
        return None

    assert isinstance(
        variable, expected_type
    ), f"Expected type {expected_type}, got {type(variable)}!"

    return variable
