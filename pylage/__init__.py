"""PyLage public API.

Users interact with PyLage through this module.

Public surface:
    ps.*       -> UI components, layouts, patterns, recipes
    style.*    -> individual style presets
    theme.*    -> complete themes

ENGINE is an internal implementation detail and is intentionally
not exported from the root public API.
"""

from pylage.ENGINE.app import run
from pylage.UI import *
from pylage.UI import __all__ as _ui_all
from pylage.UI import style
from pylage.UI import themes as theme

# Root public package metadata.
# This is intentionally independent from the legacy pylage_ui facade.
IMPORT_NAME = "pylage"
PACKAGE_NAME = "pylage-ui-kit"

__all__ = list(dict.fromkeys([
    "run",
    *_ui_all,
    "style",
    "theme",
    "IMPORT_NAME",
    "PACKAGE_NAME",
])) # type: ignore
