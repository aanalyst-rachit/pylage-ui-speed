from __future__ import annotations

from playwright.sync_api import expect, sync_playwright

import pylage as pl
from pylage.ENGINE.runtime import Runtime


def test_form_field_browser_render_and_interaction():
    email = pl.input(
        value="initial@example.com",
        placeholder="Email",
    )

    message = pl.textarea(
        value="Hello",
        rows=3,
    )

    app = pl.Stack(
        pl.form_field(
            email,
            label="Email",
            help_text="Use your work email.",
            error="Email is required.",
            required=True,
        ),
        pl.form_field(
            message,
            label="Message",
            help_text="Enter your message.",
        ),
    )

    runtime = Runtime(
        app,
        title="PyLage FormField Browser Test",
        output="test_output/form_field_browser/index.html",
    )

    try:
        url = runtime.start()

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            try:
                page.goto(url)

                assert page.locator("input").count() == 1
                assert page.locator("textarea").count() == 1

                body_text = page.locator("body").inner_text()

                assert "Email" in body_text
                assert "Use your work email." in body_text
                assert "Email is required." in body_text
                assert "Message" in body_text
                assert "Enter your message." in body_text
                assert "*" in body_text

                email_locator = page.locator("input").first
                expect(email_locator).to_have_value("initial@example.com")

                email_locator.fill("updated@example.com")
                expect(email_locator).to_have_value("updated@example.com")

                textarea_locator = page.locator("textarea").first
                expect(textarea_locator).to_have_value("Hello")

                textarea_locator.fill("Updated message")
                expect(textarea_locator).to_have_value("Updated message")

            finally:
                browser.close()

    finally:
        runtime.stop()
