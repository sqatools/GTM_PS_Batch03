from SeleniumBase import SeleniumCode
from Locators_page import *


class GooglePage(SeleniumCode):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def enter_value_to_search(self, search_value):
        self.enter_value(search_value, search_field_locator)  # Calling the SeleniumCode class method here

    def click_search_button(self):
        self.click_element(search_button_locator)    # Calling the SeleniumCode class method here
