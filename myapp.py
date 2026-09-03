import threading
import time
from pathlib import Path
import webview

from app import (
    button_manual,
    card_manual,
    form_manual,
    grid_manual,
    input_manual,
    heading_manual,
    text_manual,
    row_manual,
    column_manual,
    media_manual,
    switch_manual,
    select_manual,
    modern_button_manual,
    nav_interaction_manual,
    data_feedback_manual,
    table_manual,
    accordion_manual,
    carousel_manual,
    dialog_manual,
    drawer_manual,
    tabs_manual,
    datepicker_manual,
    popover_tooltip_manual,
    pagination_manual,
    avatar_badge_divider_manual,
    audio_video_canvas_manual,
    slider_radio_checkbox_manual,
    menu_breadcrumbs_pagination_manual,
    patterns_manual,
    templates_manual,
    layout_primitives_manual,
    themes_tokens_manual,
    manual_overview,
    ui_kit_button_manual,
    ui_kit_card_manual,
    ui_kit_text_manual,
    ui_kit_badge_manual,
    ui_kit_avatar_manual,
    ui_kit_divider_manual,
    ui_kit_metric_manual,
    ui_kit_trend_manual,
    ui_kit_table_manual,
   ui_kit_dataframe_manual,
)

from pylage import run

overview_app = ui_kit_dataframe_manual.get_app()

def start_pylage():
    run(
        overview_app,
        title="PyLage Component & Layout Manual",
        output=Path("index.html"),
        serve=True,
        host="127.0.0.1",
        port=8081,
        open_browser=False,  # Browser auto-open off rakha hai kyunki Webview use ho raha hai
    )


if __name__ == "__main__":
    # 1. Background thread me PyLage server start karein
    server_thread = threading.Thread(target=start_pylage, daemon=True)
    server_thread.start()

    # Server initialize hone ke liye 1 second ka delay
    time.sleep(1)

    # 2. PyWebview Window open karein
    webview.create_window(
        "PyLage Component & Layout Manual",
        "http://127.0.0.1:8081",
        width=1200,        height=800,
    )

    # 3. GUI Start karein (Directly Qt engine target kiya hai)
    webview.start(gui="qt")