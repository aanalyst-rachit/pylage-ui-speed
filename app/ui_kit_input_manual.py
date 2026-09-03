import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
from pylage.ENGINE import Button, Column, Heading, State, Style, Text
from pylage.UI.components import input


def get_app():
    name_state = State("Aapka Naam Here")
    submitted_state = State("Form abhi submit nahi hua hai.")

    def handle_name_input(payload):
        if isinstance(payload, dict):
            value = payload.get("value", "")
        else:
            value = "" if payload is None else str(payload)

        name_state.set(value if value else "Aapka Naam Here")

    def handle_submit():
        current = name_state.value
        if isinstance(current, dict):
            current = current.get("value", "")
        submitted_state.set(f"Submitted Name: {current}")

    name_input = input(
        placeholder="Apna naam type karein...",
        on_input=handle_name_input,
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

    email_input = input(
        input_type="email",
        placeholder="Email address",
        name="email",
        required=True,
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

    password_input = input(
        input_type="password",
        placeholder="Password",
        name="password",
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

    disabled_input = input(
        value="Disabled input",
        disabled=True,
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

    submit_button = Button(
        "Submit Form",
        on_click=handle_submit,
        style=Style(
            padding="0.75rem 1.5rem",
            font_size="1rem",
            font_weight="700",
            border_radius="0.5rem",
            cursor="pointer",
        ),
    )

    return Column(
        Heading(
            "PyLage UI Kit — Input Manual",
            style=Style(
                font_size="1.75rem",
                font_weight="700",
                margin_bottom="0.5rem",
            ),
        ),
        Text(
            "Manual verification: text, email, password, disabled and reactive input.",
            style=Style(
                margin_bottom="1.5rem",
            ),
        ),

        Text("Text Input", style=Style(font_weight="700")),
        name_input,

        Text(
            "Live Preview:",
            style=Style(
                font_weight="700",
                margin_top="1rem",
            ),
        ),
        Heading(
            name_state,
            style=Style(
                font_size="1.25rem",
                margin_bottom="1.5rem",
            ),
        ),

        Text("Email Input", style=Style(font_weight="700")),
        email_input,

        Text("Password Input", style=Style(font_weight="700")),
        password_input,

        Text("Disabled Input", style=Style(font_weight="700")),
        disabled_input,

        submit_button,

        Text(
            submitted_state,
            style=Style(
                font_weight="600",
                margin_top="1rem",
            ),
        ),

        style=Style(
            width="100%",
            max_width="600px",
            min_height="100vh",
            padding="2rem",
            box_sizing="border-box",
        ),
    )


if __name__ == "__main__":
    ps.run(get_app())
