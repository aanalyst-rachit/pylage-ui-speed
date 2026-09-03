import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
from pylage.ENGINE import State, Style, Column, Heading, Text, Card, Row
from pylage.UI.components.textarea import textarea


def get_app():
    # Reactive state used to verify real browser input binding.
    message = State("")
    input_count = State(0)
    custom_value = State("")

    def handle_custom_input(payload=None):
        if isinstance(payload, dict) and "value" in payload:
            custom_value.set(payload["value"])

    basic = textarea(
        "",
        placeholder="Type something here...",
        rows=5,
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

    state_bound = textarea(
        message,
        placeholder="Type to update the reactive state...",
        rows=5,
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #2563eb",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

    custom_handler = textarea(
        "",
        placeholder="Custom on_input handler...",
        rows=4,
        on_input=handle_custom_input,
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #7c3aed",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

    disabled = textarea(
        "This textarea is disabled.",
        rows=3,
        disabled=True,
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            background_color="#f1f5f9",
            box_sizing="border-box",
        ),
    )

    configured = textarea(
        "Textarea with configured attributes.",
        placeholder="Configured placeholder",
        name="manual-notes",
        rows=4,
        cols=40,
        required=True,
        minlength=3,
        maxlength=500,
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #94a3b8",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

    return Column(
        Heading(
            "PyLage Textarea — Live Manual",
            level=1,
            style=Style(
                font_size="1.75rem",
                font_weight="700",
                margin_bottom="0.5rem",
            ),
        ),
        Text(
            "Manual verification of textarea rendering, attributes, disabled state, "
            "State binding, and custom input handling.",
            style=Style(
                color="#64748b",
                margin_bottom="1.5rem",
            ),
        ),

        Card(
            Heading("1. Basic Textarea", level=3),
            Text(
                "Verify that the textarea renders as a native multi-line input "
                "with placeholder and configurable rows.",
                style=Style(color="#64748b", margin_bottom="0.75rem"),
            ),
            basic,
            style=Style(
                padding="1.25rem",
                margin_bottom="1rem",
                border="1px solid #e2e8f0",
                border_radius="0.75rem",
            ),
        ),

        Card(
            Heading("2. State-Bound Textarea", level=3),
            Text(
                "Type into the textarea and verify that the reactive state below updates.",
                style=Style(color="#64748b", margin_bottom="0.75rem"),
            ),
            state_bound,
            Row(
                Text(
                    "Reactive value: ",
                    style=Style(font_weight="700"),
                ),
                Text(
                    message,
                    style=Style(
                        color="#2563eb",
                        font_weight="700",
                        white_space="pre-wrap",
                    ),
                ),
                style=Style(
                    display="flex",
                    align_items="flex-start",
                    gap="0.5rem",
                    margin_top="0.75rem",
                ),
            ),
            style=Style(
                padding="1.25rem",
                margin_bottom="1rem",
                border="1px solid #bfdbfe",
                border_radius="0.75rem",
                background_color="#eff6ff",
            ),
        ),

        Card(
            Heading("3. Custom Input Handler", level=3),
            Text(
                "Verify that an explicitly supplied on_input handler is preserved.",
                style=Style(color="#64748b", margin_bottom="0.75rem"),
            ),
            custom_handler,
            Row(
                Text(
                    "Custom handler value: ",
                    style=Style(font_weight="700"),
                ),
                Text(
                    custom_value,
                    style=Style(
                        color="#7c3aed",
                        font_weight="700",
                        white_space="pre-wrap",
                    ),
                ),
                style=Style(
                    display="flex",
                    align_items="flex-start",
                    gap="0.5rem",
                    margin_top="0.75rem",
                ),
            ),
            style=Style(
                padding="1.25rem",
                margin_bottom="1rem",
                border="1px solid #ddd6fe",
                border_radius="0.75rem",
                background_color="#f5f3ff",
            ),
        ),

        Card(
            Heading("4. Disabled Textarea", level=3),
            Text(
                "Verify that disabled=True prevents editing.",
                style=Style(color="#64748b", margin_bottom="0.75rem"),
            ),
            disabled,
            style=Style(
                padding="1.25rem",
                margin_bottom="1rem",
                border="1px solid #e2e8f0",
                border_radius="0.75rem",
            ),
        ),

        Card(
            Heading("5. Native Textarea Attributes", level=3),
            Text(
                "Verify name, rows, cols, required, minlength, maxlength, "
                "and placeholder attributes.",
                style=Style(color="#64748b", margin_bottom="0.75rem"),
            ),
            configured,
            style=Style(
                padding="1.25rem",
                margin_bottom="1rem",
                border="1px solid #e2e8f0",
                border_radius="0.75rem",
            ),
        ),

        style=Style(
            width="100%",
            max_width="800px",
            min_height="100vh",
            padding="2rem",
            margin="0 auto",
            background_color="#f8fafc",
            box_sizing="border-box",
            font_family="system-ui, sans-serif",
        ),
    )


if __name__ == "__main__":
    app = get_app()
    ps.run(
        app,
        title="PyLage Textarea Manual Test",
        serve=True,
        host="0.0.0.0",
        port=3000,
    )
