## Overview

`toast()` provides a semantic, high-level feedback component for transient informational, success, warning, and error messages.

The UI Kit Toast is a thin wrapper around the existing PyLage engine `Toast` component.

## Variants

Supported variants: `default`, `info`, `success`, `warning`, `danger`, and `error`.

## Composition

Toast accepts existing PyLage components as children. Plain child values are normalized into existing PyLage `Text` components.

## Visibility

Toast supports the existing engine `visible` prop:

```text
visible=True  → hidden absent
visible=False → hidden present
```

The framework renderer emits the semantic CSS rule `[hidden] { display: none !important; }`.

This ensures the native hidden state remains authoritative even when Toast uses an inline `display:flex` style.

## Styling

The wrapper applies UI Kit design tokens for spacing, radius, semantic colors, borders, and surface styling. A supplied `style` is merged last.

## Architecture

```text
pl.toast()
    ↓
UI Kit toast wrapper
    ↓
PyLage ENGINE Toast
    ↓
visible → inverse hidden attribute
```

## Verification

* UI Kit Toast automated tests: **15 passed**.
* Visible and hidden rendering regression tests pass.
* Renderer `[hidden]` semantic CSS regression test passes.
* Manual browser toggle verification passed.
* Full project test suite: **965 passed**.

## Resolution

The Toast visibility issue was caused by inline `display:flex` overriding the browser default `[hidden]` presentation. The framework renderer now emits the semantic `[hidden]` rule with `display: none` and `!important`, preserving native hidden semantics without Toast-specific runtime logic.

## Status

Toast is **COMPLETE** for Phase 09 Feedback & Overlays.
