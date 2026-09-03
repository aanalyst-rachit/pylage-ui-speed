"""Public PyLage style presets.

This module intentionally exposes style values rather than the
ENGINE Style class itself.

Usage:

    from pylage import style

    ps.button("Save", bg=style.black)
    ps.card(..., style=style.elevated_card)
    ps.topheader(..., style=style.topheader)
"""

from pylage.ENGINE.styling.style import Style


black = Style(
    background_color="#000000",
    color="#ffffff",
)

white = Style(
    background_color="#ffffff",
    color="#000000",
)

elevated_card = Style(
    box_shadow="0 10px 15px -3px rgba(0,0,0,0.1)",
)

topheader = Style(
    display="flex",
    align_items="center",
    justify_content="space-between",
    width="100%",
    padding="0.75rem 1.5rem",
)


__all__ = [
    "black",
    "white",
    "elevated_card",
    "topheader",
]
