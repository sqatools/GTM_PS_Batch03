import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.mcdonalds.com/us/en-us.html")
menu =driver.find_element(By.XPATH,"//button[@aria-controls='ourMenuSubItemsList_desktop']")
menu.click()
order =driver.find_element(By.XPATH,"//a[@id='button-ordernow']")
order.click()
#close = driver.find_element(By.XPATH,"//span[@class ='ui-button-icon ui-icon ui-icon-closethick']")
#close.click()


time.sleep(10)
driver.close()

