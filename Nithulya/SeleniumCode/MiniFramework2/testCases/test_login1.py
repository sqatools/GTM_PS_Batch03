import pytest
from selenium import webdriver
from pageObjects1.LoginPage import LoginClass

class Test_001_Login:
    baseURL = 'https://admin-demo.nopcommerce.com/'
    email1= 'admin@yourstore.com'
    password1 = 'admin'
    def test_homepageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()


