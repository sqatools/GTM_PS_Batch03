import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"),
time.sleep(5)
driver.find_element(By.XPATH, "//input[@value='radio_123']").click()
driver.find_element(By.XPATH, "//input[@id='firstname'][1]").send_keys("Abc")
