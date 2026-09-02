import sys
from pathlib import Path

# Ensure local pylage import
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
import pylage_ui as ui
from pylage import Style


def get_app():
    click_count = ps.State(0)

    def mark_clicked():
        click_count.set(click_count.value + 1)

    return ps.Column(
        ps.Heading(
            "PyLage UI Kit — Card",
            level=2,
        ),
        ps.Text(
            "Semantic Card API using the existing PyLage engine."
        ),

        ps.Heading("Default", level=3),
        ui.card(
            heading="Revenue",
            body="₹42,000",
            footer="Monthly revenue",
        ),

        ps.Heading("Elevated", level=3),
        ui.card(
            heading="Active Users",
            body="12,450",
            footer="Growing steadily",
            variant="elevated",
        ),

        ps.Heading("Outlined", level=3),
        ui.card(
            heading="Orders",
            body="1,284 orders this month",
            footer="Updated just now",
            variant="outlined",
        ),

        ps.Heading("Interactive", level=3),
        ui.card(
            heading="Interactive Card — Click Me",
            body="Click this card to test the UI Kit interaction.",
            footer=click_count,
            variant="interactive",
            on_click=mark_clicked,
        ),

        ps.Heading("Advanced Composition", level=3),
        ui.card(
            ps.Column(
                ps.Heading("Custom Header", level=4),
                ps.Text("Custom body content"),
                ps.Text("Custom footer content"),
            ),
            style=Style(
                background_color="#f8fafc",
            ),
        ),
    )
