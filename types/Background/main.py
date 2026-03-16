from typing import NotRequired
from ..base import HTMLBase


class BackgroundProps(HTMLBase):
    width: str
    height: str
    src: str
    badge: NotRequired[str]
