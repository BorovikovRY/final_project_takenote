from pages.login_page import LoginPage
#Проверяет корректность открытия приложения TakeNote и наличие заголовка "TakeNote" в title страницы
def test_open_app(browser):
    browser.goto("https://takenote.dev/app")
    assert "TakeNote" in browser.title()
#Проверяет видимость кнопки Trash в интерфейсе
def test_trash_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('Trash')")
#Проверяет видимость кнопки Favorites
def test_favorites_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('Favorites')")
#Проверяет видимость кнопки Notes
def test_notes_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('Notes')")
#Проверяет видимость кнопки Scratchpad
def test_scratchpad_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('Scratchpad')")
#Проверяет видимость кнопки New Note
def test_new_note_button_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.is_visible("button:has-text('New Note')")
#Проверяет наличие и работоспособность поля поиска
def test_search_input_exists(browser):
    browser.goto("https://takenote.dev/app")
    search_input = browser.locator("input[placeholder='Search for notes']")
    assert search_input.is_visible()
    assert search_input.is_enabled()
#Проверяет видимость основного контен
def test_main_content_is_visible(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.locator("main").is_visible()
#Проверяет видимость иконки настроек
def test_settings_icon_exists(browser):
    browser.goto("https://takenote.dev/app")
    assert browser.locator("button >> nth=-1").is_visible()
#Проверяет работу кнопки обновления
def test_refresh_button(browser):
    browser.goto("https://takenote.dev/app")
    browser.locator("button >> nth=-2").click()  #  кнопка справа (обновить)
    assert browser.locator("body").is_visible()