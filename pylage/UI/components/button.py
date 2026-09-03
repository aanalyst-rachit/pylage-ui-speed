from __future__ import annotations

from typing import Any

from pylage.ENGINE import Button as _Button
from pylage.ENGINE import Style
from pylage.UI.tokens import COLORS


_VARIANT_STYLES: dict[str, Style] = {
    "primary": Style(
        background_color=COLORS["primary"],
        color=COLORS["primary_contrast"],
        border=f"1px solid {COLORS['primary']}",
    ),
    "secondary": Style(
        background_color=COLORS["secondary"],
        color=COLORS["secondary_contrast"],
        border=f"1px solid {COLORS['secondary']}",
    ),
    "outline": Style(
        background_color=COLORS["background"],
        color=COLORS["primary_hover"],
        border=f"1px solid {COLORS['primary_hover']}",
    ),
    "ghost": Style(
        background_color="transparent",
        color=COLORS["text"],
        border="1px solid transparent",
    ),
    "danger": Style(
        background_color=COLORS["danger"],
        color=COLORS["primary_contrast"],
        border=f"1px solid {COLORS['danger']}",
    ),
}

_SIZE_STYLES: dict[str, Style] = {
    "sm": Style(
        padding="0.5rem 0.75rem",
        font_size="0.875rem",
    ),
    "md": Style(
        padding="0.625rem 1rem",
        font_size="1rem",
    ),
    "lg": Style(
        padding="0.75rem 1.25rem",
        font_size="1.125rem",
    ),
}

_BASE_STYLE = Style(
    border_radius="0.5rem",
    font_weight="600",
    cursor="pointer",
)


def button(
    text: Any,
    *,
    variant: str = "primary",
    size: str = "md",
    bg: Style | None = None,
    style: Style | None = None,
    **props: Any,
):
    """Create a semantic UI Kit button using the existing PyLage Button."""
    if variant not in _VARIANT_STYLES:
        valid = ", ".join(_VARIANT_STYLES)
        raise ValueError(
            f"Unknown button variant {variant!r}. "
            f"Expected one of: {valid}."
        )

    if size not in _SIZE_STYLES:
        valid = ", ".join(_SIZE_STYLES)
        raise ValueError(
            f"Unknown button size {size!r}. "
            f"Expected one of: {valid}."
        )

    default_style = _BASE_STYLE.merge(_VARIANT_STYLES[variant])
    default_style = default_style.merge(_SIZE_STYLES[size])
    # ``bg`` is a public convenience API.  It accepts a Style
    # preset such as ``style.black`` and merges it before the
    # explicit ``style=`` override.
    if bg is not None and not isinstance(bg, Style):
        raise TypeError("bg must be a Style or None")

    final_style = default_style.merge(bg).merge(style)

    return _Button(text, style=final_style, **props)
