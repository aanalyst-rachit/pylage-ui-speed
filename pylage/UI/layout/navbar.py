from typing import Any

from pylage.ENGINE.components.basic import Navigation as _Navigation
from pylage.ENGINE.core.component import Component
from pylage.ENGINE.styling.style import Style


def navbar(*children: Any, style: Style | None = None, **props: Any) -> Component:
    base_style = Style(
        display="flex",
        align_items="center",
        justify_content="space-between",
        width="100%",
        padding="1rem 1.5rem",
    )
    return _Navigation(*children, style=style or base_style, **props)


# Backward-compatible CamelCase alias.
Navbar = navbar


__all__ = ["navbar", "Navbar"]
