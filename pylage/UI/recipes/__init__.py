"""Canonical reusable PyLage page recipes."""

from .landing import LandingPage
from .dashboard import Dashboard
from .admin import AdminPanel
from .authentication import Authentication
from .profile import ProfilePage
from .settings import Settings, SettingsPage
from .documentation import Documentation
from .modal import modal

Admin = AdminPanel
Landing = LandingPage
Profile = ProfilePage

__all__ = [
    "LandingPage",
    "Dashboard",
    "AdminPanel",
    "Authentication",
    "ProfilePage",
]
