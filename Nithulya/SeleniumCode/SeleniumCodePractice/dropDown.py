# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# driver.maximize_window()
# driver.implicitly_wait(10)

# element1 = driver.find_element(By.XPATH,"//select[@id='admorepass']")
# dropCountry = Select(element1)
# # dropCountry.select_by_visible_text('Add 3 more passenger (200%)')
# #(OR)
# # dropCountry.select_by_value('4')
# #(OR)
#dropCountry.select_by_index('4')

# webdriver.close()

# #2).Capture all the options and print them
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# element1 = driver.find_element(By.XPATH,"//select[@id='admorepass']")
# dropCountry = Select(element1)
# allOptions = dropCountry.options
# print('Total Number of Options :',len(allOptions))
# for opt in allOptions:
    #print(opt.text)

#driver.close()


#2).Select option from dropdown without uing built-in method
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
driver.implicitly_wait(10)

element1 = driver.find_element(By.XPATH,"//select[@id='admorepass']")
dropCountry = Select(element1)
allOptions = dropCountry.options
for opt in allOptions:
    if opt.text == 'Add 1 more passenger (100%)':
        opt.click()
        time.sleep(1)
        break

driver.close()


