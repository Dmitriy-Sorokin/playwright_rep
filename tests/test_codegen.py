from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(browser_fixture) -> None:
    page = browser_fixture
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Exsample")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("link", name="Completed").click()
    page.get_by_text("All Active Completed").click()
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("new")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_text("All Active Completed").click()


'''
Что бы запустить браузер с поиском лакаторов пише  [laywright codegen нужный адрес сайта]  
'''
