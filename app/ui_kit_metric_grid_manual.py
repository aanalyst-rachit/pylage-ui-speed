import pylage as ps
import pylage as ui
from pylage import Column, Style

def get_app():
    return Column(
        ps.Heading("PyLage UI Kit — Metric Grid", level=2),
        ps.Text("High-level metric grid for responsive KPI rows."),
        ui.metric_grid(
            ui.metric(label="Total MRR", value="$248.5K", delta="+14.2%"),
            ui.metric(label="Net Retention", value="112%", delta="+3.1%"),
            ui.metric(label="Active Seats", value="18,400", delta="+850"),
            columns=3,
        ),
        gap="1.5rem",
        style=Style(max_width="1200px", margin="0 auto", padding="2rem"),
    )
