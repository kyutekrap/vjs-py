from ..base import HTMLBase, HTMLNode
from typing import List


class GridProps(HTMLBase):
    columns: int
    children: List[HTMLNode]
