from __future__ import annotations

from typing import Any

from pylage.ENGINE import Input as _Input
from pylage.ENGINE import Style


def input(
    value: Any = "",
    *,
    input_type: str | None = None,
    style: Style | None = None,
    **props: Any,
):
    """Create a public PyLage UI input using the existing engine Input."""
    return _Input(
        value=value,
        input_type=input_type,
        style=style,
        **props,
    )


__all__ = ["input"]
