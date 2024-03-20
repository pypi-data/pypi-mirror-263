from dataclasses import dataclass
from enum import Enum, auto
from typing import Union


class SpecialToken(Enum):
    EmptyArgument = auto()


Expression = Union[str, "FuncCall", SpecialToken]


@dataclass
class FuncCall:
    name: str
    args: list[Expression]
