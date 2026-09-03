import pylage as ps
from pylage.ENGINE import Column, Row

def get_app():
    return Column(
        ps.heading("Badge"),
        ps.text("Semantic status and category badges."),
        # Row me wraps karke align-items start karein
        Row(
            ps.badge("Default"),
            ps.badge("Primary", variant="primary"),
            ps.badge("Secondary", variant="secondary"),
            ps.badge("Success", variant="success"),
            ps.badge("Warning", variant="warning"),
            ps.badge("Danger", variant="danger"),
            ps.badge("Info", variant="info"),
            gap="0.5rem",
            wrap=True
        ),
        gap="1rem"
    )