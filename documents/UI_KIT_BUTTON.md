# PyLage UI Kit — Button

The UI Kit provides a semantic Button API on top of the existing PyLage
component and rendering infrastructure.

## Basic Usage

    import pylage_ui as ps

    button = ps.button("Save")

The UI Kit returns the existing PyLage Component; it does not introduce a
second component or rendering system.

## Variants

    ps.button("Primary")
    ps.button("Secondary", variant="secondary")
    ps.button("Outline", variant="outline")
    ps.button("Ghost", variant="ghost")
    ps.button("Danger", variant="danger")

Supported variants:

- primary
- secondary
- outline
- ghost
- danger

The default variant is primary.

## Sizes

    ps.button("Small", size="sm")
    ps.button("Medium", size="md")
    ps.button("Large", size="lg")

Supported sizes:

- sm
- md
- lg

The default size is md.

## Disabled State

    ps.button("Save", disabled=True)

The disabled property is forwarded to the existing PyLage Button.

## Events

UI Kit callbacks use the existing PyLage on_* event convention:

    def save():
        print("saved")

    ps.button("Save", on_click=save)

The callback remains part of the existing PyLage event system.

## Custom Styling

The existing Style system can override UI Kit defaults:

    from pylage import Style
    import pylage_ui as ps

    ps.button(
        "Custom",
        style=Style(
            background_color="#123456",
            border_radius="999px",
        ),
    )

UI Kit defaults are applied first; explicit custom styles take precedence.

## API Boundary

variant and size are UI Kit semantic properties. They are consumed by the
UI Kit and are not passed as renderer/component properties.

The implementation reuses:

- pylage.Button
- pylage.Style
- pylage_layout.tokens.COLORS
- the existing PyLage event system
- the existing PyLage renderer

The UI Kit therefore remains a high-level developer API rather than a second
UI engine.
