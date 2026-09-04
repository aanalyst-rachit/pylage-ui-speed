import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
from pylage.ENGINE import Column, Heading, Text, Button
from pylage.UI.recipes import tooltip


def get_app():
    return Column(
        Heading("PyLage UI Kit — Tooltip", level=1),
        Text("UI Kit Tooltip wrapper using the existing PyLage Tooltip component."),
        Heading("1. Button Tooltip", level=3),
        tooltip(
            Button("Hover target"),
            title="Helpful information",
            class_name="ui-kit-tooltip",
        ),
        Heading("2. Text Tooltip", level=3),
        tooltip(
            Text("Hover over this information target"),
            title="This is a second tooltip",
        ),
    )


if __name__ == "__main__":
    app = get_app()
    ps.run(app, title="PyLage UI Kit - Tooltip Manual Test", serve=True, host="0.0.0.0", port=3000)
