from __future__ import annotations
from typing_extensions import TypeAlias
from typing import (
    Any,
    Dict,
    Literal,
    Mapping,
    Set,
    Union,
)
from pydantic import BaseModel, ConfigDict

IncEx: TypeAlias = Union[Set[int], Set[str], Dict[int, Any], Dict[str, Any], None]

AccessMode: TypeAlias = Literal["w", "w+", "r", "a"]


class StrictBase(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")


def ensure_member_name(data: Any) -> str:
    """
    If the input is a string, then ensure that it is a valid
    name for a subnode in a zarr group
    """
    if isinstance(data, str):
        if "/" in data:
            raise ValueError(
                f'Strings containing "/" are invalid. Got {data}, which violates this rule.'
            )
        if data in ("", ".", ".."):
            raise ValueError(f"The string {data} is not a valid member name.")
        return data
    raise TypeError(f"Exected a str, got {type(data)}.")


def ensure_key_no_path(data: Any) -> Any:
    if isinstance(data, Mapping):
        [ensure_member_name(key) for key in data.keys()]
    return data


def model_like(
    a: BaseModel, b: BaseModel, exclude: IncEx = None, include: IncEx = None
) -> bool:
    """
    A similarity check for a pair pydantic.BaseModel, parametrized over included or excluded fields.


    """

    a_dict = a.model_dump(exclude=exclude, include=include)
    b_dict = b.model_dump(exclude=exclude, include=include)

    return a_dict == b_dict
