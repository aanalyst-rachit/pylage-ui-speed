# UI Kit Error State

`pylage_ui.error_state()` provides a semantic, high-level error boundary and feedback card for failure scenarios and system errors.

## Basic Usage

```python
import pylage_ui as ps

ps.error_state()
```

## With Custom Action and Details

```python
import pylage_ui as ps

ps.error_state(
    title="Failed to load dashboard",
    description="The connection to the database timed out.",
    icon="⚠️",
    action=ps.button("Retry", variant="danger"),
)
```

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `title` | `Any` | `"Something went wrong"` | Primary error headline |
| `description` | `Any` | `"An error occurred..."` | Explanation or recovery guidance |
| `icon` | `Any` | `"⚠️"` | Warning icon or emoji |
| `action` | `Any` | `None` | Retry or recovery action button |
| `style` | `Style` | `None` | Custom style overrides |
| `**props` | `Any` | — | Forwarded to root component |

## Custom Styling

```python
from pylage import Style
import pylage_ui as ps

ps.error_state(
    title="Service Unavailable",
    style=Style(border="2px solid #ef4444", background_color="#fef2f2"),
)
```
