from pylage.ENGINE import Column, Heading, Option, State, Style, Text
import pylage as ps


def get_app():
    selected_language = State("python")
    selected_country = State("india")
    custom_status = State("Custom handler not triggered yet.")

    def handle_country_change(payload):
        if isinstance(payload, dict):
            value = payload.get("value", "")
        else:
            value = str(payload)

        custom_status.set(f"Selected country: {value}")

    basic_select = ps.select(
        Option("Python", value="python"),
        Option("JavaScript", value="javascript"),
        Option("Rust", value="rust"),
        value="python",
        name="language",
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

    state_select = ps.select(
        Option("Python", value="python"),
        Option("JavaScript", value="javascript"),
        Option("Rust", value="rust"),
        value=selected_language,
        name="state-language",
        on_change=lambda payload: selected_language.set(
            payload.get("value", "") if isinstance(payload, dict) else str(payload)
        ),
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

    custom_select = ps.select(
        Option("India", value="india"),
        Option("Japan", value="japan"),
        Option("Nepal", value="nepal"),
        value=selected_country,
        name="country",
        on_change=handle_country_change,
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

    disabled_select = ps.select(
        Option("Locked option", value="locked"),
        value="locked",
        disabled=True,
        name="disabled-select",
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

    multiple_select = ps.select(
        Option("Python", value="python"),
        Option("JavaScript", value="javascript"),
        Option("Rust", value="rust"),
        Option("Go", value="go"),
        multiple=True,
        size=4,
        name="multiple-languages",
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

    return Column(
        Heading(
            "PyLage UI Kit — Select",
            style=Style(
                font_size="1.75rem",
                font_weight="700",
                margin_bottom="0.5rem",
            ),
        ),

        Text(
            "Basic Select",
            style=Style(font_weight="700", margin_top="1rem"),
        ),
        basic_select,

        Text(
            "State-Bound Select",
            style=Style(font_weight="700", margin_top="1rem"),
        ),
        state_select,
        Text(selected_language),

        Text(
            "Custom on_change Handler",
            style=Style(font_weight="700", margin_top="1rem"),
        ),
        custom_select,
        Text(custom_status),

        Text(
            "Disabled Select",
            style=Style(font_weight="700", margin_top="1rem"),
        ),
        disabled_select,

        Text(
            "Multiple Select",
            style=Style(font_weight="700", margin_top="1rem"),
        ),
        multiple_select,

        style=Style(
            width="100%",
            max_width="700px",
            padding="2rem",
            box_sizing="border-box",
        ),
    )
