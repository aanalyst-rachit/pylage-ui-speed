import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
from pylage.ENGINE import Column, Heading, Text, Button, Card
from pylage.UI.recipes import popover


def get_app():
    return Column(
        Heading("PyLage UI Kit — Popover", level=1),
        Text("UI Kit Popover wrapper using the existing PyLage Popover component."),
        Heading("1. Basic Popover", level=3),
        popover(
            Text("This is popover content."),
            title="Additional information",
            class_name="ui-kit-popover",
        ),
        Heading("2. Popover with Multiple Children", level=3),
        popover(
            Card(
                Text("Popover details"),
                Button("Close"),
            ),
            title="Quick information",
        ),
        Heading("3. Props + Children", level=3),
        popover(
            Text("Props and children are preserved by the UI Kit wrapper."),
            class_name="ui-kit-popover-demo",
            title="UI Kit Popover",
        ),
    )


if __name__ == "__main__":
    app = get_app()
    ps.run(app, title="PyLage UI Kit - Popover Manual Test", serve=True, host="0.0.0.0", port=3000)
