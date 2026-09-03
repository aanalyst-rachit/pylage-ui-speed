# UI Kit Form

## Overview

`form()` is the public PyLage UI Kit wrapper around the existing engine `Form` component.

Form provides semantic HTML form composition, native form attributes, and submit-event integration without introducing a duplicate renderer or runtime.

## Public API

```python
import pylage as pl

def handle_submit(payload):
    print(payload)

pl.form(
    pl.form_field(
        pl.input(name="email"),
        label="Email",
        required=True,
    ),
    pl.button("Submit", type="submit"),
    on_submit=handle_submit,
)
```

## Architecture

The implementation follows the existing PyLage architecture:

```text
pl.form()
   ↓
UI Kit form wrapper
   ↓
ENGINE Form
   ↓
Component("Form")
   ↓
Existing renderer + client runtime
```

No new renderer, WebSocket layer, reactive engine, or duplicate form implementation is introduced.

## Children

Forms accept normal PyLage children, including existing controls and composition components such as `form_field()`, `input()`, `textarea()`, `select()`, and `button()`.

## Form Attributes

Native form properties such as `method` and `action` are forwarded to the rendered `<form>` element.

```python
pl.form(
    pl.input(name="email"),
    method="post",
    action="/submit",
)
```

## Submit Events

`on_submit` is dispatched through the existing PyLage client runtime.

The browser submit handler prevents the native page navigation, collects submitted controls through `FormData`, and sends the resulting values through the existing PyLage event protocol.

The resulting payload has the established structure:

```python
{
    "values": {
        "email": "user@example.com",
    }
}
```

## FormField Composition

Form and FormField have separate responsibilities:

```text
Form
├── FormField
│   ├── Label
│   ├── Control
│   ├── Help text
│   └── Error
├── Other controls
└── Submit action
```

FormField handles field-level presentation; Form handles form composition and submission.

## Verification

- Existing Form component tests pass.
- Public Form wrapper tests pass.
- Browser verification confirms form rendering, input interaction, and submit payload behavior.
- Full manual suite passes.
- Full project test suite passes.

## Status

Phase 08 Form is complete.
