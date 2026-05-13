from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .property_type import PropertyType


# A placeholder for a type that will be specified at runtime or through template arguments.
class GenericPropertyType(PropertyType):
    type: Literal["generic"] = Field(alias="type")
    name: Optional[str] = Field(default=None, alias="name")
    pass


