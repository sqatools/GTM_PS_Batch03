from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
driver.implicitly_wait(15)
driver.maximize_window()

###### Alert box #####################################################################################################
# driver.find_element(By.XPATH,"//input[@id='btnShowMsg']").click()
# time.sleep(3)
# # alert1 = driver.switch_to.alert
# # print(alert1.text)
# # alert1.dismiss()          # (OR)
# alert1 = Alert(driver)
# print(alert1.text)
# alert1.accept()
# time.sleep(3)

########## Confirm Box ###############################################################################################
# driver.find_element(By.XPATH,"//button[@id='button']").click()
# time.sleep(3)
# alert_obj = Alert(driver)
# print(alert_obj.text)
# alert_obj.accept()
# #alert_obj.dismiss()
# msg = driver.find_element(By.XPATH,"//p[text()='You pressed OK!']")
# print(msg.text)

########## Prompt Box #################################################################################################
driver.find_element(By.XPATH,"//button[@id='promptbtn']").click()
time.sleep(5)
alert1 = Alert(driver)
print(alert1.text)
alert1.send_keys("GTM")
time.sleep(2)
alert1.accept()
#alert1.dismiss()
msg = driver.find_element(By.ID, "prompt")
print(msg.text)

driver.close()