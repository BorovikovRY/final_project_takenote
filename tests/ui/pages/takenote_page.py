class TakeNotePage:
    def __init__(self, browser):
        self.browser = browser

    def navigate(self):
        self.browser.goto("https://takenote.dev/app")
        return self

    @property
    def trash_button(self):
        return self.browser.locator("button:has-text('Trash')")

    @property
    def favorites_button(self):
        return self.browser.locator("button.app-sidebar-wrapper:has-text('Favorites')")

    @property
    def notes_button(self):
        return self.browser.locator("button.app-sidebar-wrapper:has-text('Notes')")

    @property
    def scratchpad_button(self):
        return self.browser.locator("button:has-text('Scratchpad')")

    @property
    def new_note_button(self):
        return self.browser.locator("button:has-text('New Note')")

    @property
    def search_input(self):
        return self.browser.locator("input[placeholder='Search for notes']")

    @property
    def main_content(self):
        return self.browser.locator("main")

    @property
    def settings_icon(self):
        return self.browser.locator("button >> nth=-1")  # "ЭТО КНОПКА  НАСТРОЙКИ "

    @property
    def refresh_button(self):
        return self.browser.locator("button >> nth=-2")  # ЭТО КНОПКА ОБНОВЛЕНИЕЕ

    def click_refresh(self):
        self.refresh_button.click()