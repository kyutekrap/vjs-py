from ..base import HTMLBase, HTMLNode
from typing import List, NotRequired, Literal


class HBoxProps(HTMLBase):
    children: List[HTMLNode]
    startFrom: NotRequired[Literal["right", "left"]]
