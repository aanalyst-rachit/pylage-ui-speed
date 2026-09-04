# UI Kit Column

## Overview

The UI Kit `column()` wrapper reuses the existing PyLage Engine `Column` component. It does not create a duplicate layout engine.

## API

- `pylage.UI.column`
- `pylage.UI.layout.column`
- Filters `None` children.
- Supports `Style` and `ResponsiveStyle`.
- Uses the existing UI Kit responsive style resolution.
- Supports reactive `State` values nested inside `Style`.

## Verification

- Column wrapper renders through the existing Engine `Column`.
- Reactive `gap` was manually verified by changing `1rem` to `2rem` and back.
- Reactive background color was also verified.
- State binding regression coverage was added for `State` nested inside `Style`.
- Full test suite: `949 passed`.

## Architecture

The wrapper delegates to the existing PyLage Engine and does not duplicate rendering, state, scheduler, WebSocket, or CSS systems.
