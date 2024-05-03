import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.yatra.com/")

search_flights = driver.find_element(By.XPATH,"//input[@value='Search Flights']")
search_flights.click()
search_again= driver.find_element(By.XPATH, "//span[@ng-if='!submitted']")
search_again.click()
user_login = driver.find_element(By.XPATH, "//li[@class='list-dropdown']")
user_login.click()
#sign_up = driver.find_element(By.XPATH,"//a[@id='SignUpBtn']")
#sign_up.click()

time.sleep(10)
driver.close()