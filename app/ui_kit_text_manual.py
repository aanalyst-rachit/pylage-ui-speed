from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pylage as ps
from pylage import Column


def get_app():
    return Column(
        ps.heading("Surface Components"),
        ps.text("Primary body text"),
        ps.text("Secondary information", muted=True),
        ps.text("Field label", label=True),
        ps.text("Small metadata", caption=True),
    )
