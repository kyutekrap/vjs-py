from typing import NotRequired, List
from ..base import HTMLBase


class SelectProps(HTMLBase):
    options: List[str]
    selected: NotRequired[str]
    editable: NotRequired[bool]
    placeholder: NotRequired[str]
    width: NotRequired[str]
    required: NotRequired[bool]
    multiselect: NotRequired[bool]
    searchable: NotRequired[bool]
    name: NotRequired[str]
