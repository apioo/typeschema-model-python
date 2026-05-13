from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal


# The base abstract type for all schema definitions. It provides metadata common to all types such as descriptions and deprecation status.
class DefinitionType(BaseModel):
    deprecated: Optional[bool] = Field(default=None, alias="deprecated")
    description: Optional[str] = Field(default=None, alias="description")
    type: str = Field(alias="type")
    pass


