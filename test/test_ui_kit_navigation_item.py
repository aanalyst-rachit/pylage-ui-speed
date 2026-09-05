from pylage.ENGINE import State, Style
from pylage.ENGINE.core.component import Component
from pylage.ENGINE.core.renderer import render
import pylage as pl


def test_navigation_item_returns_existing_component():
    item = pl.navigation_item("Home")

    assert isinstance(item, Component)
    assert item.type == "Button"
    assert item.props["text"] == "Home"


def test_navigation_item_default_contract():
    item = pl.navigation_item("Home")
    style = item.props["style"]

    assert style.background_color == "transparent"
    assert style.color == "#0f172a"
    assert style.border == "1px solid transparent"
    assert style.border_radius == "0.375rem"
    assert style.padding == "0.5rem 0.75rem"
    assert style.cursor == "pointer"


def test_navigation_item_active_style():
    item = pl.navigation_item("Home", active=True)
    style = item.props["style"]

    assert style.background_color == "#3b82f6"
    assert style.color == "#ffffff"
    assert style.border == "1px solid #3b82f6"


def test_navigation_item_custom_style_overrides_defaults():
    item = pl.navigation_item("Home", style=Style(color="#123456", padding="1rem", border_radius="999px"))
    style = item.props["style"]

    assert style.color == "#123456"
    assert style.padding == "1rem"
    assert style.border_radius == "999px"
    assert style.cursor == "pointer"


def test_navigation_item_forwards_event_handler():
    called = []

    def clicked():
        called.append(True)

    item = pl.navigation_item("Home", on_click=clicked)

    assert item.events["click"] is clicked

    html = render(item)
    assert 'data-pylage-events="click"' in html
    assert "clicked" not in html


def test_navigation_item_does_not_leak_active_prop_to_engine():
    item = pl.navigation_item("Home", active=True)

    assert "active" not in item.props



def test_navigation_item_reactive_active_state():
    active = State(False)
    item = pl.navigation_item("Products", active=active)

    assert item.props["style"].background_color.value == "transparent"
    assert item.props["style"].color.value == "#0f172a"

    active.set(True)

    assert item.props["style"].background_color.value == "#3b82f6"
    assert item.props["style"].color.value == "#ffffff"
    assert item.props["style"].border.value == "1px solid #3b82f6"

    active.set(False)

    assert item.props["style"].background_color.value == "transparent"
    assert item.props["style"].color.value == "#0f172a"


def test_navigation_item_reactive_active_state_does_not_leak_prop():
    active = State(False)
    item = pl.navigation_item("Products", active=active)

    assert "active" not in item.props

    active.set(True)

    assert "active" not in item.props
