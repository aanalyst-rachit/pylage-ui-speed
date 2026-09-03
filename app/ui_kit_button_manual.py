import sys
from pathlib import Path

# Ensure local pylage import
from pylage.ENGINE import Column, Heading, Text
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
import pylage as ui
from pylage.ENGINE import Style


def get_app():
    return Column(
        Heading(
            "PyLage UI Kit — Button",
            level=2,
        ),
        Text(
            "Semantic Button API using the existing PyLage engine."
        ),
        ui.button("Primary"),
        ui.button("Secondary", variant="secondary"),
        ui.button("Outline", variant="outline"),
        ui.button("Ghost", variant="ghost"),
        ui.button("Danger", variant="danger"),
        ui.button("Small", size="sm"),
        ui.button("Medium", size="md"),
        ui.button("Large", size="lg"),
        ui.button(
            "Disabled",
            disabled=True,
            style=Style(opacity="0.6"),
        ),
    )
