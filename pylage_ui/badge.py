from __future__ import annotations

from typing import Any

from pylage import Badge as _Badge
from pylage import Text as _Text
from pylage.core.component import Component
from pylage import Style
from pylage_layout.tokens import COLORS, RADIUS


_VARIANT_STYLES: dict[str, Style] = {
    "default": Style(
        background_color=COLORS["surface_variant"],
        color=COLORS["text"],
        border=f"1px solid {COLORS['border']}",
    ),
    "primary": Style(
        background_color=COLORS["primary"],
        color=COLORS["primary_contrast"],
        border=f"1px solid {COLORS['primary']}",
    ),
    "secondary": Style(
        background_color=COLORS["secondary"],
        color=COLORS["secondary_contrast"],
        border=f"1px solid {COLORS['secondary']}",
    ),
    "success": Style(
        background_color=COLORS["success"],
        color=COLORS["primary_contrast"],
        border=f"1px solid {COLORS['success']}",
    ),
    "warning": Style(
        background_color=COLORS["warning"],
        color=COLORS["text"],
        border=f"1px solid {COLORS['warning']}",
    ),
    "danger": Style(
        background_color=COLORS["danger"],
        color=COLORS["primary_contrast"],
        border=f"1px solid {COLORS['danger']}",
    ),
    "info": Style(
        background_color=COLORS["info"],
        color=COLORS["primary_contrast"],
        border=f"1px solid {COLORS['info']}",
    ),
}

_BASE_STYLE = Style(
    padding="0.25rem 0.625rem",
    border_radius=RADIUS["full"],
    font_size="0.75rem",
    font_weight="600",
)


def badge(
    *children: Any,
    variant: str = "default",
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic UI Kit badge using the existing PyLage Badge."""
    if variant not in _VARIANT_STYLES:
        valid = ", ".join(_VARIANT_STYLES)
        raise ValueError(
            f"Unknown badge variant {variant!r}. Expected one of: {valid}."
        )

    default_style = _BASE_STYLE.merge(_VARIANT_STYLES[variant])
    final_style = default_style.merge(style)

    normalized_children = [
        child if isinstance(child, Component) else _Text(child)
        for child in children
        if child is not None
    ]

    return _Badge(*normalized_children, style=final_style, **props)
