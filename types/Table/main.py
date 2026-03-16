from typing import NotRequired, List, Dict, TypedDict, Any, Literal
from ..HBox.main import HBoxProps
from ..base import HTMLBase, HTMLCallable


class TableColumn(TypedDict):
    label: NotRequired[str]
    value: str


class TableCell(TypedDict):
    label: NotRequired[str]
    value: Any
    href: NotRequired[str]
    checked: NotRequired[bool]
    editable: NotRequired[bool]
    list: List[str]
    textAlign: NotRequired[Literal["left", "center", "right"]]
    events: NotRequired[Dict[Literal["click", "change"], HTMLCallable]]


class TableProps(HTMLBase):
    title: NotRequired[str]
    columns: List[TableColumn]
    data: List[Dict[str, TableCell]]
    resizable: NotRequired[bool]
    checkbox: NotRequired[bool]
    sortable: NotRequired[bool]
    footer: NotRequired[HBoxProps]
    skeletonLines: NotRequired[int]
    fixedLeftColumn: NotRequired[bool]
    fixedRightColumn: NotRequired[bool]
    fixedBottomRow: NotRequired[bool]
