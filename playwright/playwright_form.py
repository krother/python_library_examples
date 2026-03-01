
from playwright.sync_api import Playwright, sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # type query into a search engine
    page.goto("https://www.ecosia.org/")
    page.locator("[data-test-id=\"search-form-input\"]").click()
    page.locator("[data-test-id=\"search-form-input\"]").fill("Hunter und Crohn")
    page.locator("[data-test-id=\"search-form-input\"]").press("Enter")

    # click on a search result
    page.get_by_role("link", name="Hunter & Friends - Webshop").click()

    # visit the target page
    page.get_by_text("Willkommen im Hunter & Friends Webshop").click()
    page.locator("#MainContent").press("Control+c")

    heading = page.get_by_text("Willkommen im")

    # assertion
    expect(heading).to_contain_text("Willkommen im Hunter & Friends Webshop")

    context.close()
    browser.close()
