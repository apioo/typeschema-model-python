from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .property_type import PropertyType


# A wildcard property that accepts any valid JSON value (object, array, string, etc.).
class AnyPropertyType(PropertyType):
    type: Literal["any"] = Field(alias="type")
    pass


