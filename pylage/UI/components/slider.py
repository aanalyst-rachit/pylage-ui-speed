from __future__ import annotations

from typing import Any

from pylage.ENGINE import Slider as _Slider
from pylage.ENGINE import Style


def slider(
    *,
    style: Style | None = None,
    **props: Any,
):
    """Create a public PyLage UI slider using the existing engine Slider."""
    return _Slider(
        style=style,
        **props,
    )


__all__ = ["slider"]
