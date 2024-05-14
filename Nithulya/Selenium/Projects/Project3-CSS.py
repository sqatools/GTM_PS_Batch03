from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
driver.implicitly_wait(10)
search1 = driver.find_element(By.CSS_SELECTOR,'#search')
time.sleep(2)
search1.send_keys("women's top")
search2 = driver.find_element(By.CSS_SELECTOR,'.action[title=Search]')
search2.click()
time.sleep(1)
next1 = driver.find_element(By.CSS_SELECTOR,'div>a[href=https://magento.softwaretestingboard.com/nona-fitness-tank.html]')
next1.click()
time.sleep(1)
next2 = driver.find_element(By.CSS_SELECTOR,'div>a[href=https://magento.softwaretestingboard.com/nona-fitness-tank.html]')
next2.click()
time.sleep(2)
driver.close()


