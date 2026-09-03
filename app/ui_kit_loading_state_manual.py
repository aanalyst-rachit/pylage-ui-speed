import pylage as ps
import pylage as ui
from pylage import Column, Grid, Style

def get_app():
    return Column(
        ps.Heading("PyLage UI Kit — Loading State", level=2),
        ps.Text("High-level feedback spinners and loaders for async workflows."),
        Grid(
            ui.loading_state(
                text="Loading dashboard...",
                description="Fetching latest analytics from the cluster.",
            ),
            ui.loading_state(
                text="Importing dataset",
                description="Parsing CSV and computing summary metrics.",
            ),
            ui.loading_state(
                text="Synchronizing state",
                spinner=True,
            ),
            style=Style(
                display="grid",
                grid_template_columns="repeat(auto-fit, minmax(300px, 1fr))",
                gap="1.5rem",
                width="100%",
            ),
        ),
        gap="1.5rem",
        style=Style(max_width="1200px", margin="0 auto", padding="2rem"),
    )
