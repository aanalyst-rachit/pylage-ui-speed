from __future__ import annotations

from typing import Any

from pylage.ENGINE import DatePicker as _DatePicker
from pylage.ENGINE import Style


def datepicker(
    *,
    style: Style | None = None,
    **props: Any,
):
    """Create a public PyLage UI date picker using the existing engine DatePicker."""
    return _DatePicker(
        style=style,
        **props,
    )


__all__ = ["datepicker"]
