from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginClass:
    textbox_email_id= 'Email'
    textbox_password_id = 'Password'
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email1):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(email1)

    def setPassword(self, password1):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password1)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

