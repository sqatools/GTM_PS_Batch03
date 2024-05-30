from base.SeleniumBase import SeleniumBase
from login_locators import *

class HomePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_sign_in(self):
        self.click_element(sign_in_locator)