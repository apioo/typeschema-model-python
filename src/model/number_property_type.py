from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .scalar_property_type import ScalarPropertyType


# Represents a floating-point or decimal number.
class NumberPropertyType(ScalarPropertyType):
    type: Literal["number"] = Field(alias="type")
    pass


