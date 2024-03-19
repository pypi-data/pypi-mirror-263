#
#  Copyright 2024 by C Change Labs Inc. www.c-change-labs.com
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  This software was developed with support from the Skanska USA,
#  Charles Pankow Foundation, Microsoft Sustainability Fund, Interface, MKA Foundation, and others.
#  Find out more at www.BuildingTransparency.org
#
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Annotated, Callable, TypeAlias

import pydantic as pyd

from openepd.model.common import OpenEPDUnit

if TYPE_CHECKING:
    from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec

    QuantityValidatorType = Callable[[type[BaseOpenEpdHierarchicalSpec], str], str]


class QuantityValidator(ABC):
    """
    Interface for quantity validator.

    The openEPD models are mapped using the simple types. Caller code should provide their own implementation of this
    and set it with `set_unit_validator` function.
    """

    @abstractmethod
    def validate_unit_correctness(self, value: str, dimensionality: str) -> None:
        """
        Validate the given string value against the given dimensionality.

        Args:
            value: The value to validate, like "102.4 kg"
            dimensionality: The dimensionality to validate against, like "kg"
        Returns:
            None if the value is valid, raises an error otherwise.
        Raises:
            ValueError: If the value is not valid.
        """
        pass

    @abstractmethod
    def validate_quantity_greater_or_equal(self, value: str, min_value: str) -> None:
        """
        Validate the quantity is greater than minimal value.

        Args:
            value: The value to validate, like "2.4 kg"
            min_value: The value to compare with, like "102.4 kg"
        Returns:
            None if the value is valid, raises an error otherwise.
        Raises:
            ValueError: If the value is not valid.
        """
        pass

    @abstractmethod
    def validate_quantity_less_or_equal(self, value: str, max_value: str) -> None:
        """
        Validate the quantity is less than minimal value.

        Args:
            value: The value to validate, like "2.4 kg"
            max_value: The value to compare with, like "0.4 kg"
        Returns:
            None if the value is valid, raises an error otherwise.
        Raises:
            ValueError: If the value is not valid.
        """
        pass


def validate_unit_factory(dimensionality: OpenEPDUnit | str) -> "QuantityValidatorType":
    """Create validator for quantity field to check unit matching."""

    def validator(cls: "type[BaseOpenEpdHierarchicalSpec]", value: str) -> str:
        if hasattr(cls, "_QUANTITY_VALIDATOR") and cls._QUANTITY_VALIDATOR is not None:
            cls._QUANTITY_VALIDATOR.validate_unit_correctness(value, dimensionality)
        return value

    return validator


def validate_quantity_ge_factory(min_value: str) -> "QuantityValidatorType":
    """Create validator to check that quantity is greater than or equal to min_value."""

    def validator(cls: "type[BaseOpenEpdHierarchicalSpec]", value: str) -> str:
        if hasattr(cls, "_QUANTITY_VALIDATOR") and cls._QUANTITY_VALIDATOR is not None:
            cls._QUANTITY_VALIDATOR.validate_quantity_greater_or_equal(value, min_value)
        return value

    return validator


def validate_quantity_le_factory(max_value: str) -> "QuantityValidatorType":
    """Create validator to check that quantity is less than or equal to max_value."""

    def validator(cls: "type[BaseOpenEpdHierarchicalSpec]", value: str) -> str:
        if hasattr(cls, "_QUANTITY_VALIDATOR") and cls._QUANTITY_VALIDATOR is not None:
            cls._QUANTITY_VALIDATOR.validate_quantity_less_or_equal(value, max_value)
        return value

    return validator


# todo with the migration to Pydantic 2 we will be able to use pydantic.funcational_validators.AfterDecorator
# this will let us bind the validator not to the model or the field, but to the type itself.

# for abitrary non-standard quantity
QuantityStr: TypeAlias = Annotated[str, pyd.Field()]
PressureMPaStr: TypeAlias = Annotated[str, pyd.Field(example="30 MPa")]
MassKgStr: TypeAlias = Annotated[str, pyd.Field(example="30 kg")]
LengthMmStr: TypeAlias = Annotated[str, pyd.Field(example="30 mm")]
AreaM2Str: TypeAlias = Annotated[str, pyd.Field(example="12 m2")]
LengthMStr: TypeAlias = Annotated[str, pyd.Field(example="30 m")]
TemperatureCStr: TypeAlias = Annotated[str, pyd.Field(example="45 C")]
HeatConductanceUCIStr: TypeAlias = Annotated[str, pyd.Field(example="0.3 U")]
GwpKgCo2eStr: TypeAlias = Annotated[str, pyd.Field(example="300 kgCO2e")]
