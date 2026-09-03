# UI Kit Loading State

`pylage_ui.loading_state()` provides a semantic, high-level loader and spinner feedback card for data fetching and async operations.

## Basic Usage

```python
import pylage_ui as ps

ps.loading_state()
```

## Custom Text and Description

```python
import pylage_ui as ps

ps.loading_state(
    text="Importing dataset...",
    description="Please wait while your data is parsed and verified.",
)
```

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `text` | `Any` | `"Loading..."` | Primary loading indicator label |
| `description` | `Any` | `None` | Optional subtitle or secondary context message |
| `spinner` | `bool` | `True` | Whether to display the animated spinner component |
| `style` | `Style` | `None` | Style overrides merged with default container style |
| `**props` | `Any` | — | Forwarded to root component |

## Reactive Binding

```python
from pylage import State
import pylage_ui as ps

status = State("Connecting...")
ps.loading_state(text=status)
```
