from pylage import Column, Style, Text
from pylage_ui import table


def get_app():
    users = [
        {"Name": "Rachit", "Role": "Admin", "Status": "Active", "Revenue": "₹42,000"},
        {"Name": "Rahul", "Role": "Developer", "Status": "Active", "Revenue": "₹35,500"},
        {"Name": "Priya", "Role": "Designer", "Status": "Pending", "Revenue": "₹28,750"},
        {"Name": "Aman", "Role": "Manager", "Status": "Active", "Revenue": "₹31,200"},
    ]

    return Column(
        Text(
            "Table",
            style=Style(
                font_size="2rem",
                font_weight="700",
                color="#0f172a",
                font_family="Inter, sans-serif",
            ),
        ),
        Text(
            "DataFrame-friendly semantic tables through the PyLage UI Kit.",
            style=Style(
                color="#64748b",
                margin_bottom="1.5rem",
                font_family="Inter, sans-serif",
            ),
        ),
        table(
            users,
            title="Users",
            class_name="users-table",
        ),
        Text(
            "The same component accepts record dictionaries, headers + rows, and DataFrame-like objects.",
            style=Style(
                color="#64748b",
                margin_top="1rem",
                font_size="0.875rem",
                font_family="Inter, sans-serif",
            ),
        ),
        style=Style(
            padding="2rem",
            max_width="1100px",
            margin="0 auto",
            font_family="Inter, sans-serif",
            display="flex",
            flex_direction="column",
            gap="1rem",
        ),
    )
