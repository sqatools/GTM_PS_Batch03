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
driver.find_element(By.XPATH, "//h1[@align='center']//following::input[@value='radio_123']").click()
from_city_element = driver.find_element(By.ID, "female")
from_city_element.send_keys("female")
time.sleep(10)
#driver.find_element(By.XPATH, "//h2[text()='Billing Details']//following::input[@id='billing_name']").send_keys("Tejashree")
driver.find_element(By.XPATH, "//input[@id='billing_name'and @type='text']").send_keys("tejashree")
driver.find_element(By.XPATH, "//input[@id='billing_phone'and @type='text']").send_keys("9445698034")
driver.find_element(By.XPATH, "//input[@id='billing_email'and @type='text]").send_keys("teju@gmail.com")
#driver.find_element(By.XPATH, "//input[@id='billing_address'and @type='text']").send_keys("Pune")
#driver.find_element(By.XPATH, "//select[@id='billing_country']").send_keys("India")



time.sleep(10)
driver.close()



