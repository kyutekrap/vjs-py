from typing import NotRequired
from ..base import HTMLBase


class FileInputProps(HTMLBase):
    value: NotRequired[str]
    editable: NotRequired[bool]
    placeholder: NotRequired[str]
    width: NotRequired[str]
    name: NotRequired[str]
    required: NotRequired[bool]
    multiselect: NotRequired[bool]
    accept: str
    size: int
