from typing import NotRequired, Literal
from ..base import HTMLBase


class InputProps(HTMLBase):
    variant: NotRequired[Literal["number", "text", "date", "datetime-local", "checkbox", "radio", "password", "email", "url", "file"]]
    editable: NotRequired[bool]
    placeholder: NotRequired[str]
    value: NotRequired[str]
    width: NotRequired[str]
    name: NotRequired[str]
    required: NotRequired[bool]
    checked: NotRequired[bool]
