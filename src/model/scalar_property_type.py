from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .property_type import PropertyType


# The abstract base type for simple scalar value properties (strings, integers, numbers, booleans).
class ScalarPropertyType(PropertyType):


