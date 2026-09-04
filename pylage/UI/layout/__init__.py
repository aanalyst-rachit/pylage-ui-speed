"""Canonical PyLage UI layout primitives and containers."""

from .row import row
from .column import column
from .factories import (
    AppShell,
    Center,
    Container,
    Footer,
    Header,
    Navigation,
    Pagination,
    Menu,
    Section,
    SidebarLayout,
    Split,
    Stack,
    TwoColumn,
    ThreeColumn,
)
from .navbar import Navbar
from .topbar import Topbar

# Public semantic alias for the top navigation/header.
topheader = Topbar
from .drawer import Drawer, NavigationDrawer, MobileSidebar
from .navigation_controls import NavigationControls

# The following additional primitives remain importable explicitly,
# but the established public API contract intentionally keeps __all__
# limited to the original layout surface.
__all__ = [
    "AppShell",
    "Center",
    "Container",
    "Footer",
    "Header",
    "Navigation",
    "Pagination",
    "Menu",
    "Section",
    "SidebarLayout",
    "Split",
    "Stack",
    "TwoColumn",
    "ThreeColumn",
    "row",
    "column",
    "Topbar",
    "topheader",
]
