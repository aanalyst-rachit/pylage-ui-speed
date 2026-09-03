import pylage_ui as ps


def test_ui_kit_import():
    assert ps.IMPORT_NAME == "pylage_ui"


def test_ui_kit_package_name():
    assert ps.PACKAGE_NAME == "pylage-ui-kit"


def test_ui_kit_version():
    assert ps.__version__ == "0.1.0"


def test_ui_kit_public_api():
    assert ps.__all__ == [
        "IMPORT_NAME",
        "PACKAGE_NAME",
        "__version__",
        "avatar",
        "badge",
        "button",
        "card",
        "dashboard",
        "dashboard_card",
        "dashboard_grid",
        "dashboard_header",
        "dashboard_section",
        "dataframe",
        "data_list",
        "divider",
        "empty_state",
        "error_state",
        "heading",
        "loading_state",
        "metric",
        "metric_grid",
        "stat_group",
        "table",
        "text",
        "trend",
    ]
