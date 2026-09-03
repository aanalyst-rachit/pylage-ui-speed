from __future__ import annotations

import csv
from pathlib import Path

from pylage.ENGINE import Column, Style, Text
from pylage import dataframe


def _load_test_csv():
    csv_path = Path(__file__).resolve().parents[1] / "test.csv"

    with csv_path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def get_app():
    rows = _load_test_csv()

    return Column(
        Text(
            "DataFrame",
            style=Style(
                font_size="2rem",
                font_weight="700",
                color="#0f172a",
                font_family="Inter, sans-serif",
            ),
        ),
        Text(
            "Excel-like data grid using the project's real test.csv dataset.",
            style=Style(
                color="#64748b",
                margin_bottom="1.5rem",
                font_family="Inter, sans-serif",
            ),
        ),
        Text(
            "Cell borders — default ON",
            style=Style(
                font_size="1.1rem",
                font_weight="600",
                color="#0f172a",
                font_family="Inter, sans-serif",
            ),
        ),
        dataframe(
            rows,
            title="test.csv — bordered grid",
            class_name="test-csv-grid",
        ),
        Text(
            "Cell borders — OFF",
            style=Style(
                font_size="1.1rem",
                font_weight="600",
                color="#0f172a",
                margin_top="1.5rem",
                font_family="Inter, sans-serif",
            ),
        ),
        dataframe(
            rows[:8],
            title="test.csv — no cell borders",
            cell_border=False,
            class_name="test-csv-grid-no-border",
        ),
        Text(
            "Verify: the outer DataFrame border remains visible while "
            "individual cell borders are disabled.",
            style=Style(
                color="#64748b",
                margin_top="1rem",
                font_size="0.875rem",
                font_family="Inter, sans-serif",
            ),
        ),
        style=Style(
            padding="2rem",
            max_width="1100px",
            margin="0 auto",
            font_family="Inter, sans-serif",
            display="flex",
            flex_direction="column",
            gap="0.75rem",
        ),
    )
