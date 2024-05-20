from selenium import webdriver
from selenium.webdriver.common.by import By
from IgnoreFile.config import Username,Password
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
def getLogin():
    driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(Username)
    driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(Password)
    driver.find_element(By.CSS_SELECTOR, "button.oxd-button").click()
    time.sleep(2)

def getAdmin():
    driver.find_element(By.CSS_SELECTOR, 'span.oxd-text').click()
    time.sleep(2)
def addName():
    driver.find_element(By.CSS_SELECTOR, 'div>div>div>div>button.oxd-button[type = button]').click()
    time.sleep(2)


time.sleep(5)
getLogin()
getAdmin()
addName()

