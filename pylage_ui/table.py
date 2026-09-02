from __future__ import annotations

from typing import Any

from pylage import Style
from pylage import Table as _Table
from pylage_layout.tokens import COLORS, RADIUS


_DEFAULT_STYLE = Style(
    width="100%",
    border=f"1px solid {COLORS['border']}",
    border_radius=RADIUS["lg"],
    overflow="hidden",
)


def table(
    data: Any = None,
    *,
    headers: Any = None,
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic UI Kit table using the existing PyLage Table."""
    final_style = _DEFAULT_STYLE.merge(style)

    return _Table(
        data=data,
        headers=headers,
        style=final_style,
        **props,
    )
