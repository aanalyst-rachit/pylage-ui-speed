from __future__ import annotations

from typing import Any

from pylage.ENGINE import Checkbox as _Checkbox
from pylage.ENGINE import Style


def checkbox(
    *,
    style: Style | None = None,
    **props: Any,
):
    """Create a public PyLage UI checkbox using the existing engine Checkbox."""
    return _Checkbox(
        style=style,
        **props,
    )


__all__ = ["checkbox"]
