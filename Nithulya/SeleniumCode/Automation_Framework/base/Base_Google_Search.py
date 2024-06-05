from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import logging

log = logging.getLogger(__name__)

class SeleniumBase1:
    def __init__(self,driver,timeout=25):
        self.driver = driver
        self.timeout1 = timeout
        self.wait =  WebDriverWait(self.driver, self.timeout1)
    def getElement(self,locator):
        try:
            log.info(f"finding element:{locator}")
            element1 = self.wait.until(EC.visibility_of_element_located(locator))
            return element1
        except Exception as e :
            self.driver.save_screenshot("locator_file.png")
            raise

    def clickElement(self,locator):
        log.info(f"click to element :{locator}")
        element2 = self.getElement(locator)
        element2.click()
    def enterValue(self,data,locator):
        element3 = self.getElement(locator)
        element3.send_keys(data)




