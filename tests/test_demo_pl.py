import time

from playwright.sync_api import expect


def test_demo_playwright(browser_fixture):
    page = browser_fixture
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    todo_exam = page.locator(".new-todo")
    expect(todo_exam).to_be_empty()
    todo_exam.type("One")
    todo_exam.press("Enter")
    todo_exam.type("two")
    todo_exam.press("Enter")
    task = page.locator(".todo-list li")
    expect(task).to_have_count(2)
    checkboxes = page.locator("[type=checkbox]")
    # page.pause()  # ДЭбагер
    checkboxes.nth(1).check()
    expect(task.nth(0)).to_have_class("completed")
    time.sleep(3)
