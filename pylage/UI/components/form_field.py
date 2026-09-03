from __future__ import annotations

from typing import Any

from pylage.ENGINE import Style
from pylage.UI.components.text import text
from pylage.UI.layout.factories import Stack


def form_field(
    child: Any,
    *,
    label: Any = None,
    help_text: Any = None,
    error: Any = None,
    required: bool = False,
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic form field around an existing input control.

    FormField is a composition component. It does not introduce a new
    renderer or input implementation; it arranges an existing control
    together with its label, help text, and error presentation.
    """

    children: list[Any] = []

    if label is not None:
        label_value = f"{label} *" if required else label
        children.append(text(label_value, label=True))

    children.append(child)

    if help_text is not None:
        children.append(text(help_text, muted=True, caption=True))

    if error is not None:
        children.append(text(error))

    return Stack(
        *children,
        style=style,
        **props,
    )


__all__ = ["form_field"]
