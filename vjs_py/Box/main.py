from ..base import HTMLBase, HTMLNode
from typing import List


class BoxProps(HTMLBase):
    children: List[HTMLNode]
