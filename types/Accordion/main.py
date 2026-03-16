from ..HBox.main import HBoxProps
from ..base import HTMLBase, HTMLNode
from typing import List


class AccordionProps(HTMLBase):
    caption: HBoxProps
    children: List[HTMLNode]
