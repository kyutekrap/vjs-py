from typing import Literal, NotRequired
from ..base import HTMLBase


class LinkProps(HTMLBase):
    size: Literal["medium", "small"]
    variant: Literal["primary", "secondary"]
    text: str
    href: NotRequired[str]
