####### - The website is not working,
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
driver.maximize_window()
driver.implicitly_wait(10)

driver.execute_script("window.scrollBy(0,3000)","")     # scroll down page by pixel,it is a javascript syntax.
value = driver.execute_script("return window.pageYoffset;")
print('Number of pixels moved : ',value)
time.sleep(5)


driver.close()