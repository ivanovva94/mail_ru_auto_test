from page.base_page import BasePage
from utils.locators import *


class LoginPage(BasePage):
    def __init__(self, browser):
        self.locator = LoginPageLocators
        super().__init__(browser)

    def click_enter_button(self):
        self.find_element(*self.locator.MAIL_ENTER_BUTTON).click()

        iframe = self.find_element(*self.locator.IFRAME)
        self.browser.switch_to.frame(iframe)

    def enter_email(self, login):
        login_field = self.wait_element_clickable(*self.locator.LOGIN_FIELD)
        login_field.send_keys(login)

        self.find_element(*self.locator.LOGIN_ENTER_BUTTON).click()

    def enter_password(self, password):
        password_field = self.wait_element_clickable(*self.locator.PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.PASSWORD_ENTER_BUTTON).click()
        self.browser.switch_to.default_content()

    def login_user(self, login, password):
        pass

    def check_authorized_user(self, login):
        account_check = self.wait_element(*self.locator.ICON_USER_ACCOUNT).get_attribute("aria-label")
        assert account_check == login + "@mail.ru", "Пользователь не авторизован"

    def exit_from_account(self):
        self.find_element(*self.locator.ICON_USER_ACCOUNT).click()
        self.wait_element_clickable(*self.locator.EXIT_BUTTON).click()

    def check_exit(self):
        self.wait_element(*self.locator.MAIL_ENTER_BUTTON)
        assert self.is_element_present(*self.locator.MAIL_ENTER_BUTTON)
