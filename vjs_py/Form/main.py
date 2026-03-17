from ..base import HTMLBase, HTMLNode
from typing import List, NotRequired


class FormProps(HTMLBase):
    children: List[HTMLNode]
    title: NotRequired[str]
    showFooter: NotRequired[bool]
