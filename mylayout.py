"""
mylayout.py — pylage_layout Skeleton Demo (Live Demo)

Run directly:
    python mylayout.py

Purpose of this file:
    Unlike mydash.py (which hand-built every Row/Column manually),
    this demo's STRUCTURE comes from `pylage_layout` — the layout
    skeleton package:

        pylage_layout.layouts   → AppShell, Navbar, Container, Stack,
                                   TwoColumn, ThreeColumn, Footer
        pylage_layout.patterns  → Hero, StatsSection, FeatureSection,
                                   CTA, Testimonial, FAQ

    `pylage` core (Style, State, Button, Text, ...) is only used for
    small leaf content and styling — never for building the page
    skeleton itself. That's the point of pylage_layout: you compose
    pages from ready-made structural blocks instead of hand-rolling
    Row/Column trees every time.
"""

import pylage as ps
from pylage import Style, State

from pylage_layout.layouts import (
    AppShell,
    Container,
    Stack,
    TwoColumn,
    ThreeColumn,
    Footer,
    Navbar,
)
from pylage_layout.patterns import (
    Hero,
    StatsSection,
    FeatureSection,
    CTA,
    Testimonial,
    FAQ,
)


# ============================================================
# Shared design tokens
# ============================================================

COLORS = {
    "bg": "#f4f6fb",
    "surface": "#ffffff",
    "border": "#e5e9f2",
    "text": "#0f172a",
    "text_muted": "#64748b",
    "primary": "#4f46e5",
    "primary_soft": "#eef2ff",
}

FONT = "'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"

CARD_STYLE = Style(
    background_color=COLORS["surface"],
    border="1px solid " + COLORS["border"],
    border_radius="1rem",
    box_shadow="0 1px 3px rgba(15, 23, 42, 0.06), 0 1px 2px rgba(15, 23, 42, 0.04)",
    box_sizing="border-box",
    padding="1.5rem",
)


# ============================================================
# State — which "page" is active, purely to show the skeleton
# stays reactive even though the layout comes from pylage_layout
# ============================================================

active_page = State("Home")


# ============================================================
# 1) Navbar — pylage_layout.layouts.Navbar (skeleton, not manual)
# ============================================================

def build_navbar():
    def go(name):
        def handler(e=None):
            active_page.set(name)
        return handler

    return Navbar(
        ps.Text(
            "⚡ MyLayout",
            style=Style(color="#ffffff", font_size="1.2rem", font_weight="800"),
        ),
        ps.Row(
            ps.Button("Home", on_click=go("Home"), style=Style(
                background_color="transparent", border="none", color="#ffffff",
                font_weight="600", cursor="pointer", padding="0.5rem 0.9rem",
            )),
            ps.Button("Features", on_click=go("Features"), style=Style(
                background_color="transparent", border="none", color="rgba(255,255,255,0.85)",
                font_weight="600", cursor="pointer", padding="0.5rem 0.9rem",
            )),
            ps.Button("Testimonials", on_click=go("Testimonials"), style=Style(
                background_color="transparent", border="none", color="rgba(255,255,255,0.85)",
                font_weight="600", cursor="pointer", padding="0.5rem 0.9rem",
            )),
            ps.Button("FAQ", on_click=go("FAQ"), style=Style(
                background_color="transparent", border="none", color="rgba(255,255,255,0.85)",
                font_weight="600", cursor="pointer", padding="0.5rem 0.9rem",
            )),
            style=Style(gap="0.25rem"),
        ),
        style=Style(
            background=f"linear-gradient(90deg, {COLORS['primary']} 0%, #4338ca 100%)",
            padding="1rem 2rem",
            display="flex",
            align_items="center",
            justify_content="space-between",
            width="100%",
            box_sizing="border-box",
        ),
    )


# ============================================================
# 2) Page sections — built from pylage_layout.patterns
# ============================================================

def build_hero_section():
    return Hero(
        title="Ship pages faster with pylage_layout",
        description=(
            "AppShell, Navbar, Container, Stack, TwoColumn/ThreeColumn and "
            "reusable patterns like Hero, StatsSection and CTA — compose a "
            "full page skeleton without hand-rolling Row/Column trees."
        ),
        actions=["Get Started", "View Docs"],
        style=Style(
            padding="3rem 2rem",
            background_color=COLORS["primary_soft"],
            border_radius="1.25rem",
            text_align="center",
        ),
    )


def build_stats_section():
    return StatsSection(
        title="Trusted at scale",
        description="Numbers from teams already shipping with pylage_layout.",
        stats=[
            {"label": "Active Users", "value": "12.8K", "description": "+18.4% this month"},
            {"label": "Pages Shipped", "value": "3,204", "description": "Across 240 projects"},
            {"label": "Avg. Build Time", "value": "6 min", "description": "From skeleton to live"},
            {"label": "Uptime", "value": "99.98%", "description": "Last 90 days"},
        ],
        style=Style(padding="2rem"),
    )


def build_features_section():
    return FeatureSection(
        {
            "icon": "layout",
            "title": "AppShell Skeleton",
            "description": "Header, sidebar, content, and footer slots ready out of the box.",
        },
        {
            "icon": "grid",
            "title": "TwoColumn / ThreeColumn",
            "description": "Responsive multi-column rows without manual flex/grid wiring.",
        },
        {
            "icon": "package",
            "title": "Reusable Patterns",
            "description": "Hero, StatsSection, CTA, Testimonial, FAQ — drop in and customize.",
        },
        title="Everything the skeleton gives you",
        description="pylage_layout composes the structure; you only supply content.",
        class_name="features-grid",
    )


def build_testimonials_section():
    # ThreeColumn is a pylage_layout skeleton primitive — used here to
    # lay out three Testimonial pattern cards side by side.
    return Container(
        ps.Heading(
            "What builders say",
            style=Style(font_size="1.5rem", font_weight="800", color=COLORS["text"], margin_bottom="1rem"),
        ),
        ThreeColumn(
            Testimonial(
                quote="AppShell + Container cut our dashboard setup time in half.",
                author="Meera Iyer",
                role="Frontend Lead",
            ),
            Testimonial(
                quote="TwoColumn and Stack meant zero manual flex debugging.",
                author="Dev Raghavan",
                role="Solo Founder",
            ),
            Testimonial(
                quote="The pattern library made our marketing page consistent instantly.",
                author="Ananya Sharma",
                role="Product Designer",
            ),
            style=Style(gap="1.25rem"),
        ),
    )


def build_faq_section():
    return FAQ(
        title="Frequently Asked Questions",
        items=[
            (
                "What does pylage_layout actually give me?",
                "Structural primitives (AppShell, Container, Stack, TwoColumn, "
                "ThreeColumn, Navbar, Footer) plus ready content patterns "
                "(Hero, StatsSection, FeatureSection, CTA, Testimonial, FAQ).",
            ),
            (
                "Can I still use plain pylage components inside it?",
                "Yes — the skeleton just arranges structure; any pylage "
                "component (Button, Text, Card, ...) can be placed inside.",
            ),
            (
                "Is it responsive by default?",
                "Layout primitives like Stack/TwoColumn/ThreeColumn use "
                "ResponsiveStyle internally, so they adapt at md/lg breakpoints.",
            ),
        ],
        style=Style(padding="1.5rem", background_color=COLORS["surface"], border_radius="1rem", border="1px solid " + COLORS["border"]),
    )


def build_cta_section():
    return CTA(
        title="Ready to build your own skeleton?",
        description="Swap the patterns, keep the structure — that's the whole idea.",
        actions=[
            ps.Button(
                "Start With AppShell",
                style=Style(
                    background_color=COLORS["primary"],
                    color="#ffffff",
                    padding="0.75rem 1.5rem",
                    border="none",
                    border_radius="0.6rem",
                    font_weight="700",
                    cursor="pointer",
                ),
            ),
        ],
        style=Style(
            padding="2.5rem",
            background_color=COLORS["text"],
            color="#ffffff",
            border_radius="1.25rem",
            text_align="center",
        ),
    )


# ============================================================
# 3) Content router — swaps which patterns are shown, but the
#    outer skeleton (AppShell/Container/Stack) never changes.
# ============================================================

def build_page_body():
    page = active_page.value

    if page == "Features":
        sections = [build_features_section()]
    elif page == "Testimonials":
        sections = [build_testimonials_section()]
    elif page == "FAQ":
        sections = [build_faq_section()]
    else:  # "Home"
        sections = [
            build_hero_section(),
            build_stats_section(),
            build_features_section(),
            build_cta_section(),
        ]

    # Container + Stack are pylage_layout skeleton primitives —
    # they handle max-width centering and responsive vertical spacing.
    # NOTE: Container() defaults to a ResponsiveStyle (with @media blocks)
    # when no style is given. pylage's current HTMLRenderer dumps that
    # entire CSS string — @media syntax included — directly into the
    # element's inline style="" attribute, which is invalid HTML/CSS and
    # silently breaks the responsive behavior in the browser. Since this
    # single-column page doesn't need Container's row/column breakpoint
    # switch anyway, we pass a plain Style() to avoid emitting that
    # invalid inline CSS.
    return Container(
        Stack(*sections, style=Style(gap="2rem", padding="2.5rem 1rem")),
        style=Style(width="100%", box_sizing="border-box"),
    )


# ============================================================
# 4) Footer — pylage_layout.layouts.Footer
# ============================================================

def build_footer():
    return Footer(
        ps.Text(
            "© 2026 MyLayout — built with pylage_layout skeleton primitives.",
            style=Style(color=COLORS["text_muted"], font_size="0.85rem"),
        ),
        style=Style(
            width="100%",
            padding="1.5rem 2rem",
            background_color=COLORS["surface"],
            border_top="1px solid " + COLORS["border"],
            display="flex",
            justify_content="center",
        ),
    )


# ============================================================
# 5) Assemble the whole page with AppShell — the top-level
#    pylage_layout skeleton primitive that owns header/content/footer.
# ============================================================

def get_app():
    content_holder = build_page_body()

    def rebuild_content(e=None):
        # AppShell's body is just a Row(sidebar_children, content_children);
        # we only need to refresh the content slot's children in place.
        content_holder.set_children(*build_page_body().children)

    # Re-render content whenever the active page changes.
    active_page.subscribe(lambda old, new: rebuild_content())

    return AppShell(
        header=build_navbar(),
        content=content_holder,
        footer=build_footer(),
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
        title="MyLayout — pylage_layout Skeleton Demo",
        serve=True,
        host="127.0.0.1",
        port=8091,
        open_browser=True,
    )