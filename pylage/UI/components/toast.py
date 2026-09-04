from __future__ import annotations

from typing import Any

from pylage.ENGINE import Style
from pylage.ENGINE import Text as _Text
from pylage.ENGINE import Toast as _Toast
from pylage.ENGINE.core.component import Component
from pylage.UI.tokens import COLORS, RADIUS, SPACING


__all__ = ["toast"]


_VARIANT_STYLES: dict[str, Style] = {
    "default": Style(
        background_color=COLORS["surface_variant"],
        color=COLORS["text"],
        border="1px solid " + COLORS["border"],
    ),
    "info": Style(
        background_color=COLORS["info"],
        color=COLORS["primary_contrast"],
        border="1px solid " + COLORS["info"],
    ),
    "success": Style(
        background_color=COLORS["success"],
        color=COLORS["primary_contrast"],
        border="1px solid " + COLORS["success"],
    ),
    "warning": Style(
        background_color=COLORS["warning"],
        color=COLORS["text"],
        border="1px solid " + COLORS["warning"],
    ),
    "danger": Style(
        background_color=COLORS["danger"],
        color=COLORS["primary_contrast"],
        border="1px solid " + COLORS["danger"],
    ),
    "error": Style(
        background_color=COLORS["danger"],
        color=COLORS["primary_contrast"],
        border="1px solid " + COLORS["danger"],
    ),
}


_BASE_STYLE = Style(
    display="flex",
    flex_direction="column",
    gap=SPACING["xs"],
    padding=SPACING["md"],
    border_radius=RADIUS["md"],
)


def toast(
    *children: Any,
    variant: str = "default",
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic UI Kit toast using the existing PyLage Toast."""
    if variant not in _VARIANT_STYLES:
        valid = ", ".join(_VARIANT_STYLES)
        raise ValueError(
            f"Unknown toast variant {variant!r}. Expected one of: {valid}."
        )

    final_style = _BASE_STYLE.merge(_VARIANT_STYLES[variant]).merge(style)

    normalized_children = [
        child if isinstance(child, Component) else _Text(child)
        for child in children
        if child is not None
    ]

    return _Toast(*normalized_children, style=final_style, **props)
