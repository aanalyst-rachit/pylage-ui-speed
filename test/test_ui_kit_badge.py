from pylage.ENGINE import Badge as EngineBadge
from pylage.ENGINE import State, Style
from pylage.ENGINE.core.renderer import render

import pylage.UI as ui


def test_badge_returns_existing_badge_component():
    badge = ui.badge("Active")

    assert badge.type == "Badge"
    assert isinstance(badge, type(EngineBadge()))


def test_badge_default_contract():
    badge = ui.badge("Active")

    style = badge.props["style"]

    assert style.background_color == "#f1f5f9"
    assert style.color == "#0f172a"
    assert style.border == "1px solid #e2e8f0"
    assert style.padding == "0.25rem 0.625rem"
    assert style.border_radius == "9999px"
    assert style.font_size == "0.75rem"
    assert style.font_weight == "600"


def test_badge_renders_content():
    html = render(ui.badge("Active"))

    assert "Active" in html


def test_badge_supports_reactive_content():
    status = State("Online")

    badge = ui.badge(status)

    assert "Online" in render(badge)


def test_badge_variants():
    expected = {
        "primary": ("#3b82f6", "#ffffff"),
        "secondary": ("#64748b", "#ffffff"),
        "success": ("#22c55e", "#ffffff"),
        "warning": ("#f59e0b", "#0f172a"),
        "danger": ("#ef4444", "#ffffff"),
        "info": ("#06b6d4", "#ffffff"),
    }

    for variant, (background, foreground) in expected.items():
        badge = ui.badge("Status", variant=variant)
        style = badge.props["style"]

        assert style.background_color == background
        assert style.color == foreground


def test_badge_custom_style_overrides_defaults():
    custom = Style(
        background_color="#111827",
        color="#ffffff",
        padding="0.5rem 1rem",
    )

    badge = ui.badge("Custom", style=custom)
    style = badge.props["style"]

    assert style.background_color == "#111827"
    assert style.color == "#ffffff"
    assert style.padding == "0.5rem 1rem"
    assert style.border_radius == "9999px"


def test_badge_does_not_leak_variant_to_engine_props():
    badge = ui.badge("Success", variant="success")

    assert "variant" not in badge.props


def test_badge_forwards_engine_props():
    badge = ui.badge(
        "Active",
        class_name="status-badge",
        title="Current status",
    )

    html = render(badge)

    assert 'class="status-badge"' in html
    assert 'title="Current status"' in html


def test_badge_forwards_events():
    clicked = []

    def on_click():
        clicked.append(True)

    badge = ui.badge("Click", on_click=on_click)

    assert "click" in badge.events

    html = render(badge)

    assert 'data-pylage-events="click"' in html


def test_badge_rejects_unknown_variant():
    try:
        ui.badge("Status", variant="unknown")
    except ValueError as exc:
        assert "Unknown badge variant" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
