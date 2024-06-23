import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClass:

    @pytest.mark.parametrize('uname, pwd',
                             [("Admin", "admin123"), ("adm", "admin123"), ("Admin", "adm"), ("adm", "adm")])
    def test_login(self, uname, pwd):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(2)
        self.driver.find_element(By.NAME, "username").send_keys(uname)
        self.driver.find_element(By.NAME, "password").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Signin
        assert self.driver.title == "OrangeHRM"
