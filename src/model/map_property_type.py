from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .collection_property_type import CollectionPropertyType


# Represents a property containing a key-value map where all values share the same schema.
class MapPropertyType(CollectionPropertyType):
    type: Literal["map"] = Field(alias="type")


