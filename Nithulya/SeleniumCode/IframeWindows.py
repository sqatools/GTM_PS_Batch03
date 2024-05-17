#1.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
# driver.implicitly_wait(15)
# driver.maximize_window()
# iframeElement1 = driver.find_element(By.NAME,"globalSqa")
# driver.switch_to.frame(iframeElement1)
#
# driver.find_element(By.XPATH, "//div[@id='mobile_menu_toggler']").click()
# driver.switch_to.default_content()
# page_heading = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
# print(page_heading.text)
#
# home_page = driver.find_element(By.XPATH, "//a[text()='Home']")
# home_page.click()
#
# time.sleep(5)
# driver.close()


#2.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://theautomationzone.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()

iframe1 = driver.find_element(By.ID,'frame1')
driver.switch_to.frame(iframe1)
iframe12 = driver.find_element(By.XPATH,"//p[text()='Parent Iframe']")
print(iframe12.text)
iframe2 = driver.find_element(By.ID,'frame2')
driver.switch_to.frame(iframe2)
iframe21 = driver.find_element(By.XPATH,"//p[text()='child Iframe']")
print(iframe21.text)
driver.switch_to.default_content()
title1 = driver.find_element(By.XPATH,"//div[@class='titlewrapper']/child::h1[@class='title']")
print('Title :',title1.text)


