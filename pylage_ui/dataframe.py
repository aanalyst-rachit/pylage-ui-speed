from __future__ import annotations

from typing import Any

from pylage import Style
from pylage import Table as _Table
from pylage_layout.tokens import COLORS, RADIUS

_DEFAULT_STYLE = Style(
    width="100%",
    border=f"1px solid {COLORS['border']}",
    border_radius=RADIUS["lg"],
    overflow="auto",
)


def dataframe(
    data: Any,
    *,
    headers: Any = None,
    style: Style | None = None,
    **props: Any,
):
    """Create a UI Kit DataFrame view.

    This is intentionally separate from ``table()``.

    DataFrame-like objects are passed through to the existing PyLage
    table normalization/renderer. No pandas dependency is imported
    or required by PyLage itself.
    """
    final_style = _DEFAULT_STYLE.merge(style)

    return _Table(
        data=data,
        headers=headers,
        style=final_style,
        class_name=props.pop("class_name", "pylage-dataframe"),
        **props,
    )
