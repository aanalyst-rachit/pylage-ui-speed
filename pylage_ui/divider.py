from __future__ import annotations

from typing import Any

from pylage import Divider as _Divider
from pylage import Style


_DEFAULT_STYLE = Style(
    width="100%",
    border="0",
    border_top="1px solid #e2e8f0",
    margin="1rem 0",
)


def divider(*, style: Style | None = None, **props: Any):
    """Create a semantic UI Kit divider using the existing PyLage Divider."""
    final_style = _DEFAULT_STYLE.merge(style)
    return _Divider(style=final_style, **props)
