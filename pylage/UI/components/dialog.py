from __future__ import annotations

from typing import Any

from pylage.ENGINE import Dialog as _Dialog
from pylage.ENGINE import Style
from pylage.ENGINE.core.component import Component
from pylage.UI.tokens import COLORS, RADIUS, SPACING


__all__ = ["dialog"]


_BASE_STYLE = Style(
    padding=SPACING["lg"],
    background_color=COLORS["background"],
    color=COLORS["text"],
    border=f"1px solid {COLORS['border']}",
    border_radius=RADIUS["xl"],
)


def dialog(
    *children: Any,
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic UI Kit dialog using the existing PyLage Dialog."""

    normalized_children = [
        child for child in children
        if child is not None
    ]

    final_style = _BASE_STYLE.merge(style)

    return _Dialog(
        *normalized_children,
        style=final_style,
        **props,
    )
