from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .scalar_property_type import ScalarPropertyType


# Represents a whole number without fractional components.
class IntegerPropertyType(ScalarPropertyType):
    type: Literal["integer"] = Field(alias="type")


