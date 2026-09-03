from __future__ import annotations

from typing import Any

from pylage.ENGINE import Form as _Form
from pylage.ENGINE import Style


def form(
    *children: Any,
    style: Style | None = None,
    **props: Any,
):
    """Create a public PyLage UI form using the existing engine Form."""
    return _Form(
        *children,
        style=style,
        **props,
    )


__all__ = ["form"]
