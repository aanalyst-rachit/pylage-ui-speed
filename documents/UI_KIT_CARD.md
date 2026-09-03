# UI Kit Card

`pylage_ui.card()` provides a semantic, high-level Card API while reusing the existing PyLage Card and primitive components.

## Basic usage

```python
import pylage_ui as ui

ui.card(heading="Revenue", body="₹42,000", footer="Monthly revenue")
```

## Optional sections

```python
ui.card(heading="Revenue", body="₹42,000")
ui.card(body="Nothing to show")
```

## Variants

Supported variants:

- `default`
- `elevated`
- `outlined`
- `interactive`

```python
ui.card(heading="Active Users", body="12,450", variant="elevated")
```

## Interactive card

Cards support the existing PyLage event system:

```python
ui.card(
    heading="Click me",
    body="Interactive content",
    variant="interactive",
    on_click=handle_click,
)
```

Event handling uses the existing PyLage runtime event delegation.

## Advanced composition

Existing PyLage children remain supported:

```python
import pylage as ps
import pylage_ui as ui

ui.card(
    ps.Column(
        ps.Heading("Custom Header"),
        ps.Text("Custom body"),
    ),
    variant="elevated",
)
```

The UI Kit does not introduce separate CardHeader, CardBody, or CardFooter engine components. Semantic sections are composed from existing PyLage primitives.

## Custom styling

Use `style=` for customization:

```python
from pylage import Style

ui.card(
    heading="Revenue",
    body="₹42,000",
    style=Style(background_color="#f8fafc"),
)
```
