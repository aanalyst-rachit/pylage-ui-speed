from __future__ import annotations

from typing import Any

from pylage.ENGINE import Select as _Select
from pylage.ENGINE import Style


def select(
    *children: Any,
    style: Style | None = None,
    **props: Any,
):
    """Create a public PyLage UI select using the existing engine Select."""
    return _Select(
        *children,
        style=style,
        **props,
    )


__all__ = ["select"]
