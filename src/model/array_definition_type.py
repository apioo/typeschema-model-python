from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .collection_definition_type import CollectionDefinitionType


# Represents an ordered list of elements where every item conforms to the same schema.
class ArrayDefinitionType(CollectionDefinitionType):
    type: Literal["array"] = Field(alias="type")


