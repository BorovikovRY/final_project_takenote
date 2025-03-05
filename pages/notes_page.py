from pages.base_page import BasePage

class NotesPage(BasePage):
    NEW_NOTE_BUTTON = "button:has-text('New Note')"
    NOTE_TITLE_INPUT = "input[placeholder='Title']"
    NOTE_BODY_INPUT = "textarea[placeholder='Start writing...']"
    DELETE_BUTTON = "button:has-text('Delete')"

    def create_note(self, title, body):
        self.page.click(self.NEW_NOTE_BUTTON)
        self.page.fill(self.NOTE_TITLE_INPUT, title)
        self.page.fill(self.NOTE_BODY_INPUT, body)

    def delete_note(self):
        self.page.click(self.DELETE_BUTTON)