from __future__ import annotations

from typing import Any
from pylage_layout.templates.dashboard import Dashboard as _Dashboard
from .stat_group import stat_group

def dashboard(
    *,
    title: Any = None,
    header: Any = None,
    sidebar: Any = None,
    metrics: Any = None,
    stats: Any = None,
    filters: Any = None,
    content: Any = None,
    table: Any = None,
    footer: Any = None,
    **props: Any,
):
    """Compose a complete, responsive dashboard page layout with minimal Python."""
    effective_stats = metrics if metrics is not None else stats
    if isinstance(effective_stats, (list, tuple)) and len(effective_stats) > 0:
        effective_stats = stat_group(*effective_stats)

    return _Dashboard(
        header=header,
        sidebar=sidebar,
        content=content,
        stats=effective_stats,
        table=table,
        footer=footer,
        title=title,
        filters=filters,
        **props,
    )
