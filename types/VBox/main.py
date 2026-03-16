from ..base import HTMLBase, HTMLNode
from typing import List


class VBoxProps(HTMLBase):
    children: List[HTMLNode]
