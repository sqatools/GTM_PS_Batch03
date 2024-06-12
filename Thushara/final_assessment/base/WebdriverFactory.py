from selenium import webdriver
class WebdriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_driver_instance(self):
        driver = None
        if self.browser.lower().__eq__('chrome'):
            crm_option = webdriver.ChromeOptions()
            crm_option.add_experimental_option('detach',True)
            driver = webdriver.Chrome(options=crm_option)

        elif self.browser.lower().__eq__('firefox'):
            driver = webdriver.Firefox()

        elif self.browser.lower().__eq__('edge'):
            driver = webdriver.Edge()
        driver.maximize_window()
        return driver



