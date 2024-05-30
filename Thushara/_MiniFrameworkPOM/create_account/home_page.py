from SeleniumBase import SeleniumBase
from homepage_locators import *

class HomePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_sign_in(self):
        self.click_element(sign_in_locator)

    def click_create_account(self):
        self.click_element(create_account_locator)
