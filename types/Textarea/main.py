from typing import NotRequired, Literal
from ..base import HTMLBase


class TextareaProps(HTMLBase):
    value: NotRequired[str]
    lines: int
    editable: NotRequired[bool]
    placeholder: NotRequired[str]
    width: NotRequired[str]
    resize: Literal["none", "both", "horizontal", "vertical"]
    name: NotRequired[str]
    required: NotRequired[bool]
