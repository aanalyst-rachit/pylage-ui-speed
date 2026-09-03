from __future__ import annotations

from typing import Any

from pylage.ENGINE import DataFrame as _DataFrame
from pylage.ENGINE import Style
from pylage.UI.tokens import COLORS, RADIUS


_DEFAULT_STYLE = Style(
    width="100%",
    border=f"1px solid {COLORS['border']}",
    border_radius=RADIUS["lg"],
    overflow="hidden",
)


def dataframe(
    data: Any,
    *,
    headers: Any = None,
    style: Style | None = None,
    cell_border: bool = True,
    **props: Any,
):
    """Create an Excel-like DataFrame view.

    ``dataframe()`` is intentionally separate from ``table()``.
    """
    final_style = _DEFAULT_STYLE.merge(style)

    return _DataFrame(
        data=data,
        headers=headers,
        style=final_style,
        cell_border=cell_border,
        class_name=props.pop("class_name", "pylage-dataframe"),
        **props,
    )
