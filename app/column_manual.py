import sys
from pathlib import Path

# Project root setup
from pylage.ENGINE import Button, Column, Heading, Row, State, Text
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pylage as ps
from pylage.ENGINE import Style

def get_app():
    # Dynamic State for Column Interactivity Demo
    item_count = State(2)

    def add_item():
        item_count.set(item_count.value + 1)

    def reset_items():
        item_count.set(2)

    # Helper function for dynamic item blocks
    def create_block(text, bg_color="#2563eb", width="100%"):
        return Column(
            Text(text, style=Style(color="#ffffff", font_weight="700")),
            style=Style(
                background_color=bg_color,
                width=width,
                padding="0.75rem 1rem",
                border_radius="0.375rem",
            ),
        )

    # ============================================================
    # 1. BASIC COLUMN WITH GAP
    # ============================================================
    basic_column = Column(
        create_block("Stacked Block 1", "#2563eb"),
        create_block("Stacked Block 2", "#7c3aed"),
        create_block("Stacked Block 3", "#dc2626"),
        style=Style(
            gap="0.75rem",
            padding="1rem",
            background_color="#ffffff",
            border="1px solid #e2e8f0",
            border_radius="0.5rem",
            margin_bottom="1.5rem",
        ),
    )

    # ============================================================
    # 2. ALIGN ITEMS (Horizontal Alignment in Vertical Column)
    # ============================================================
    align_column = Column(
        create_block("Start Aligned", "#059669", width="40%"),
        create_block("Center Aligned", "#d97706", width="50%"),
        create_block("End Aligned", "#2563eb", width="40%"),
        style=Style(
            align_items="center",  # Centers all child blocks horizontally
            gap="0.75rem",
            padding="1rem",
            background_color="#ffffff",
            border="1px solid #e2e8f0",
            border_radius="0.5rem",
            margin_bottom="1.5rem",
        ),
    )

    # ============================================================
    # 3. JUSTIFY CONTENT (Vertical Distribution inside Fixed Height)
    # ============================================================
    justify_column = Column(
        create_block("Top Block", "#7c3aed"),
        create_block("Bottom Block", "#059669"),
        style=Style(
            justify_content="space-between",
            height="180px",
            padding="1rem",
            background_color="#ffffff",
            border="1px solid #e2e8f0",
            border_radius="0.5rem",
            margin_bottom="1.5rem",
        ),
    )

    # ============================================================
    # 4. SCROLLABLE COLUMN CONTAINER
    # ============================================================
    scroll_column = Column(
        create_block("Scrollable Item 1", "#475569"),
        create_block("Scrollable Item 2", "#475569"),
        create_block("Scrollable Item 3", "#475569"),
        create_block("Scrollable Item 4", "#475569"),
        create_block("Scrollable Item 5", "#475569"),
        style=Style(
            gap="0.5rem",
            height="140px",
            overflow="auto",
            padding="1rem",
            background_color="#ffffff",
            border="1px solid #cbd5e1",
            border_radius="0.5rem",
            margin_bottom="1.5rem",
        ),
    )

    # ============================================================
    # 5. INTERACTIVE COLUMN (Dynamic Content Stacking)
    # ============================================================
    interactive_column = Column(
        Row(
            Button("Add Stack Item", on_click=add_item, style=Style(padding="0.5rem 1rem", cursor="pointer")),
            Button("Reset", on_click=reset_items, style=Style(padding="0.5rem 1rem", cursor="pointer")),
            style=Style(gap="0.75rem", margin_bottom="1rem"),
        ),
        Row(
            Text("Current Items Stacked: ", style=Style(font_weight="600")),
            Heading(item_count, style=Style(color="#2563eb", font_size="1rem")),
            style=Style(align_items="center", gap="0.5rem"),
        ),
        style=Style(
            gap="0.5rem",
            padding="1rem",
            background_color="#eff6ff",
            border="1px dashed #2563eb",
            border_radius="0.5rem",
            margin_bottom="1.5rem",
        ),
    )

    return Column(
        Heading(
            "PyLage Column — Live Manual",
            style=Style(font_size="1.75rem", font_weight="700", color="#0f172a", margin_bottom="0.5rem"),
        ),
        Text(
            "Column layout component ke vertical stacking, alignment, aur scrollable features test karein:",
            style=Style(color="#64748b", margin_bottom="1.5rem"),
        ),

        Text("1. Basic Vertical Stacking (With Gap)", style=Style(font_weight="700", margin_bottom="0.5rem")),
        basic_column,

        Text("2. Horizontal Alignment (Align Items Center)", style=Style(font_weight="700", margin_bottom="0.5rem")),
        align_column,

        Text("3. Vertical Distribution (Justify Space-Between)", style=Style(font_weight="700", margin_bottom="0.5rem")),
        justify_column,

        Text("4. Fixed Height Scrollable Column", style=Style(font_weight="700", margin_bottom="0.5rem")),
        scroll_column,

        Text("5. Interactive Column State Update", style=Style(font_weight="700", margin_bottom="0.5rem")),
        interactive_column,

        style=Style(
            width="100%",
            max_width="750px",
            min_height="100vh",
            padding="2rem",
            background_color="#f8fafc",
            box_sizing="border-box",
        ),
    )
