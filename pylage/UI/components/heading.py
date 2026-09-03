from __future__ import annotations

from typing import Any

from pylage.ENGINE import Heading as _Heading
from pylage.ENGINE import Style


def heading(
    value: Any,
    *,
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic UI Kit heading using the existing PyLage Heading."""

    return _Heading(
        value,
        style=style,
        **props,
    )
