import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(5)

browser.get("https://www.google.com/")
search = browser.find_element(By.XPATH,"//textarea[contains(@aria-controls, 'Alh6id')]")
search.send_keys("python selenium bindings")
enter= browser.find_element(By.XPATH,"//input[@data-ved='0ahUKEwi7qNHLsfCFAxXnGDQIHfWADvkQ4dUDCBc']")
enter.click()
#enter =browser.find_element(By.XPATH," //*[contains(@data-ved, '0ahUKEwi7qNHLsfCFAxXnGDQIHfWADvkQ4dUDCBc')]")
#enter.click()

time.sleep(10)
browser.close()
