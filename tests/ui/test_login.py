from pages.login_page import LoginPage

def test_open_app(browser):
    browser.goto("https://takenote.dev/app")
    assert "TakeNote" in browser.title()

def test_trash_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('Trash')")

def test_favorites_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('Favorites')")

def test_notes_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('Notes')")

def test_scratchpad_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('Scratchpad')")

def test_new_note_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('New Note')")

def test_search_input_exists(browser):
    browser.goto("https://takenote.dev/app")
    search_input = browser.locator("input[placeholder='Search for notes']")
    assert search_input.is_visible()
    assert search_input.is_enabled()

def test_main_content_is_visible(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.locator("main").is_visible()

def test_settings_icon_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.locator("button >> nth=-1").is_visible()

def test_refresh_button(browser):
    browser.goto("https://takenote.dev/app")
    browser.locator("button >> nth=-2").click()  # Вторая кнопка справа (обновить)
    assert browser.locator("body").is_visible()