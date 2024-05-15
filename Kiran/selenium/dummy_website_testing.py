import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from _datetime import datetime
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

def choosing_option():
    opt=driver.find_elements(By.XPATH,"//li/input[@type='radio']")
    for ele in opt:
        ele.click()
choosing_option()
driver.find_element(By.XPATH,"//input[@name='firstname'][1]").send_keys("KIRAN")
driver.find_element(By.XPATH,"//input[@name='firstname'][2]").send_keys("YADAV")
driver.find_element(By.XPATH,"//input[@id='birthday']").send_keys("01-04-2000")
driver.find_element(By.XPATH,"//input[@id='female']").click()
time.sleep(10)
driver.close()
