# PyLage UI Kit — Confirmation Dialog

## Purpose

The UI Kit Confirmation Dialog provides a reusable confirmation-flow recipe for actions that require explicit user approval or cancellation.

## Architecture

Confirmation Dialog is implemented as a COMPOSE recipe. It does not introduce a new dialog component, renderer, reactive engine, event system, or JavaScript behavior.

The recipe composes the existing UI Kit Dialog, Button, and Row APIs.

## API

```python
from pylage.UI import confirmation_dialog

confirmation_dialog(
    Text("Delete this item?"),
    title=Text("Delete Item"),
    open=dialog_open,
    on_confirm=delete_item,
    on_cancel=cancel_action,
    confirm_text="Delete",
    cancel_text="Cancel",
    confirm_variant="danger",
)
```

The recipe supports:

- message content
- optional title
- reactive open state
- confirm and cancel callbacks
- customizable button labels
- configurable confirm button variant
- custom dialog style
- additional Dialog properties

## Callback Handling

Callbacks are forwarded to the underlying Button only when they are provided.

This preserves the existing PyLage event contract, where event handlers must be callable. Missing callbacks are omitted rather than passing `None` as an event handler.

## Existing Core Contract

The underlying PyLage Dialog remains the source of truth for dialog rendering and reactive open behavior.

No core Dialog or Button implementation was duplicated or modified.

## Regression Coverage

Coverage includes:

- Dialog composition
- message and action rendering
- optional title
- reactive open state
- confirm callback forwarding
- cancel callback forwarding
- danger confirm variant
- custom style support
- public recipe export

Focused verification completed with **8 tests passed**.

## Manual Verification

`app/ui_kit_confirmation_dialog_manual.py` was added to verify the recipe through the normal PyLage application runtime.

Manual browser verification confirmed:

- dialog is initially hidden
- dialog opens reactively
- Cancel closes the dialog
- Confirm closes the dialog
- action status updates correctly
- danger confirmation styling renders correctly

## Design Boundary

The UI Kit intentionally provides a reusable confirmation-flow composition rather than creating a second dialog system.

Existing PyLage Dialog, Button, Row, state, event, and rendering behavior remain the source of truth.

## Phase Status

Confirmation Dialog is complete as a Phase 09 Feedback & Overlays item.

Phase 09 remains incomplete until all Phase 09 items are finished. Toast remains unresolved/on hold unless explicitly requested.

## Workflow

reuse/create/------>manual create-------> manual verify----> documentation-----> tracker update---git checkpoint

rules - PYTHON TERMINAL RULE + MD FILE RULE
