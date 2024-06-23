import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_chrome():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Signin
    assert driver.title == "OrangeHRM"


def test_login_edge():
    opt = webdriver.EdgeOptions()
    opt.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=opt)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Signin
    assert driver.title == "OrangeHRM"


def test_login_firefox():
    opt = webdriver.FirefoxOptions()
    opt.add_experimental_option("detach", True)
    driver = webdriver.Firefox(options=opt)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Signin
    assert driver.title == "OrangeHRM"

