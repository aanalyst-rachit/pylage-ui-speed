from __future__ import annotations

from typing import Any
from pylage.ENGINE import Column as _Column
from pylage.ENGINE import Heading as _Heading
from pylage.ENGINE import Style
from pylage.ENGINE import Text as _Text
from pylage.UI.tokens import COLORS, RADIUS, SPACING

_DEFAULT_CONTAINER_STYLE = Style(
    display="flex",
    flex_direction="column",
    align_items="center",
    justify_content="center",
    text_align="center",
    padding=SPACING["2xl"],
    background_color=COLORS["background"],
    border=f"1px dashed {COLORS['border_muted']}",
    border_radius=RADIUS["xl"],
    gap=SPACING["sm"],
)

_TITLE_STYLE = Style(
    font_size="1.125rem",
    font_weight="600",
    color=COLORS["text"],
    margin="0",
)

_DESC_STYLE = Style(
    font_size="0.875rem",
    color=COLORS["text_muted"],
    max_width="28rem",
    margin="0",
    line_height="1.5",
)

_ICON_CONTAINER_STYLE = Style(
    display="inline-flex",
    align_items="center",
    justify_content="center",
    width="3.5rem",
    height="3.5rem",
    border_radius=RADIUS["full"],
    background_color=COLORS["surface"],
    color=COLORS["text_muted"],
    font_size="1.5rem",
    margin_bottom=SPACING["xs"],
)

def empty_state(
    title: Any = "No data found",
    description: Any = "There are no items or records to display at this time.",
    *,
    icon: Any = None,
    action: Any = None,
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic, high-level UI Kit empty state card."""
    items: list[Any] = []

    if icon is not None:
        if isinstance(icon, str):
            items.append(_Text(icon, style=_ICON_CONTAINER_STYLE))
        else:
            items.append(icon)

    if title is not None:
        items.append(_Heading(title, style=_TITLE_STYLE))

    if description is not None:
        items.append(_Text(description, style=_DESC_STYLE))

    if action is not None:
        items.append(action)

    final_style = _DEFAULT_CONTAINER_STYLE.merge(style)

    return _Column(
        *items,
        style=final_style,
        **props,
    )
