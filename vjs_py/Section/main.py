from ..base import HTMLBase, HTMLNode
from typing import List


class SectionProps(HTMLBase):
    children: List[HTMLNode]
