from SeleniumBase import SeleniumBase
from locators import *

class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def enter_value_to_email_field(self, search_value):
        self.enter_value(search_value, email_field_locator)

    def enter_value_to_password_field(self, search_value):
        self.enter_value(search_value, password_field_locator)

    def click_sign_in_button(self,):
        self.click_element(sign_in_button_locator)

