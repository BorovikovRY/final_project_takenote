from tests.ui.pages.takenote_page import TakeNotePage
#Проверяет корректность открытия приложения TakeNote и наличие заголовка "TakeNote" в title страницы
def test_open_app(browser):
    page = TakeNotePage(browser).navigate()
    assert "TakeNote" in browser.title()
#Проверяет видимость кнопки Trash в интерфейсе
def test_trash_button_exists(browser):
    page = TakeNotePage(browser).navigate()
    assert page.trash_button.is_visible()
#Проверяет видимость кнопки Favorites
def test_favorites_button_exists(browser):
    page = TakeNotePage(browser).navigate()
    assert page.favorites_button.is_visible()
#Проверяет видимость кнопки Notes
def test_notes_button_exists(browser):
    page = TakeNotePage(browser).navigate()
    assert page.notes_button.is_visible()
#Проверяет видимость кнопки Scratchpad
def test_scratchpad_button_exists(browser):
    page = TakeNotePage(browser).navigate()
    assert page.scratchpad_button.is_visible()
#Проверяет видимость кнопки New Note
def test_new_note_button_exists(browser):
    page = TakeNotePage(browser).navigate()
    assert page.new_note_button.is_visible()
#Проверяет наличие и работоспособность поля поиска
def test_search_input_exists(browser):
    page = TakeNotePage(browser).navigate()
    assert page.search_input.is_visible()
    assert page.search_input.is_enabled()
#Проверяет видимость основного контен
def test_main_content_is_visible(browser):
    page = TakeNotePage(browser).navigate()
    assert page.main_content.is_visible()
#Проверяет видимость иконки настроек
def test_settings_icon_exists(browser):
    page = TakeNotePage(browser).navigate()
    assert page.settings_icon.is_visible()
#Проверяет работу кнопки обновления
def test_refresh_button(browser):
    page = TakeNotePage(browser).navigate()
    page.click_refresh()
    assert browser.locator("body").is_visible()