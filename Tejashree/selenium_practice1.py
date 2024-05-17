from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.select import Select
import time
from datetime import datetime



driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH, "//input[@name='firstname'][1]").send_keys("Mumbai")
driver.find_element(By.XPATH, "//input[@name='firstname'][2]").send_keys("Pune")

from_city_element = driver.find_element(By.ID, "female")
from_city_element.send_keys("female")


time.sleep(10)
driver.close()



