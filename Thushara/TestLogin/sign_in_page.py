from SeleniumBase import SeleniumBase
from login_locators import *

class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def enter_value_to_email_field(self, search_value):
        self.enter_value(search_value, email_field_locator)

    def enter_value_to_password_field(self, search_value):
        self.enter_value(search_value, password_field_locator)

    def click_sign_in_button(self,):
        self.click_element(sign_in_button_locator)

    def invalid_email_message(self):
        self.get_element(invalid_email_password_error_message_locator)

    def invalid_password_message(self):
        self.get_element(invalid_email_password_error_message_locator)