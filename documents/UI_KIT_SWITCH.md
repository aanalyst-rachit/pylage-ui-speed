# UI Kit Switch

## Overview

The PyLage UI Kit `switch()` component provides a Python-first boolean toggle control using the existing PyLage engine `Switch` component.

The public UI Kit wrapper reuses the existing engine implementation.

## Behavior

- Supports checked True and False values.
- Supports State-bound checked values.
- Synchronizes State to the browser.
- Synchronizes browser changes back to State.
- Preserves the on_change callback.
- Supports disabled switches and standard attributes.

## Architecture

Python application → pylage.switch() → UI Kit wrapper → ENGINE.Switch → existing registry / renderer / runtime

No duplicate renderer or runtime implementation is introduced.

## Reactive State Binding

A State passed to checked is synchronized in both directions: Python State to browser, and browser change back to Python State.

## Verification

Automated Switch coverage: 11 passed.

Manual browser verification passed for basic, checked, state-bound, disabled, event, and native-property behavior.

## Status

Phase 08 — Forms: Switch COMPLETE.
