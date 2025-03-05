from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_BUTTON = "button:has-text('Sign in with Google')"

    def click_login(self):
        self.page.click(self.LOGIN_BUTTON)