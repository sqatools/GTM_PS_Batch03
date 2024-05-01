from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.,'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button').click()
