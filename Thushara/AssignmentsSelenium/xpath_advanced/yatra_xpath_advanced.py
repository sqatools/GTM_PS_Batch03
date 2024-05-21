import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.yatra.com/")
search_flights = driver.find_element(By.XPATH,"//input[@value='Search Flights' and @id='BE_flight_flsearch_btn']")
a =search_flights.text
print(a)
search_flights.click()

time.sleep(10)
driver.close()