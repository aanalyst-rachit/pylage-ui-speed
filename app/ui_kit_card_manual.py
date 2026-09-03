import pylage as ps
import pylage as ui
from pylage.ENGINE import Column, Grid, Heading, State, Style, Text

def get_app():
    click_count = State(0)

    def mark_clicked():
        click_count.set(click_count.value + 1)

    return Column(
        Heading("PyLage UI Kit — Card", level=2),
        Text("Semantic Card API using the existing PyLage engine."),
        
        # Grid div par direct inline grid styles pass karein
        Grid(
            ui.card(
                heading="Revenue",
                body="₹42,000",
                footer="Monthly revenue",
            ),
            ui.card(
                heading="Active Users",
                body="12,450",
                footer="Growing steadily",
                variant="elevated",
            ),
            ui.card(
                heading="Orders",
                body="1,284",
                footer="Updated just now",
                variant="outlined",
            ),
            ui.card(
                heading="Interactive Card",
                body="Click to test state update",
                footer=click_count,
                variant="interactive",
                on_click=mark_clicked,
            ),
            style=Style(
                display="grid",
                grid_template_columns="repeat(auto-fit, minmax(280px, 1fr))",
                gap="1.5rem",
                width="100%"
            )
        ),
        gap="1.5rem",
        style=Style(max_width="1200px", margin="0 auto", padding="2rem")
    )