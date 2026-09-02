from __future__ import annotations

from pylage import Style
from pylage.core.renderer import render
from pylage_ui import dataframe


class FakeDataFrame:
    columns = ["Name", "Age"]

    def to_dict(self, orient="records"):
        assert orient == "records"
        return [
            {"Name": "Rachit", "Age": 24},
            {"Name": "Rahul", "Age": 25},
        ]


def test_ui_kit_dataframe_accepts_dataframe_like_object():
    html = render(dataframe(FakeDataFrame()))

    assert "<thead>" in html
    assert "<th>Name</th>" in html
    assert "<td>Rachit</td>" in html
    assert 'class="pylage-dataframe"' in html


def test_ui_kit_dataframe_accepts_headers_and_rows():
    html = render(
        dataframe(
            [[1, "Rachit"], [2, "Rahul"]],
            headers=["ID", "Name"],
        )
    )

    assert "<th>ID</th>" in html
    assert "<td>Rahul</td>" in html


def test_ui_kit_dataframe_merges_custom_style():
    html = render(
        dataframe(
            [{"Name": "Rachit"}],
            style=Style(width="80%"),
        )
    )

    assert "width:80%" in html
    assert "border:1px solid" in html


def test_ui_kit_dataframe_does_not_require_pandas():
    # The component itself must remain independent of pandas.
    html = render(
        dataframe(
            [
                {"Name": "Rachit", "Score": 95},
                {"Name": "Rahul", "Score": 91},
            ]
        )
    )

    assert "<th>Name</th>" in html
    assert "<td>91</td>" in html
