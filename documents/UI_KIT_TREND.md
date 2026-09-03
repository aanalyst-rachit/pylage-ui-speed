# PyLage UI Kit — Trend

`ps.trend()` is a semantic UI Kit component for displaying directional change, movement, or comparison values.

It is designed to complement `ps.metric()` and other dashboard components.

## Quick Start

```python
import pylage_ui as ps

trend = ps.trend("+12%")
```

## Direction Detection

When `direction` is not provided, PyLage detects it from the value:

```python
ps.trend("+12%")   # Up
ps.trend("-8.5%")  # Down
ps.trend("0%")     # Neutral
```

## Explicit Direction

Use `direction` when the text itself does not contain a `+` or `-` sign:

```python
ps.trend("Improving", direction="up")
ps.trend("Declining", direction="down")
ps.trend("Stable", direction="neutral")
```

Available directions:

- `up`
- `down`
- `neutral`

## Indicators

By default, `ps.trend()` displays a directional indicator:

```python
ps.trend("+12%")
ps.trend("-8%")
ps.trend("0%")
```

Hide the indicator when only semantic styling is needed:

```python
ps.trend("+12%", show_indicator=False)
```

## Reactive Values

`ps.trend()` supports reactive `pylage.State` values:

```python
from pylage import State
import pylage_ui as ps

change = State("+12%")
trend = ps.trend(change)
```

## Custom Styling

Custom styles override the default semantic styling:

```python
from pylage import Style
import pylage_ui as ps

trend = ps.trend(
    "+12%",
    style=Style(padding="0.5rem 1rem"),
)
```

## Dashboard Usage

Use `ps.trend()` alongside `ps.metric()` to show directional context:

```python
ps.metric(
    label="Revenue",
    value="₹42,000",
)

ps.trend("+12%")
```

`ps.metric()` represents the primary KPI value, while `ps.trend()` communicates how that value is moving or changing.
