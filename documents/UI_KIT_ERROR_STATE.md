# UI Kit Error State

## Overview

`error_state()` provides a semantic, high-level error feedback component for page, section, operation, or system-level failures.

It is separate from field-level validation feedback: `form_field(error=...)` is used for individual fields, while `error_state()` is intended for broader failure states.

## Basic Usage

```python
import pylage as pl

pl.error_state()
```

## Custom Error State

```python
import pylage as pl

pl.error_state(
    title="Failed to load dashboard",
    description="The connection to the database timed out.",
    icon="⚠️",
    action=pl.button("Retry", variant="danger"),
)
```

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `title` | `Any` | `"Something went wrong"` | Primary error headline |
| `description` | `Any` | `"An error occurred while processing your request."` | Error explanation or recovery guidance |
| `icon` | `Any` | `"⚠️"` | Warning icon, text, or component |
| `action` | `Any` | `None` | Optional recovery/action component |
| `style` | `Style` | `None` | Custom style overrides |
| `**props` | `Any` | — | Forwarded root component properties |

## Architecture

`error_state()` reuses existing PyLage engine primitives and does not introduce a new renderer, runtime, or error-handling engine.

## Verification

- Automated UI Kit ErrorState tests pass.
- Manual error-state verification exists.
- Custom content, actions, styles, and forwarded properties are covered.

## Status

Error state is complete for Phase 08.
