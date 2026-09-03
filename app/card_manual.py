import sys
from pathlib import Path

# Project root setup
from pylage.ENGINE import Button, Card, Column, Heading, State, Text
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
from pylage.ENGINE import Style

def get_app():
    # Dynamic States for Interactivity
    click_count = State(0)
    card_status = State("Status: Idle")

    def handle_card_click():
        new_count = click_count.value + 1
        click_count.set(new_count)
        card_status.set(f"⚡ Interactive Card Clicked! Total: {new_count}")

    # ============================================================
    # 1. BASIC CARD
    # ============================================================
    basic_card = Card(
        Text("Minimal Card", style=Style(font_weight="700")),
        Text("Ye simple content container card hai.", style=Style(color="#64748b")),
        style=Style(
            background_color="#ffffff",
            padding="1.25rem",
            border_radius="0.5rem",
            border="1px solid #e2e8f0",
            margin_bottom="1.5rem",
        ),
    )

    # ============================================================
    # 2. ELEVATED CARD (Shadow & Custom Border)
    # ============================================================
    elevated_card = Card(
        Heading("Elevated Card", style=Style(font_size="1.25rem", color="#0f172a")),
        Text(
            "Box-shadow, custom border aur rounded corners prop customisation.",
            style=Style(color="#475569", margin_top="0.5rem"),
        ),
        style=Style(
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="1rem",
            box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1)",
            border="1px solid #cbd5e1",
            margin_bottom="1.5rem",
        ),
    )

    # ============================================================
    # 3. INTERACTIVE / CLICKABLE CARD
    # ============================================================
    interactive_card = Card(
        Heading("Interactive Card (Click Me)", style=Style(font_size="1.25rem", color="#2563eb")),
        Text("Click handling & dynamic state update demo.", style=Style(color="#64748b", margin_top="0.25rem")),
        Heading(click_count, style=Style(color="#166534", margin_top="1rem")),
        on_click=handle_card_click,
        style=Style(
            background_color="#eff6ff",
            padding="1.5rem",
            border_radius="0.75rem",
            border="2px dashed #2563eb",
            cursor="pointer",
            margin_bottom="1.5rem",
        ),
    )

    # ============================================================
    # 4. FULL COMPOSED CARD (Header, Body, Footer)
    # ============================================================
    composed_card = Card(
        # Card Header
        Column(
            Heading("Product Analytics", style=Style(font_size="1.25rem", color="#0f172a")),
            Text("Monthly subscription overview", style=Style(color="#64748b", font_size="0.875rem")),
            style=Style(margin_bottom="1rem"),
        ),
        # Card Body (Fixed Style without border_top/border_bottom)
        Column(
            Text("Active Users: 1,240", style=Style(font_weight="600", color="#166534")),
            Text("Revenue: $4,500", style=Style(font_weight="600", color="#2563eb")),
            style=Style(
                padding="1rem 0",
                border="1px solid #e2e8f0"
            ),
        ),
        # Card Footer Action
        Button(
            "View Full Report",
            style=Style(
                background_color="#0f172a",
                color="#ffffff",
                padding="0.5rem 1rem",
                border_radius="0.375rem",
                margin_top="1rem",
                cursor="pointer",
            ),
        ),
        style=Style(
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.75rem",
            border="1px solid #e2e8f0",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.05)",
            margin_bottom="1.5rem",
        ),
    )

    return Column(
        Heading(
            "PyLage Card — Live Manual",
            style=Style(font_size="1.75rem", font_weight="700", color="#0f172a", margin_bottom="0.5rem"),
        ),
        Text(
            "Card component ke alag-alag variations aur interactive event handling test karein:",
            style=Style(color="#64748b", margin_bottom="1.5rem"),
        ),

        Text(card_status, style=Style(color="#166534", font_weight="600", margin_bottom="1rem")),

        Text("1. Basic Card", style=Style(font_weight="700", margin_bottom="0.5rem")),
        basic_card,

        Text("2. Elevated Card", style=Style(font_weight="700", margin_bottom="0.5rem")),
        elevated_card,

        Text("3. Interactive Card", style=Style(font_weight="700", margin_bottom="0.5rem")),
        interactive_card,

        Text("4. Composed Card", style=Style(font_weight="700", margin_bottom="0.5rem")),
        composed_card,

        style=Style(
            width="100%",
            max_width="700px",
            min_height="100vh",
            padding="2rem",
            background_color="#f8fafc",
            box_sizing="border-box",
        ),
    )
