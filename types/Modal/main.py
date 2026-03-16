from typing import NotRequired
from ..BgButton.main import BgButtonProps
from ..base import HTMLBase


class ModalProps(HTMLBase):
    closeBgButton: NotRequired[BgButtonProps]
