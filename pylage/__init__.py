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

__all__ = [
    "run",
    *_ui_all,
    "style",
    "theme",
    "IMPORT_NAME",
    "PACKAGE_NAME",
]

# ---------------------------------------------------------------------------
# Legacy compatibility surface
#
# These names are retained so existing applications/tests continue to work.
# New application code should prefer the semantic lowercase UI API:
#     ps.button, ps.card, ps.topheader
# and the namespaces:
#     style.*, theme.*
#
# ENGINE remains an internal implementation detail.
# ---------------------------------------------------------------------------

from pylage.ENGINE.components.basic import (
    Canvas,
    Icon,
    Audio,
    Video,
    Image,
    Grid,
    Carousel,
    Accordion,
    Avatar,
    Badge,
    Divider,
    Button,
    Card,
    Column,
    Row,
    Dialog,
    Form,
    Heading,
    Input,
    Navigation,
    RadioGroup,
    Select,
    Option,
    Slider,
    Switch,
    Table,
    DataFrame,
    Tabs,
    Text,
    Checkbox,
    DatePicker,
    Alert,
    Toast,
    Spinner,
    ProgressBar,
    Skeleton,
    Breadcrumbs,
    Pagination,
    Menu,
    Drawer,
    Tooltip,
    Popover,
)

from pylage.ENGINE.core.state import State
from pylage.ENGINE.styling import Style, Theme, ResponsiveStyle
