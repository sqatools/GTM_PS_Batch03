from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
driver.implicitly_wait(10)

element = driver.execute_script("return document.getElementById('fromcity')")
element.send_keys("Mumbai")
time.sleep(2)
driver.execute_script("return document.getElementById('oneway');")
time.sleep(6)
