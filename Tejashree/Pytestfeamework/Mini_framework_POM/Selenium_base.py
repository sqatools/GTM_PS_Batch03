
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumBase:
    def __int__(self, timeout):
        self.timeout = timeout