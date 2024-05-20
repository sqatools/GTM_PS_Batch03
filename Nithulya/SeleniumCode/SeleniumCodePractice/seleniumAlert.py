
##################### Alerts,Popups #################################################################################
#1).
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# click1 = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
# time.sleep(1)
# alert1 = driver.switch_to.alert
# time.sleep(1)
# print(alert1.text)
# time.sleep(2)
# alert1.send_keys('Welcome')
# time.sleep(1)
# alert1.accept()
# time.sleep(1)
# result1 = driver.find_element(By.XPATH,"//p[@id='result']")
# print(result1.text)


#2).
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# click1 = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
# time.sleep(1)
# alert1 = driver.switch_to.alert
# time.sleep(1)
# print(alert1.text)
# time.sleep(2)
# alert1.send_keys('Welcome')
# time.sleep(1)
# alert1.dismiss()
# time.sleep(1)
# result1 = driver.find_element(By.XPATH,"//p[@id='result']")
# print(result1.text)

#3).
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# click1 = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
# time.sleep(1)
# alert1 = driver.switch_to.alert
# time.sleep(1)
# print(alert1.text)
# time.sleep(2)
# alert1.send_keys('Welcome')
# time.sleep(1)
# alert1.dismiss()
# time.sleep(1)
# result1 = driver.find_element(By.XPATH,"//p[@id='result']")
# print(result1.text)

##################### Authentication Popups #########################################################################
### Syntax : http://username:password@test.com
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")  # Actual path is ("https://the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
driver.implicitly_wait(10)

