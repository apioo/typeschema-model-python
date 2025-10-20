from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .scalar_property_type import ScalarPropertyType


# Represents a string value
class StringPropertyType(ScalarPropertyType):
    default: Optional[str] = Field(default=None, alias="default")
    format: Optional[str] = Field(default=None, alias="format")
    pass


