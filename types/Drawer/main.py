from ..BgButton.main import BgButtonProps
from ..base import HTMLBase, HTMLNode
from typing import List, NotRequired


class DrawerProps(HTMLBase):
    children: List[HTMLNode]
    closeBgButton: NotRequired[BgButtonProps]
