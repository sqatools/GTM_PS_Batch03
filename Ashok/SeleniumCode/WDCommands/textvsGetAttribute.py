"""
text -----> returns inner text of the element
get_attribute() ----> returns values of any attribute of web element

<input id='123"  name="xyz"> Email: </input>      ---> Email is inner text
Both text, get_attribute will access by web-element not driver instance
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

emailbox = driver.find_element(By.XPATH, "//input[@id='Email']")
emailbox.clear()
time.sleep(2)
emailbox.send_keys("abc@gmail.com")
time.sleep(2)
print("Result of email box:", emailbox.text)
print("Result of emailbox:", emailbox.get_attribute('value'))







