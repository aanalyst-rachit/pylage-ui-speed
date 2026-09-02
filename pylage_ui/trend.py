from __future__ import annotations

from typing import Any

from pylage import Badge as _Badge
from pylage import Style, Text as _Text
from pylage.core.component import Component
from pylage_layout.tokens import COLORS, RADIUS


_DIRECTION_CONFIG: dict[str, tuple[str, str]] = {
    "up": ("↑", "success"),
    "down": ("↓", "danger"),
    "neutral": ("→", "secondary"),
}

_VARIANT_STYLES: dict[str, Style] = {
    "success": Style(
        background_color=COLORS["success"],
        color=COLORS["primary_contrast"],
        border=f"1px solid {COLORS['success']}",
    ),
    "danger": Style(
        background_color=COLORS["danger"],
        color=COLORS["primary_contrast"],
        border=f"1px solid {COLORS['danger']}",
    ),
    "secondary": Style(
        background_color=COLORS["secondary"],
        color=COLORS["secondary_contrast"],
        border=f"1px solid {COLORS['secondary']}",
    ),
}

_BASE_STYLE = Style(
    padding="0.25rem 0.625rem",
    border_radius=RADIUS["full"],
    font_size="0.75rem",
    font_weight="600",
)


def _detect_direction(value: Any) -> str:
    resolved = str(getattr(value, "value", value))

    if resolved.startswith("+"):
        return "up"

    if resolved.startswith("-"):
        return "down"

    return "neutral"


def trend(
    value: Any,
    *,
    direction: str | None = None,
    show_indicator: bool = True,
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic UI Kit trend indicator.

    Direction is automatically detected from leading ``+`` or ``-`` signs
    unless explicitly provided.
    """
    final_direction = direction or _detect_direction(value)

    if final_direction not in _DIRECTION_CONFIG:
        valid = ", ".join(_DIRECTION_CONFIG)
        raise ValueError(
            f"Unknown trend direction {final_direction!r}. "
            f"Expected one of: {valid}."
        )

    indicator, variant = _DIRECTION_CONFIG[final_direction]

    default_style = _BASE_STYLE.merge(_VARIANT_STYLES[variant])
    final_style = default_style.merge(style)

    children = []

    if show_indicator:
        children.append(_Text(indicator))

    children.append(
        value if isinstance(value, Component) else _Text(value)
    )

    return _Badge(
        *children,
        style=final_style,
        **props,
    )
