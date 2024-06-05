from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

import logging

log = logging.getLogger(__name__)



class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.actions = ActionChains(self.driver)

    def get_element(self,locator):
        try:
            log.info(f"finding element {locator}")
            element = self.wait.until(ec.visibility_of_element_located(locator))
            return element
        except Exception as e:
            self.driver.save_screenshot("locator_file.png")
            raise

    def click_element(self,locator):
        element = self.get_element(locator)
        element.click()

    def enter_value(self,data,locator):
        element = self.get_element(locator)
        element.send_keys(data)

    def select_dropdown_value(self, value, locator):
        element = self.get_element(locator)
        obj = Select(element)
        obj.select_by_visible_text(value)

    def assert_message_displayed(self,locator):
        self.get_element(locator)

    def move_to_third_element(self,l1, l2, l3):
        self.actions.move_to_element(l1).move_to_element(l2).move_to_element(l3).click().perform()

    """
    def move_to_third_element(self,l,l1,l2,l3):
        self.click_element(l)
        self.actions.move_to_element(l1).move_to_element(l2).move_to_element(l3).click().perform()

    """
