import pylage as ps
from pylage.ENGINE import Column, Heading, State, Style, Text, Button, Row
from pylage.UI.recipes import modal


def get_app():
    modal_open = State(False)
    action_log = State("No modal action taken yet.")

    def open_modal(e=None):
        modal_open.set(True)
        action_log.set("Modal opened by user.")

    def confirm_action(e=None):
        modal_open.set(False)
        action_log.set("Modal confirmed & closed.")

    def cancel_action(e=None):
        modal_open.set(False)
        action_log.set("Modal cancelled & closed.")

    modal_content = Column(
        Text("Are you sure you want to deploy the updated PyLage components to production?"),
        Row(
            Button("Cancel", on_click=cancel_action, variant="secondary"),
            Button("Confirm & Deploy", on_click=confirm_action, variant="primary"),
            style=Style(
                display="flex",
                justify_content="flex-end",
                gap="0.75rem",
                margin_top="1.5rem",
            ),
        ),
        gap="0.75rem",
    )

    deployment_modal = modal(
        modal_content,
        open=modal_open,
        title="Confirm System Deployment",
        class_name="pylage-ui-kit-modal",
    )

    return Column(
        Heading("PyLage UI Kit — Modal", level=2),
        Text("Reusable Modal recipe composed from the existing UI Kit Dialog and Card components."),
        Column(
            Text("Modal Status:", style=Style(font_weight="bold")),
            Text(action_log, style=Style(font_weight="bold")),
            gap="0.5rem",
            style=Style(
                padding="1rem",
                background_color="#f8fafc",
                border_radius="8px",
            ),
        ),
        Button("Open Modal", on_click=open_modal, variant="primary"),
        deployment_modal,
        gap="1.5rem",
        style=Style(
            max_width="1200px",
            margin="0 auto",
            padding="2rem",
        ),
    )


if __name__ == "__main__":
    ps.run(
        get_app(),
        title="PyLage Modal Manual",
        serve=True,
        host="0.0.0.0",
        port=3000,
    )
