import pylage as ps
import pylage as ui
from pylage.ENGINE import Column, Heading, Style, Text

def get_app():
    return Column(
        Heading("PyLage UI Kit — Dashboard Card", level=2),
        Text("High-level dashboard cards with action and footer slots."),
        ui.dashboard_grid(
            ui.dashboard_card(
                title="Active Users",
                body="3,420 active right now across North America and Europe.",
                action=ui.badge("Live", variant="success"),
                footer="Refreshed every 30s",
            ),
            ui.dashboard_card(
                title="Error Budget",
                body="99.98% availability remaining this calendar month.",
                action=ui.button("Policy", variant="ghost"),
                footer="SLA: 99.9%",
            ),
            layout="2-col",
        ),
        gap="1.5rem",
        style=Style(max_width="1200px", margin="0 auto", padding="2rem"),
    )
