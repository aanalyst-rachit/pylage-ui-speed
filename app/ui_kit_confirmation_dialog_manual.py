import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
from pylage.ENGINE import Column, State, Style, Heading, Text
from pylage.UI import button, card, confirmation_dialog, row


def get_app():
    dialog_open = State(False)
    action_log = State("No confirmation action taken yet.")

    def open_dialog(e=None):
        dialog_open.set(True)
        action_log.set("Confirmation dialog opened.")

    def confirm_action(e=None):
        dialog_open.set(False)
        action_log.set("Action confirmed and dialog closed.")

    def cancel_action(e=None):
        dialog_open.set(False)
        action_log.set("Action cancelled and dialog closed.")

    confirmation = confirmation_dialog(
        Text("Are you sure you want to deploy the updated PyLage components to production?"),
        title=Heading("Confirm System Deployment", level=3),
        open=dialog_open,
        on_confirm=confirm_action,
        on_cancel=cancel_action,
        confirm_text="Confirm & Deploy",
        cancel_text="Cancel",
        confirm_variant="danger",
        class_name="pylage-confirmation-dialog",
    )

    app = Column(
        Heading("Confirmation Dialog — UI Kit Manual Test", level=1),
        Text("Test reactive open state, cancel/confirm callbacks, action buttons, and danger variant."),
        card(
            row(
                Text("Status: ", style=Style(font_weight="bold")),
                Text(action_log, style=Style(font_weight="bold")),
                style=Style(display="flex", align_items="center", gap="0.5rem"),
            ),
            style=Style(padding="1rem", margin_bottom="1.5rem"),
        ),
        button("Open Confirmation Dialog", on_click=open_dialog, variant="primary"),
        confirmation,
        style=Style(padding="2rem", gap="1.5rem", font_family="system-ui, sans-serif"),
    )

    return app


if __name__ == "__main__":
    app = get_app()
    ps.run(app, title="PyLage UI Kit Confirmation Dialog Manual", serve=True, host="0.0.0.0", port=3000)
