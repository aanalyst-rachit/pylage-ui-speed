# UI Kit Badge

`ps.badge()` provides a semantic UI Kit wrapper around the existing PyLage `Badge` primitive.

## Basic usage

```python
import pylage_ui as ps

ps.badge("Active")
```

## Variants

```python
ps.badge("Default")
ps.badge("Primary", variant="primary")
ps.badge("Secondary", variant="secondary")
ps.badge("Success", variant="success")
ps.badge("Warning", variant="warning")
ps.badge("Danger", variant="danger")
ps.badge("Info", variant="info")
```

Supported variants:

- `default`
- `primary`
- `secondary`
- `success`
- `warning`
- `danger`
- `info`

## Styling

Badges receive UI Kit defaults for compact padding, full radius, small typography, semibold text, and semantic background, text, and border colors.

Custom styling can override the defaults:

```python
from pylage import Style

ps.badge(
    "Custom",
    style=Style(
        font_size="0.875rem",
        padding="0.5rem 0.75rem",
    ),
)
```

## Composition

Component children remain supported:

```python
from pylage import Text

ps.badge(Text("Active"))
```

Primitive children are composed through the existing PyLage `Text` primitive rather than introducing a new renderer or Badge content engine.

Reactive values are also supported through the existing PyLage state system.

## Props and events

Existing PyLage props and event callbacks can be forwarded.

## Architecture

```text
Developer
    ↓
pylage_ui.badge()
    ↓
semantic UI Kit defaults
    ↓
pylage.Badge + pylage.Text
    ↓
existing PyLage renderer
```

The UI Kit does not introduce a new Badge renderer, styling engine, or state system.
