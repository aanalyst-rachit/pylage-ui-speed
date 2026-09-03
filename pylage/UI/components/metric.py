from __future__ import annotations

from typing import Any

from pylage.ENGINE import Style
from pylage.ENGINE import Card as _Card
from pylage.ENGINE import Column as _Column
from pylage.ENGINE import Heading as _Heading
from pylage.ENGINE import Text as _Text

from pylage.UI.tokens import COLORS, RADIUS, SPACING


_DEFAULT_CARD_STYLE = Style(
    display="flex",
    flex_direction="column",
    gap=SPACING["sm"],
    padding=SPACING["lg"],
    background_color=COLORS["background"],
    border=f"1px solid {COLORS['border']}",
    border_radius=RADIUS["xl"],
)


_LABEL_STYLE = Style(
    font_size="0.875rem",
    font_weight="500",
    color=COLORS["text_muted"],
    margin="0",
)


_VALUE_STYLE = Style(
    font_size="1.75rem",
    font_weight="700",
    color=COLORS["text"],
    margin="0",
)


_DELTA_STYLE = Style(
    font_size="0.875rem",
    font_weight="600",
    color=COLORS["success"],
    margin="0",
)


_DESCRIPTION_STYLE = Style(
    font_size="0.75rem",
    color=COLORS["text_muted"],
    margin="0",
)


def metric(
    label: Any,
    value: Any,
    delta: Any = None,
    description: Any = None,
    *,
    featured: bool = False,
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic KPI/metric card using only PyLage engine primitives."""

    items: list[Any] = []

    if label is not None:
        items.append(_Text(label, style=_LABEL_STYLE))

    if value is not None:
        items.append(_Heading(value, level=2, style=_VALUE_STYLE))

    if delta is not None:
        items.append(_Text(delta, style=_DELTA_STYLE))

    if description is not None:
        items.append(_Text(description, style=_DESCRIPTION_STYLE))

    card_style = _DEFAULT_CARD_STYLE

    if featured:
        card_style = card_style.merge(
            Style(
                border=f"2px solid {COLORS['primary']}",
            )
        )

    final_style = card_style.merge(style)

    return _Card(
        _Column(
            *items,
            style=Style(
                display="flex",
                flex_direction="column",
                gap=SPACING["sm"],
            ),
        ),
        style=final_style,
        **props,
    )
