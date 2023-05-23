import time


def test_loc(browser_fixture):
    page = browser_fixture
    page.goto('https://textinput.antonzimaiev.repl.co/?')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()
    time.sleep(3)
