from typing import NotRequired
from ..base import HTMLBase


class BgButtonProps(HTMLBase):
    src: str
    rounded: NotRequired[bool]
    width: str
    height: str
    badge: NotRequired[str]
