from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .property_type import PropertyType


# Represents a generic value which can be replaced with a concrete type
class GenericPropertyType(PropertyType):
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[str] = Field(default="generic", alias="type")
    pass


