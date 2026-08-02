from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal


# The abstract base type for all property definitions within a struct or collection.
class PropertyType(BaseModel):
    deprecated: Optional[bool] = Field(default=None, alias="deprecated")
    description: Optional[str] = Field(default=None, alias="description")
    nullable: Optional[bool] = Field(default=None, alias="nullable")
    type: str = Field(alias="type")


