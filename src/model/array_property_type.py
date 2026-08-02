from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .collection_property_type import CollectionPropertyType


# Represents a property containing a list of items that share the same schema.
class ArrayPropertyType(CollectionPropertyType):
    type: Literal["array"] = Field(alias="type")


