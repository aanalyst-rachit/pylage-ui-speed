# UI Kit FormField

## Overview

`form_field()` is a semantic composition helper for wrapping an existing PyLage UI control with field-level presentation.

## Public API

```python
import pylage as pl

pl.form_field(
    pl.input(value="user@example.com"),
    label="Email",
    help_text="Use your work email.",
    error="Email is required.",
    required=True,
)
```

## Composition

A FormField is composed from existing PyLage components and does not introduce a new renderer or input implementation.

The composition is:

- Label
- Existing control
- Optional help text
- Optional error presentation
- Optional required marker

## Supported Controls

FormField can wrap existing controls such as Input, Textarea, and Select.

## Required Fields

When `required=True`, the field label is presented with a required marker.

## Help and Error Presentation

`help_text` provides supporting field information and `error` provides an error message.
FormField presents these values but does not perform validation itself. Validation logic belongs to the validation/error-state layer.

## State and Events

FormField preserves the wrapped control and its existing event behavior. State binding remains the responsibility of the underlying control.

## Architecture Decision

FormField is intentionally a composition component. It does not duplicate the renderer, reactive engine, or existing form controls.

There is no dedicated button/action prop. Existing controls and future Form composition can provide actions without coupling FormField to a specific button implementation.

## Verification

- Automated component tests pass.
- Browser rendering and interaction test passes.
- Main manual browser discovers the manual through `get_app()`.
- Manual verification confirms labels, required state, help text, error presentation, Input, Textarea, and Select behavior.

## Status

Phase 08 FormField is complete.
