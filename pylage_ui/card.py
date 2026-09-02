from __future__ import annotations

from typing import Any

from pylage import Card as _Card
from pylage import Heading as _Heading
from pylage import Style
from pylage import Text as _Text
from pylage_layout.tokens import COLORS, RADIUS, SPACING


_VARIANT_STYLES: dict[str, Style] = {
    "default": Style(
        background_color=COLORS["background"],
        padding=SPACING["lg"],
        border_radius=RADIUS["xl"],
        border=f"1px solid {COLORS['border']}",
    ),
    "elevated": Style(
        background_color=COLORS["background"],
        padding=SPACING["lg"],
        border_radius=RADIUS["xl"],
        border=f"1px solid {COLORS['border_muted']}",
        box_shadow="0 10px 15px -3px rgba(0,0,0,0.1)",
    ),
    "outlined": Style(
        background_color=COLORS["background"],
        padding=SPACING["lg"],
        border_radius=RADIUS["xl"],
        border=f"1px solid {COLORS['border_muted']}",
    ),
    "interactive": Style(
        background_color=COLORS["background"],
        padding=SPACING["lg"],
        border_radius=RADIUS["xl"],
        border=f"1px solid {COLORS['border']}",
        cursor="pointer",
    ),
}


def card(
    *children: Any,
    heading: Any = None,
    body: Any = None,
    footer: Any = None,
    variant: str = "default",
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic UI Kit card using the existing PyLage Card."""

    if variant not in _VARIANT_STYLES:
        valid = ", ".join(_VARIANT_STYLES)
        raise ValueError(
            f"Unknown card variant {variant!r}. "
            f"Expected one of: {valid}."
        )

    semantic_children = []

    if heading is not None:
        semantic_children.append(_Heading(heading))

    if body is not None:
        semantic_children.append(_Text(body))

    if footer is not None:
        semantic_children.append(_Text(footer))

    semantic_children.extend(children)

    final_style = _VARIANT_STYLES[variant].merge(style)

    return _Card(
        *semantic_children,
        style=final_style,
        **props,
    )
