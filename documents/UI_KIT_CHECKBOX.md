# UI Kit Checkbox

## Overview

`checkbox()` is the public PyLage UI Kit wrapper for the existing engine `Checkbox` component.
It reuses the existing renderer, registry, event system, and State reactivity without duplicating engine behavior.

## API

```python
from pylage.UI.components import checkbox
```

### Basic usage

```python
checkbox(checked=True)
```

### State binding

```python
from pylage.ENGINE import State

checked = State(False)
checkbox(checked=checked)
```

The existing Checkbox engine supports State-backed `checked` values and propagates Python-side State changes to the browser DOM.

## Supported behavior

- Unchecked checkbox
- Pre-checked checkbox
- State-bound checked state
- Custom `on_change` handler
- Disabled checkbox
- Native checkbox properties such as `name`, `title`, and other registered attributes
- Custom styling through `Style`
- Browser `change` event integration

## Architecture

The UI Kit wrapper delegates directly to the existing engine implementation:

```text
pylage.UI.components.checkbox
        ↓
pylage.ENGINE.Checkbox
        ↓
PyLage registry / renderer / runtime
        ↓
Browser checkbox
```

No new renderer, runtime protocol, registry implementation, or duplicated checkbox engine was introduced.

## Verification

### Automated tests

```text
18 passed in 3.14s
```

Covered suites:

- `test/test_b2_checkbox_api.py`
- `test/test_checkbox_component.py`
- `test/test_public_phase08_wrappers.py`

### Manual browser verification

Project-wide manual runner completed successfully:

```text
1 passed in 56.38s
```

Dedicated manual application: `app/ui_kit_checkbox_manual.py`

Manual coverage includes basic, State-bound, custom event, pre-checked, disabled, and styled checkbox cases.


