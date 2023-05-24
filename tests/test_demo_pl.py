from playwright.sync_api import expect


def test_demo_playwright(browser_fixture):
    page = browser_fixture
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
