from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .collection_definition_type import CollectionDefinitionType


# An object with a dynamic set of keys where every value conforms to the same schema.
class MapDefinitionType(CollectionDefinitionType):
    type: Literal["map"] = Field(alias="type")
    pass


