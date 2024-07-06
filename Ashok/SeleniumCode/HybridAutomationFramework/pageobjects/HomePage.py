from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    # locators
    lnk_myaccount_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/a/span"
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # action methods
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
