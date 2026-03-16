from typing import NotRequired, List, Literal
from ..base import HTMLBase


class IFrameProps(HTMLBase):
    srcdoc: NotRequired[str]
    src: NotRequired[str]
    title: NotRequired[str]
    sandbox: NotRequired[List[str]]
    referrerpolicy: NotRequired[Literal["", "no-referrer", "no-referrer-when-downgrade", "origin", "origin-when-cross-origin", "same-origin", "strict-origin", "strict-origin-when-cross-origin", "unsafe-url"]]
    allow: NotRequired[str]
