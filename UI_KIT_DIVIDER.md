# PyLage UI Kit — Divider

## Overview

`ps.divider()` provides a semantic horizontal separator using the existing PyLage `Divider` primitive.

## API

```python
import pylage_ui as ps

ps.divider()
```

## Default behavior

The UI Kit applies sensible defaults:

- Full available width
- No default browser border
- Semantic muted top border
- Vertical margin for visual separation

## Customization

A PyLage `Style` can override the defaults:

```python
from pylage import Style

ps.divider(
    style=Style(
        border_top="2px solid #111827",
        margin="2rem 0",
    )
)
```

## Architecture

The UI Kit does not introduce a new renderer or primitive. `ps.divider()` wraps the existing `pylage.Divider` and adds the semantic UI Kit styling contract.

Engine props and events are forwarded to the underlying component.
