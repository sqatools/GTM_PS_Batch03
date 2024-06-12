from base.SeleniumBase import SeleniumBase
from .login_page_locators import *

class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)


    def enter_value_to_email_field(self, search_value):
        self.enter_value(search_value, user_name_locator)

    def enter_value_to_password_field(self, search_value):
        self.enter_value(search_value, pass_word_locator)

    def click_submit_btn(self):
        self.click_element(login_btn_locator)

    def invalid_email_message(self):
        element =self.get_element(invalid_email_locator)
        return element

    def invalid_password_message(self):
        element =self.get_element(invalid_password_locator)
        return element

    def success_message(self):
        element =self.get_element(invalid_password_locator)
        return element



