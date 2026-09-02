"""
mydash.py — Modern PyLage Dashboard (Live Demo)

Run directly:
    python mydash.py

This renders a modern, card-based dashboard with:
- Gradient sidebar navigation (reactive — click to switch pages)
- Global modern typography (system-ui font stack)
- Rounded cards, soft shadows, consistent spacing
- Reactive stat cards bound to pylage.State
- A simple data table + activity feed

No JavaScript authored — pure Python + PyLage's reactive engine.
"""

import pylage as ps
from pylage import Style, State


# ============================================================
# Design tokens (kept local so this file is fully standalone)
# ============================================================

COLORS = {
    "bg": "#f4f6fb",
    "surface": "#ffffff",
    "border": "#e5e9f2",
    "text": "#0f172a",
    "text_muted": "#64748b",
    "primary": "#4f46e5",
    "primary_soft": "#eef2ff",
    "success": "#16a34a",
    "success_soft": "#dcfce7",
    "warning": "#d97706",
    "warning_soft": "#fef3c7",
    "danger": "#dc2626",
    "danger_soft": "#fee2e2",
    "sidebar_from": "#4f46e5",
    "sidebar_to": "#4338ca",
}

FONT = "'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"


def card_style(**overrides) -> Style:
    base = dict(
        background_color=COLORS["surface"],
        border="1px solid " + COLORS["border"],
        border_radius="1rem",
        padding="1.5rem",
        box_shadow="0 1px 3px rgba(15, 23, 42, 0.06), 0 1px 2px rgba(15, 23, 42, 0.04)",
        box_sizing="border-box",
    )
    base.update(overrides)
    return Style(**base) # type: ignore


# ============================================================
# App state
# ============================================================

active_page = State("Overview")
revenue = State(48200)
active_users = State(1284)
conversion = State("4.8%")
notif_count = State(3)

NAV_ITEMS = [
    ("Overview", "🏠"),
    ("Analytics", "📈"),
    ("Customers", "👥"),
    ("Settings", "⚙️"),
]


# ============================================================
# Sidebar
# ============================================================

def build_sidebar():
    nav_buttons = []

    for label, icon in NAV_ITEMS:
        is_active = active_page.value == label

        nav_buttons.append(
            ps.Button(
                f"{icon}  {label}",
                on_click=(lambda name=label: (lambda e=None: active_page.set(name)))(label),
                style=Style(
                    width="100%",
                    text_align="left",
                    padding="0.75rem 1rem",
                    margin_bottom="0.4rem",
                    border="none",
                    border_radius="0.6rem",
                    cursor="pointer",
                    font_size="0.95rem",
                    font_weight="600" if is_active else "500",
                    color="#ffffff" if is_active else "rgba(255,255,255,0.75)",
                    background_color="rgba(255,255,255,0.15)" if is_active else "transparent",
                ),
            )
        )

    return ps.Column(
        ps.Row(
            ps.Text(
                "⚡ MyDash",
                style=Style(
                    color="#ffffff",
                    font_size="1.35rem",
                    font_weight="800",
                ),
            ),
            style=Style(margin_bottom="2rem", padding="0 0.25rem"),
        ),
        ps.Column(*nav_buttons, style=Style(gap="0.1rem")),
        ps.Column(
            ps.Text(
                "Signed in as",
                style=Style(color="rgba(255,255,255,0.55)", font_size="0.75rem"),
            ),
            ps.Text(
                "Rachit Kumar",
                style=Style(color="#ffffff", font_size="0.9rem", font_weight="600"),
            ),
            style=Style(margin_top="auto", padding_top="1.5rem", border_top="1px solid rgba(255,255,255,0.15)"),
        ),
        style=Style(
            width="240px",
            min_width="240px",
            height="100vh",
            padding="1.5rem 1.25rem",
            background=f"linear-gradient(180deg, {COLORS['sidebar_from']} 0%, {COLORS['sidebar_to']} 100%)",
            display="flex",
            flex_direction="column",
            box_sizing="border-box",
            position="sticky",
            top="0",
        ),
    )


# ============================================================
# Topbar
# ============================================================

def build_topbar():
    return ps.Row(
        ps.Column(
            ps.Text(
                active_page,
                style=Style(font_size="1.5rem", font_weight="800", color=COLORS["text"]),
            ),
            ps.Text(
                "Welcome back — here's what's happening today.",
                style=Style(font_size="0.9rem", color=COLORS["text_muted"]),
            ),
        ),
        ps.Row(
            ps.Column(
                ps.Text("🔔", style=Style(font_size="1.2rem")),
                style=Style(
                    padding="0.6rem",
                    background_color=COLORS["surface"],
                    border="1px solid " + COLORS["border"],
                    border_radius="0.75rem",
                    position="relative",
                    cursor="pointer",
                ),
            ),
            ps.Text(
                notif_count,
                style=Style(
                    color="#ffffff",
                    background_color=COLORS["danger"],
                    font_size="0.7rem",
                    font_weight="700",
                    padding="0.05rem 0.4rem",
                    border_radius="999px",
                    margin_left="-0.6rem",
                    margin_top="-1.4rem",
                ),
            ),
            ps.Column(
                ps.Text("RK", style=Style(color="#ffffff", font_weight="700", font_size="0.85rem")),
                style=Style(
                    width="38px",
                    height="38px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    background_color=COLORS["primary"],
                    border_radius="999px",
                    margin_left="0.75rem",
                ),
            ),
            style=Style(align_items="flex-start", gap="0.25rem"),
        ),
        style=Style(
            justify_content="space-between",
            align_items="center",
            margin_bottom="1.75rem",
        ),
    )


# ============================================================
# Stat cards
# ============================================================

def stat_card(icon, label, value, delta, delta_positive, accent_bg, accent_color):
    return ps.Column(
        ps.Row(
            ps.Column(
                ps.Text(icon, style=Style(font_size="1.4rem")),
                style=Style(
                    width="44px",
                    height="44px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    background_color=accent_bg,
                    border_radius="0.75rem",
                ),
            ),
            ps.Text(
                delta,
                style=Style(
                    font_size="0.8rem",
                    font_weight="700",
                    color=COLORS["success"] if delta_positive else COLORS["danger"],
                    background_color=COLORS["success_soft"] if delta_positive else COLORS["danger_soft"],
                    padding="0.2rem 0.55rem",
                    border_radius="999px",
                ),
            ),
            style=Style(justify_content="space-between", align_items="center", margin_bottom="1rem"),
        ),
        ps.Text(
            value,
            style=Style(font_size="1.6rem", font_weight="800", color=COLORS["text"], margin_bottom="0.15rem"),
        ),
        ps.Text(
            label,
            style=Style(font_size="0.85rem", color=COLORS["text_muted"]),
        ),
        style=card_style(),
    )


def build_stats_row():
    # NOTE: pass raw State objects / plain values here — stat_card()
    # already wraps `value` in ps.Text(...) internally. Passing an
    # already-built Text component double-wraps it and causes the
    # Component's repr() to leak into the rendered HTML instead of
    # the actual number.
    return ps.Row(
        stat_card("💰", "Total Revenue", revenue, "+24.1%", True, COLORS["primary_soft"], COLORS["primary"]),
        stat_card("👥", "Active Users", active_users, "+8.4%", True, "#ecfeff", "#0891b2"),
        stat_card("🎯", "Conversion Rate", conversion, "-1.2%", False, COLORS["warning_soft"], COLORS["warning"]),
        stat_card("⚡", "Uptime", "99.98%", "+0.02%", True, COLORS["success_soft"], COLORS["success"]),
        style=Style(gap="1.25rem", margin_bottom="1.75rem", flex_wrap="wrap"),
    )


# ============================================================
# Chart-ish placeholder + activity feed (pure CSS, no JS lib)
# ============================================================

def build_fake_bar_chart():
    bars = [40, 65, 50, 80, 55, 90, 70]
    bar_cols = []

    for i, h in enumerate(bars):
        bar_cols.append(
            ps.Column(
                ps.Column(
                    style=Style(
                        width="28px",
                        height=f"{h}%",
                        background=f"linear-gradient(180deg, {COLORS['primary']} 0%, #818cf8 100%)",
                        border_radius="0.4rem 0.4rem 0 0",
                        margin="auto",
                    ),
                ),
                ps.Text(
                    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][i],
                    style=Style(font_size="0.72rem", color=COLORS["text_muted"], text_align="center", margin_top="0.4rem"),
                ),
                style=Style(display="flex", flex_direction="column", justify_content="flex-end", height="100%", flex="1"),
            )
        )

    return ps.Column(
        ps.Row(
            ps.Text("Revenue — This Week", style=Style(font_size="1rem", font_weight="700", color=COLORS["text"])),
            ps.Text("Live", style=Style(
                font_size="0.7rem", font_weight="700", color=COLORS["success"],
                background_color=COLORS["success_soft"], padding="0.15rem 0.5rem", border_radius="999px",
            )),
            style=Style(justify_content="space-between", align_items="center", margin_bottom="1.25rem"),
        ),
        ps.Row(
            *bar_cols,
            style=Style(align_items="flex-end", height="160px", gap="0.75rem"),
        ),
        style=card_style(**{"flex": "2"}),
    )


def build_activity_feed():
    items = [
        ("🟢", "New order #4821 received", "2 min ago"),
        ("🔵", "Server deployment completed", "18 min ago"),
        ("🟡", "Payment retry scheduled", "45 min ago"),
        ("🟢", "New user signed up", "1 hr ago"),
    ]

    rows = []
    for icon, text, time in items:
        rows.append(
            ps.Row(
                ps.Text(icon, style=Style(font_size="0.9rem", margin_right="0.6rem")),
                ps.Column(
                    ps.Text(text, style=Style(font_size="0.85rem", color=COLORS["text"], font_weight="500")),
                    ps.Text(time, style=Style(font_size="0.72rem", color=COLORS["text_muted"])),
                ),
                style=Style(align_items="flex-start", padding="0.6rem 0", border_bottom="1px solid " + COLORS["border"]),
            )
        )

    return ps.Column(
        ps.Text("Recent Activity", style=Style(font_size="1rem", font_weight="700", color=COLORS["text"], margin_bottom="0.75rem")),
        ps.Column(*rows),
        style=card_style(**{"flex": "1"}),
    )


# ============================================================
# Data table
# ============================================================

def build_table():
    rows_data = [
        ("#4821", "Aarav Mehta", "Pro Plan", "Paid", COLORS["success"], COLORS["success_soft"]),
        ("#4820", "Sara Kapoor", "Starter", "Pending", COLORS["warning"], COLORS["warning_soft"]),
        ("#4819", "Devon Wilkins", "Enterprise", "Paid", COLORS["success"], COLORS["success_soft"]),
        ("#4818", "Priya Nair", "Pro Plan", "Failed", COLORS["danger"], COLORS["danger_soft"]),
    ]

    header_row = ps.Row(
        ps.Text("Order", style=Style(flex="1", font_size="0.78rem", font_weight="700", color=COLORS["text_muted"])),
        ps.Text("Customer", style=Style(flex="2", font_size="0.78rem", font_weight="700", color=COLORS["text_muted"])),
        ps.Text("Plan", style=Style(flex="1", font_size="0.78rem", font_weight="700", color=COLORS["text_muted"])),
        ps.Text("Status", style=Style(flex="1", font_size="0.78rem", font_weight="700", color=COLORS["text_muted"])),
        style=Style(padding="0 0 0.75rem 0", border_bottom="1px solid " + COLORS["border"]),
    )

    body_rows = [header_row]

    for order, customer, plan, status, color, bg in rows_data:
        body_rows.append(
            ps.Row(
                ps.Text(order, style=Style(flex="1", font_size="0.85rem", color=COLORS["text"], font_weight="600")),
                ps.Text(customer, style=Style(flex="2", font_size="0.85rem", color=COLORS["text"])),
                ps.Text(plan, style=Style(flex="1", font_size="0.85rem", color=COLORS["text_muted"])),
                ps.Text(
                    status,
                    style=Style(
                        flex="1",
                        font_size="0.75rem",
                        font_weight="700",
                        color=color,
                        background_color=bg,
                        padding="0.2rem 0.6rem",
                        border_radius="999px",
                        width="fit-content",
                    ),
                ),
                style=Style(padding="0.85rem 0", border_bottom="1px solid " + COLORS["border"], align_items="center"),
            )
        )

    return ps.Column(
        ps.Row(
            ps.Text("Recent Orders", style=Style(font_size="1rem", font_weight="700", color=COLORS["text"])),
            ps.Button(
                "View all",
                style=Style(
                    font_size="0.8rem",
                    font_weight="600",
                    color=COLORS["primary"],
                    background_color="transparent",
                    border="none",
                    cursor="pointer",
                ),
            ),
            style=Style(justify_content="space-between", align_items="center", margin_bottom="0.5rem"),
        ),
        ps.Column(*body_rows),
        style=card_style(),
    )


# ============================================================
# Page assembly
# ============================================================

def build_main_content():
    return ps.Column(
        build_topbar(),
        build_stats_row(),
        ps.Row(
            build_fake_bar_chart(),
            build_activity_feed(),
            style=Style(gap="1.25rem", margin_bottom="1.75rem", align_items="stretch", flex_wrap="wrap"),
        ),
        build_table(),
        style=Style(
            flex="1",
            padding="2rem 2.5rem",
            box_sizing="border-box",
            min_width="0",
        ),
    )


def get_app():
    return ps.Row(
        build_sidebar(),
        build_main_content(),
        style=Style(
            width="100%",
            min_height="100vh",
            background_color=COLORS["bg"],
            font_family=FONT,
            box_sizing="border-box",
        ),
    )


if __name__ == "__main__":
    app = get_app()
    ps.run(
        app,
        title="MyDash — Modern PyLage Dashboard",
        serve=True,
        host="127.0.0.1",
        port=8090,
        open_browser=True,
    )