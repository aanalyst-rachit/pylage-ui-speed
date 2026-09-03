# UI Kit Help Text

## Overview

Help text is provided through the existing `form_field()` composition component.

It does not require a separate renderer or standalone help-text component.

## Usage

```python
import pylage as pl

pl.form_field(
    pl.input(placeholder="Email address"),
    label="Email",
    help_text="Use your work email address.",
)
```

## Presentation

When `help_text` is supplied, `form_field()` adds an existing PyLage `Text` component after the wrapped control.

The presentation uses the existing text metadata for muted/caption styling.

## Composition

```text
FormField
├── Label
├── Existing control
├── Help text
└── Optional error
```

## Architecture

Help text remains a composition concern rather than becoming a new primitive UI control.

## Verification

- FormField automated tests cover help text.
- FormField browser verification covers rendered help text.
- Manual FormField verification includes help text.

## Status

Help text is complete for Phase 08.
