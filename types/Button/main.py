from ..base import HTMLBase
from typing import Literal, NotRequired


class ButtonProps(HTMLBase):
    variant: Literal["filled", "outlined", "text"]
    size: Literal["big", "medium"]
    content: str
    type: Literal["button", "submit"]
    width: NotRequired[str]
    form: NotRequired[str]
    name: NotRequired[str]
