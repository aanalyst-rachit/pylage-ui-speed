# UI Kit Disabled State

## Overview

Disabled state is provided by the existing UI Kit controls and their underlying PyLage engine implementations.

No separate disabled-state component is required.

## Supported Controls

The Phase 08 controls already expose native disabled behavior where applicable, including:

- Input
- Textarea
- Select
- Checkbox
- Radio
- Switch
- Slider
- DatePicker
- Button

## Usage

```python
import pylage as pl

pl.input(disabled=True)
pl.textarea(disabled=True)
pl.select(disabled=True)
pl.checkbox(disabled=True)
pl.switch(disabled=True)
pl.slider(disabled=True)
pl.datepicker(disabled=True)
pl.button("Save", disabled=True)
```

## Reactive Disabled State

Existing reactive property infrastructure also supports updating disabled state through the established State/runtime mechanism where the individual control supports reactive properties.

## Architecture

Disabled state is a control-level property handled by the existing renderer and runtime. Phase 08 does not introduce a duplicate disabled-state abstraction.

## Verification

- Existing component tests cover disabled behavior across Phase 08 controls.
- Browser reactive-property coverage includes disabled-state behavior.
- Existing manuals provide control-level manual verification.

## Status

Disabled state is complete for Phase 08.
