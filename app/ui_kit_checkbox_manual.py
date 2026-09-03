from pylage.ENGINE import Column, Heading, Row, State, Style, Text
import pylage as ps



def get_app():
    terms = State(False)
    notifications = State(True)
    custom_checked = State(False)
    status = State("Not changed yet")

    def handle_custom_change(payload):
        checked = payload.get("checked", False) if isinstance(payload, dict) else bool(payload)
        custom_checked.set(checked)
        status.set(f"Custom handler: {checked}")

    basic_checkbox = ps.checkbox(
        name="terms-basic",
        checked=False,
        title="Basic checkbox",
    )

    state_checkbox = ps.checkbox(
        name="terms-state",
        checked=terms,
        on_change=lambda payload: terms.set(
            payload.get("checked", False) if isinstance(payload, dict) else bool(payload)
        ),
    )

    custom_checkbox = ps.checkbox(
        name="custom",
        checked=custom_checked,
        on_change=handle_custom_change,
        title="Custom change handler",
    )

    checked_checkbox = ps.checkbox(
        name="prechecked",
        checked=True,
    )

    disabled_checkbox = ps.checkbox(
        name="disabled",
        checked=True,
        disabled=True,
        title="Disabled checkbox",
    )

    styled_checkbox = ps.checkbox(
        name="styled",
        checked=False,
        style=Style(
            width="1.25rem",
            height="1.25rem",
            cursor="pointer",
        ),
    )

    return Column(
        Heading(
            "PyLage UI Kit — Checkbox",
            style=Style(
                font_size="1.75rem",
                font_weight="700",
                margin_bottom="0.5rem",
            ),
        ),
        Text(
            "Interactive checkbox using the existing PyLage engine capability.",
            style=Style(margin_bottom="1.5rem"),
        ),

        Text("Basic Checkbox", style=Style(font_weight="700", margin_top="1rem")),
        Row(
            basic_checkbox,
            Text("Accept terms"),
            style=Style(align_items="center", gap="0.5rem"),
        ),

        Text("State-Bound Checkbox", style=Style(font_weight="700", margin_top="1rem")),
        Row(
            state_checkbox,
            Text("Enable terms agreement"),
            style=Style(align_items="center", gap="0.5rem"),
        ),
        Text(terms),

        Text("Custom on_change Handler", style=Style(font_weight="700", margin_top="1rem")),
        Row(
            custom_checkbox,
            Text("Use custom event handler"),
            style=Style(align_items="center", gap="0.5rem"),
        ),
        Text(status),

        Text("Pre-Checked Checkbox", style=Style(font_weight="700", margin_top="1rem")),
        Row(
            checked_checkbox,
            Text("Already checked"),
            style=Style(align_items="center", gap="0.5rem"),
        ),

        Text("Disabled Checkbox", style=Style(font_weight="700", margin_top="1rem")),
        Row(
            disabled_checkbox,
            Text("Disabled and checked"),
            style=Style(align_items="center", gap="0.5rem"),
        ),

        Text("Styled Checkbox", style=Style(font_weight="700", margin_top="1rem")),
        Row(
            styled_checkbox,
            Text("Custom dimensions and cursor"),
            style=Style(align_items="center", gap="0.5rem"),
        ),

        style=Style(
            width="100%",
            max_width="700px",
            padding="2rem",
            box_sizing="border-box",
        ),
    )

