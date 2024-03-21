from functools import cached_property as cached_property
from pydantic import BaseModel
from typing import Any

class PropertyAst(BaseModel):
    name: str
    types: list[NestedPropertyTypeAst | PropertyValueAst]
    value: PropertyValueAst | None
    @property
    def ast(self) -> Any: ...

class PropertyValueAst(BaseModel):
    attr: tuple[str, str] | None
    name: str | None
    constant: Any | None
    @property
    def ast(self) -> Any: ...

class NestedPropertyTypeAst(BaseModel):
    root: PropertyValueAst
    child: list['PropertyValueAst']
    @property
    def ast(self) -> Any: ...

class CustomCodeAst(BaseModel):
    custom_code: str
    @cached_property
    def ast_module(self) -> Any: ...
    @property
    def ast(self) -> list[Any]: ...
    @property
    def ast_imports(self) -> list[Any]: ...

def join_property_values(items: list[NestedPropertyTypeAst | PropertyValueAst] | list['PropertyValueAst']) -> Any: ...
