# PyLage UI Kit — API Conventions

## Purpose

The PyLage UI Kit is a semantic developer-experience layer above the existing PyLage component and layout systems.

It does not replace the renderer, component factory, registry, state engine, styling system, theme system, or layout engine.

Architecture: User API → pylage_ui → existing pylage / pylage_layout → renderer / reactive runtime

## Naming

The public UI Kit API uses lowercase Python names such as `ps.button()`, `ps.card()`, `ps.text()`, `ps.heading()`, `ps.input()`, `ps.select()`, `ps.form()`, `ps.badge()`, `ps.alert()`, `ps.dialog()`, `ps.drawer()`, `ps.tabs()`, and `ps.table()`.

These APIs wrap existing PyLage capabilities rather than creating duplicate rendering primitives.

## Children

Components that contain child content use positional `*children`. Existing PyLage child handling remains authoritative.

## Primary Content

Components with an obvious primary value may expose that value as the first semantic argument, for example `ps.button("Save")`, `ps.text("Hello")`, and `ps.heading("Dashboard")`.

## Props

The UI Kit exposes documented semantic properties while preserving the underlying PyLage compatibility model. The existing component factory preserves unknown properties. The UI Kit must not silently invent aliases.

## Events

The existing `on_*` convention is authoritative. Examples include `ps.button("Save", on_click=save)` and `ps.input(value=state, on_input=handle_input)`.

## Reactive State

The existing `pylage.core.state.State` is the source of truth. The UI Kit consumes existing State behavior and does not introduce another reactive state abstraction.

## Styling

The existing `Style` abstraction remains authoritative. The UI Kit provides sensible defaults but does not replace the styling engine.

## Responsive Styling

The existing `ResponsiveStyle` abstraction remains authoritative. UI Kit responsive defaults must use the existing responsive infrastructure.

## Theme and Tokens

The existing `Theme` and `pylage_layout.tokens` systems remain authoritative for colors, spacing, radius, fonts, and semantic design tokens. The UI Kit must not create a competing theme or token system.

## Variants

Semantic variants use `variant` where appropriate, for example `ps.button("Save", variant="primary")` and `ps.badge("Active", variant="success")`.

The UI Kit may standardize its supported vocabulary without breaking existing engine-level APIs.

## Size

Where a component has meaningful size variants, the UI Kit may expose `size="sm"`, `size="md"`, or `size="lg"`. A size value becomes part of the public contract only when its behavior is implemented and tested.

## Visibility and Disabled State

The UI Kit may expose `visible` where the underlying component supports visibility behavior. It must not create a second visibility mechanism.

Disabled behavior uses the existing `disabled` property, for example `ps.button("Save", disabled=True)`.

## Interaction States

The UI Kit design contract recognizes hover, focus, and disabled states. Existing behavior is reused. Missing visual behavior may be implemented at the UI Kit styling or composition layer without creating a new styling engine.

## Accessibility

The UI Kit should provide sensible accessibility defaults where the underlying engine supports them. Accessibility behavior must not require a separate rendering or DOM abstraction.

## Public Exports

Only explicitly exported UI Kit names are stable public API. Internal implementation helpers remain private. The public surface should remain intentionally small.

## Return Values

UI Kit component functions return the existing PyLage `Component` objects. They do not return rendered HTML, DOM nodes, or framework-specific wrapper objects.

## Compatibility

The UI Kit is additive. Existing APIs such as `from pylage.components.basic import Button` and `from pylage.core.component import component` must continue to work.

## Composition

UI Kit features should prefer reuse and composition over duplicate primitives. Higher-level components and recipes should compose existing PyLage capabilities whenever possible.

## Architecture Boundary

The following remain outside the UI Kit: renderer, WebSocket transport, DOM patch protocol, client runtime, State engine, dependency graph, scheduler, component registry, base Component implementation, CSS engine, Theme implementation, and layout engine.

## Implementation Rule

Every UI Kit addition follows: Inspect → Classify → Reuse → Wrap/Compose → Build only if genuinely missing → Test → Full regression.

BUILD is the last option.

## Phase 04 Contract

Phase 04 freezes these conventions: lowercase Python component names, semantic primary arguments, positional children, existing `on_*` events, existing `State`, existing `Style`, existing `ResponsiveStyle`, existing Theme/tokens, semantic variants, visibility and disabled conventions, accessibility defaults, explicit public exports, return-value behavior, additive compatibility, and composition over duplication.

Phase 05 may implement the first actual UI Kit component.
