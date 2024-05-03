import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
"""
driver.get("https://www.google.com/")
search = driver.find_element(By.XPATH,"//textarea[@class='gLFyf']")
search.send_keys("amazon.com")
enter = driver.find_element(By.XPATH,"//input[@data-ved='0ahUKEwjg8_3q_O-FAxV9HDQIHWtCDn4Q4dUDCB4']")
enter.click()

driver.get("https://www.amazon.com/")
women_clothing=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
women_clothing.send_keys("women clothing")
driver.find_element(By.XPATH)
driver.find_element(By.XPATH)
"""
time.sleep(10)
driver.close()