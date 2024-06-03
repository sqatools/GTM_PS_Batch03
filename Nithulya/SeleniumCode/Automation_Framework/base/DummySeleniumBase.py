from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumBase1:
    def __init__(self,driver,timeout=25):
        self.driver = driver
        self.timeout1 = timeout
        self.wait =  WebDriverWait(self.driver, self.timeout1)
    def getElement(self,locator):
        element1 = self.wait.until(EC.visibility_of_element_located(locator))
        return element1
    def clickElement(self,locator):
        element2 = self.getElement(locator)
        element2.click()
    def enterValue(self,data,locator):
        element3 = self.getElement(locator)
        element3.send_keys(data)
    def select_dropdown_value(self, value, locator):
        element = self.getElement(locator)
        obj = Select(element)
        obj.select_by_visible_text(value)




