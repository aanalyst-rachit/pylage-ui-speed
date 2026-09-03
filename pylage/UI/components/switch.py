from __future__ import annotations

from typing import Any

from pylage.ENGINE import Switch as _Switch
from pylage.ENGINE import Style


def switch(
    *,
    style: Style | None = None,
    **props: Any,
):
    """Create a public PyLage UI switch using the existing engine Switch."""
    return _Switch(
        style=style,
        **props,
    )


__all__ = ["switch"]
