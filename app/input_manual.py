import sys
from pathlib import Path

from pylage.ENGINE import Button, Column, Heading, Input, State, Text
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
from pylage.ENGINE import Style

def get_app():
    name_state = State("Aapka Naam Here")
    submitted_state = State("Form abhi submit nahi hua hai.")

    # Fixed: Extract string value if payload is a dict
    def on_name_change(val):
        if isinstance(val, dict):
            text_value = val.get("value", "")
        else:
            text_value = str(val) if val is not None else ""

        name_state.set(text_value if text_value else "Aapka Naam Here")

    def handle_submit():
        # Fixed: Read clean .value string
        current = name_state.value
        if isinstance(current, dict):
            current = current.get("value", "")

        submitted_state.set(f"🎉 Submitted Name: {current}")

    name_input = Input(
        placeholder="Apna naam type karein...",
        on_change=on_name_change,
        style=Style(
            padding="0.75rem 1rem",
            font_size="1rem",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            width="100%",
            box_sizing="border-box",
            margin_bottom="1rem",
        ),
    )

    submit_btn = Button(
        "Submit Form",
        on_click=handle_submit,
        style=Style(
            background_color="#2563eb",
            color="#ffffff",
            padding="0.75rem 1.5rem",
            font_size="1rem",
            font_weight="700",
            border_radius="0.5rem",
            cursor="pointer",
        ),
    )

    return Column(
        Heading(
            "PyLage Input — Live Manual",
            style=Style(
                font_size="1.75rem",
                font_weight="700",
                color="#0f172a",
                margin_bottom="0.5rem",
            ),
        ),
        Text(
            "Niche diye gaye input field me type karke live reactivity test karein:",
            style=Style(color="#64748b", margin_bottom="1.5rem"),
        ),

        name_input,

        Text("Live Preview:", style=Style(font_weight="700", margin_top="1rem")),
        Heading(
            name_state,
            style=Style(
                color="#2563eb",
                font_size="1.25rem",
                margin_bottom="1.5rem",
            ),
        ),

        submit_btn,
        Text(
            submitted_state,
            style=Style(
                color="#166534",
                font_weight="600",
                margin_top="1rem",
            ),
        ),

        style=Style(
            width="100%",
            max_width="600px",
            min_height="100vh",
            padding="2rem",
            background_color="#f8fafc",
            box_sizing="border-box",
        ),
    )
