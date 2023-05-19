from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
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

    # ---------------------
    context.close()
    browser.close()


'''
Что бы запустить браузер с поиском лакаторов пише  [laywright codegen нужный адрес сайта]  
'''
