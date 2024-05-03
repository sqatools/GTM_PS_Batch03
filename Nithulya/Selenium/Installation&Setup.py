# """
# pip install selenium
# """
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.get("https://www.google.co.in")
# driver.find_element(By.NAME,"q").send_keys("Python Selenium")
# driver.find_element(By.NAME,"btnK").click()
#
# time.sleep(10)
# driver.close()


#(OR)

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.get("https://www.google.co.in")
# search_element = driver.find_element(By.NAME, "q")
# print(search_element)
# # NAME Locator
# search_element.send_keys("Python Selenium")
# driver.find_element(By.NAME, "btnK").click()
#
# # LINK_TEXT, PARTIAL LINK_TEXT
# tutorials_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium with Python")
# tutorials_link.click()
#
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#
# # Tagname Locator
# header = driver.find_element(By.TAG_NAME, "h1")
# print(header.text)
#
# # ID Locator
# from_city_element = driver.find_element(By.ID, "fromcity")
# from_city_element.send_keys("Mumbai")
#
# time.sleep(10)
# driver.close()


#3). Locator : NAME,ID
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# #driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#(OR)                                                                                                   #By.NAME
# driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")          #By.ID
# time.sleep(5)
# driver.close()

#4).Locator : Link Text / Partial Link Text
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# #driver.find_element(By.LINK_TEXT,"Register").click()              #By.LINK_TEXT
# #(OR)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()            #By.ARTIAL_LINK_TEXT
# time.sleep(5)
#driver.close()


#5). Locator : Classname & Tagname (To find more than one elements in webpage)
#if writes find_element instead of find_elements, the locator will identify first web element.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://automationpanda.com/")
driver.maximize_window()
# sliders = driver.find_elements(By.CLASS_NAME,"menu-item menu-item-type-post_type menu-item-object-page menu-item-10")
# print(len(sliders))                                                                            #By.CLASS_NAME  : 0
#(OR)
# link1= driver.find_elements(By.TAG_NAME,"a")      # TAG_NAME     : 235
# print(len(link1))
# time.sleep(5)



