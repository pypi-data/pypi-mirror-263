from pydantic import BaseModel
from typing import Any

class DictSchema(BaseModel):
    key: TypeData
    value: TypeData

class LegacyDictSchema(BaseModel):
    key_type: str
    value_type: str

class TypeData(BaseModel):
    type: str
    items: TypeData | DictSchema | LegacyDictSchema | None
    default: Any
