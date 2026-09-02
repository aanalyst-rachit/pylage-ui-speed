from __future__ import annotations

from typing import Any

from pylage import Style
from pylage_layout.patterns import Metric as _Metric
from pylage_layout.tokens import COLORS, RADIUS, SPACING


_DEFAULT_STYLE = Style(
    background_color=COLORS["background"],
    padding=SPACING["lg"],
    border_radius=RADIUS["xl"],
    border=f"1px solid {COLORS['border']}",
)


def metric(
    label: Any,
    value: Any,
    delta: Any = None,
    description: Any = None,
    *, style: Style | None = None,
    **props: Any,
):
    """Create a semantic UI Kit metric using the existing PyLage metric pattern."""
    final_style = _DEFAULT_STYLE.merge(style)

    return _Metric(
        label=label,
        value=value,
        delta=delta,
        description=description,
        style=final_style,
        **props,
    )
