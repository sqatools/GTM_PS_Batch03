import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCLI:

    def test_Logo(self, setup):
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.status = self.driver.find_element(By.XPATH,
                                               "//img[@alt = 'company-branding']").is_displayed()
        self.driver.close()
        assert self.status == True

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(2)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Signin
        # time.sleep(1)
        # self.status = self.driver.find_element(By.XPATH,
        #                                        "//h6[normalize-space()='Dashboard']").is_displayed()
        # assert self.status == True
