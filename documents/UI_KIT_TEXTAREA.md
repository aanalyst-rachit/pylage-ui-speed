# PyLage UI Kit — Textarea

## Overview

`ps.textarea()` provides a Python-first multi-line text input for the PyLage UI Kit.

It wraps the existing PyLage engine textarea capability without introducing a separate renderer or client-side implementation.

## API

    import pylage as ps

    ps.textarea(
        value="",
        style=None,
        **props,
    )

## Basic Usage

    import pylage as ps

    ps.textarea(
        placeholder="Enter your message...",
        rows=5,
    )

## State Binding

A `State` can be supplied as the textarea value.

    import pylage as ps
    from pylage.ENGINE import State

    message = State("")

    ps.textarea(
        message,
        placeholder="Write something...",
    )

When no explicit `on_input` handler is supplied, the UI Kit automatically updates the supplied `State` from browser input events.

## Custom Input Handler

An explicit `on_input` handler is preserved when supplied.

    def handle_input(payload):
        print(payload)

    ps.textarea(
        "",
        on_input=handle_input,
    )

The handler receives the existing PyLage input event payload.

## Supported Properties

Textarea supports common native textarea properties including:

- `value`
- `placeholder`
- `name`
- `rows`
- `cols`
- `disabled`
- `required`
- `readonly`
- `title`
- `minlength`
- `maxlength`

Additional PyLage component properties and styling can be supplied through the normal UI Kit component API.

## Styling

Textarea accepts the standard PyLage `Style` object.

    from pylage.ENGINE import Style
    import pylage as ps

    ps.textarea(
        placeholder="Notes",
        rows=6,
        style=Style(
            width="100%",
            padding="0.75rem",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            box_sizing="border-box",
        ),
    )

## Disabled State

    ps.textarea(
        "This field cannot be edited.",
        disabled=True,
    )

The `disabled` property is rendered as the native HTML textarea disabled attribute.

## Architecture

Textarea follows the existing PyLage architecture:

    PyLage UI Kit
        ↓
    pylage.UI.components.textarea
        ↓
    PyLage Engine Component
        ↓
    Existing Registry
        ↓
    Existing Generic Renderer
        ↓
    Native <textarea>

No separate JavaScript renderer, HTML template system, or alternate reactive pipeline is introduced.

## Verification

Textarea was manually verified in a browser using:

- Native textarea rendering
- Placeholder and rows
- Reactive `State` input binding
- Custom `on_input` handling
- Disabled state
- Native textarea attributes
- PyLage client runtime

Automated component tests: 9 passed

Browser manual verification: all checks passed

Manual application:

    app/ui_kit_textarea_manual.py

## Status

Textarea is complete for Phase 08 Forms.

- API: Complete
- Engine integration: Complete
- UI Kit wrapper: Complete
- Automated tests: Complete
- Browser manual verification: Complete
- Documentation: Complete
