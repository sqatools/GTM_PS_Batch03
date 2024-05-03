import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.keralatourism.org/")

where_to_go = driver.find_element(By.XPATH,"//a[@href='#where-to-go']")
where_to_go.click()
#munnar = driver.find_element(By.XPATH,"//img[contains(@src, 'munnar1')"])
#munnar.click()
things_to_do = driver.find_element(By.XPATH,"//a[@href='#things-to-do']")
things_to_do.click()
find_more = driver.find_element(By.XPATH,"//a[@href='https://www.keralatourism.org/specialities/']")
find_more.click()

time.sleep(10)
driver.close()