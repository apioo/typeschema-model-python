from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .collection_definition_type import CollectionDefinitionType


# Represents a key-value map with dynamic key names where all values conform to the same schema.
class MapDefinitionType(CollectionDefinitionType):
    type: Literal["map"] = Field(alias="type")


