"""
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com/")

username = driver.find_element(By.XPATH, "//input[@data-testid='royal_email']")
username.send_keys("testuser@gmail.com")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("Admin@12345")
login_button = driver.find_element(By.XPATH, "//button[@data-testid='royal_login_button']")
login_button.click()
#create_account = driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']")
#create_account.click()

incorrect_msg = driver.find_element(By.XPATH, """//div[text()="The password that you've entered is incorrect. "]""")
print(incorrect_msg.text)
assert "incorrect" in incorrect_msg.text


time.sleep(10)
driver.close()


