
## Overview

`toast()` provides a semantic, high-level feedback component for transient informational, success, warning, and error messages.

The UI Kit Toast is a thin wrapper around the existing PyLage engine `Toast` component. It does not introduce a new renderer, runtime, or feedback engine.

> 🔴 **BUG — to be checked before final publishing or find alternative.**

## Basic Usage

```python
import pylage as pl

pl.toast("Your changes have been saved.")
````

## Variants

Supported semantic variants are:

| Variant   | Purpose                                   |
| --------- | ----------------------------------------- |
| `default` | Neutral informational feedback            |
| `info`    | Informational feedback                    |
| `success` | Successful operation feedback             |
| `warning` | Caution or review feedback                |
| `danger`  | Failure or destructive-operation feedback |
| `error`   | Error feedback                            |

Example:

```python
import pylage as pl

pl.toast("Profile updated.", variant="success")
pl.toast("Please review this action.", variant="warning")
pl.toast("The operation failed.", variant="danger")
pl.toast("Additional information.", variant="info")
```

## Composition

Toast accepts existing PyLage components as children and preserves component composition.

```python
import pylage as pl

pl.toast(
    pl.text("Component composition"),
    pl.text("Existing PyLage components remain valid children."),
    variant="info",
)
```

Plain child values are normalized into existing PyLage `Text` components.

## Parameters

| Parameter   | Type    | Default     | Description                                 |
| ----------- | ------- | ----------- | ------------------------------------------- |
| `*children` | `Any`   | —           | Toast content or existing PyLage components |
| `variant`   | `str`   | `"default"` | Semantic visual variant                     |
| `style`     | `Style` | `None`      | Custom style overrides                      |
| `**props`   | `Any`   | —           | Forwarded to the underlying PyLage Toast    |

## Styling

The wrapper applies UI Kit design tokens for spacing, radius, semantic colors, borders, and surface styling. A supplied `style` is merged last so developers can override the defaults.

## Architecture

```text
pl.toast()
    ↓
UI Kit toast wrapper
    ↓
PyLage ENGINE Toast
```

This implementation follows the UI Kit architecture by reusing the existing engine component instead of duplicating feedback infrastructure.

## Verification

* UI Kit Toast automated tests exist.
* Toast rendering and reactive visibility behavior require further verification.
* Manual browser verification is not considered complete.
* Public API integration requires final verification.

## Known Issue

🔴 **BUG — to be checked before final publishing or find alternative.**

Toast currently has an unresolved behavior issue. The component must not be marked complete until the issue is reproduced, root cause is confirmed, and the final behavior is manually verified.

## Status

Toast is **ON HOLD** for Phase 09.

Resolution is pending. Before final publishing, the bug must be checked and fixed, or an alternative implementation/component must be selected.
"""); print("OK: documents/UI_KIT_TOAST.md created")'

````

### M/V

Phir:

```bash
cat documents/UI_KIT_TOAST.md
````

Aur status check:

```bash
grep -n -A8 -B2 "Known Issue\|Status" documents/UI_KIT_TOAST.md
```