# UI Kit DatePicker

## Overview

PyLage UI Kit `datepicker()` provides a public Python-first wrapper around the existing PyLage DatePicker engine component.

It renders as a native HTML5 date input and supports reactive `State` binding, input events, date constraints, disabled state, and native input properties.

## Public API

```python
import pylage as pl

selected_date = pl.State("2026-09-03")

pl.datepicker(
    value=selected_date,
    min="2026-01-01",
    max="2026-12-31",
)
```

## Supported Behavior

- Native HTML5 `input[type="date"]` rendering
- Static date values
- `pl.State` reactive value binding
- Browser `input` event → State synchronization
- Custom `on_input` callback preservation
- Custom `on_change` callbacks
- `min` and `max` date constraints
- `disabled` state
- Native properties such as `name`, `id`, and `title`
- Programmatic State updates reflected by the component

## Architecture

The UI Kit wrapper reuses the existing engine implementation:

`User Application → pylage-ui-kit datepicker() → ENGINE DatePicker → existing renderer/runtime`

No separate renderer, WebSocket path, or browser implementation was introduced.

## Reactive Binding

When `value` is a `pl.State`, the DatePicker engine synchronizes browser input events back into that State. A user-provided `on_input` callback is preserved and receives the same event payload.

## Verification

Automated coverage:

- `test/test_datepicker_component.py`
- `test/test_public_phase08_wrappers.py`
- `test/test_datepicker_browser.py`
- Result: 17 passed

Manual coverage:

- Basic DatePicker
- State-bound DatePicker
- Custom input event
- Programmatic State update
- Disabled DatePicker
- Native date properties
- Browser verification: passed

## Phase 08 Status

DatePicker is complete for Phase 08 Forms.
