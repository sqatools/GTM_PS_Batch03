"""
pip install selenium
CSS Selector :
    1).tag id - tagname#valueofID
    2).tag class - tagname.valueofClass
    3).tag attribute - tagname[attribute=value]
    4).tag class attribute - tagname.valueofClass[attribute=value]

"""
#1).
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
#
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#
# driver.find_element(By.CSS_SELECTOR,'#fromcity').send_keys('Mumbai')
# driver.find_element(By.CSS_SELECTOR,'div>input#destcity').send_keys('Cochin')
#
# time.sleep(5)
# driver.close()

#2).######################## tag id combination #######################################################################
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.facebook.com/")
# #driver.find_element(By.CSS_SELECTOR,'input#email').send_keys('abc')    - tagname is optional
# driver.find_element(By.CSS_SELECTOR,'#email').send_keys('abc')
#
# time.sleep(3)
# driver.close()

#3).######################## tag class combination #######################################################################
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.facebook.com/")
# #driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys('abc@gmail.com') - actual class name is inputtext _55r1 _6luy, but after space it may show error,so removed that part.
# driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys('abc@gmail.com')
#
# time.sleep(3)
# driver.close()

#4).######################## tag attribute combination #######################################################################
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.facebook.com/")
# #driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal_email]').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR,'[data-testid=royal_email]').send_keys('abc@gmail.com')
#
# time.sleep(3)
# driver.close()

#4).######################## tag class attribute combination #######################################################################
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
#driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid=royal_pass]').send_keys('xyz') - if tagname and classname are same,differentiate with attribute.
driver.find_element(By.CSS_SELECTOR,'.inputtext[data-testid=royal_pass]').send_keys('xyz')

time.sleep(3)
driver.close()