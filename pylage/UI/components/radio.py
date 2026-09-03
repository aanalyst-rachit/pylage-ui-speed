from __future__ import annotations

from typing import Any

from pylage.ENGINE import RadioGroup as _RadioGroup
from pylage.ENGINE import Style


def radio_group(
    *children: Any,
    style: Style | None = None,
    **props: Any,
):
    """Create a public PyLage UI Kit radio group using the existing engine RadioGroup."""
    return _RadioGroup(
        *children,
        style=style,
        **props,
    )


__all__ = ["radio_group"]
