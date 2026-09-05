import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
from pylage.ENGINE import Heading, State, Style, Text
from pylage.UI import button, card, loading_overlay
from pylage.UI.layout import column


def get_app():
    loading = State(False)
    status = State("Overlay is hidden.")

    def toggle_loading(e=None):
        print("CLICK RECEIVED:", e)
        print("LOADING BEFORE:", loading.value)
        next_value = not loading.value
        loading.set(next_value)
        status.set("Loading overlay is visible." if next_value else "Overlay is hidden.")
        print("LOADING AFTER:", loading.value)
        print("STATUS AFTER:", status.value)

    content = column(
        Heading("Loading Overlay Manual Test", level=2),
        Text("This page verifies the UI Kit loading_overlay() recipe."),
        Text(status, style=Style(font_weight="bold")),
        button(
            "Start / Stop Loading",
            on_click=toggle_loading,
            variant="primary",
        ),
        Text("Click the button to show the full-viewport loading overlay. Click again to hide it."),
        style=Style(
            display="flex",
            flex_direction="column",
            gap="1rem",
            padding="2rem",
            min_height="400px",
        ),
    )

    overlay = loading_overlay(
        "Please wait...",
        open=loading,
        spinner=True,
        title="Loading overlay",
    )

    app = column(
        content,
        card(
            Text("Underlying page content remains mounted while the overlay is toggled."),
            style=Style(padding="1.5rem", margin_top="1rem"),
        ),
        overlay,
        style=Style(
            display="flex",
            flex_direction="column",
            gap="1.5rem",
            padding="2rem",
            font_family="system-ui, sans-serif",
        ),
    )

    return app


if __name__ == "__main__":
    app = get_app()
    ps.run(app, title="PyLage UI Kit Loading Overlay Manual", serve=True, host="0.0.0.0", port=3000)
