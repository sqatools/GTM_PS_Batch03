"""
1) Application commands
2) Conditional commands
3) Browser commands
4) Navigational commands
5) wait commands

Application commands
---------
get() - opening the application URL
title - to capture teh title of the current webpage
current_url - to capture the current url of the web page
page_source - to capture source code of the page

Conditional commands
--------------------
is_displayed()
is_enabled()
is_selected() - for radio buttons and check boxes

Browser commands
---------------
close() - close single browser window (where driver focused)
quit() - close multiple browser windows ( this will kill the process)

Navigational commands
-------------------
back()
forward()
refresh()

"""
import time

########### Application Commands ##################
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# print(driver.title)    # OrangeHRM
# print(driver.current_url)
# print(driver.page_source)

########## Conditional Commands ##################
# driver.get("https://demo.nopcommerce.com/register")
# # driver.implicitly_wait(10)
# search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print("Search box is displayed:", search_box.is_displayed())
# print("Search box is displayed:", search_box.is_enabled())
# rd_male = driver.find_element(By.ID, "gender-male")
# rd_female = driver.find_element(By.ID, "gender-female")
# print("Is Selected:", rd_male.is_selected())       # False
# print("Is Selected:", rd_female.is_selected())     # False
# rd_male.click()
# print("Is Selected:", rd_male.is_selected())          # True
# print("Is Selected:", rd_female.is_selected())        # False
# rd_female.click()
# print("Is Selected:", rd_male.is_selected())           # False
# print("Is Selected:", rd_female.is_selected())         # True

################# Browser Commands ################
# # Close # Quit
# driver.get("https://opensource-demo.orangehrmlive.com/")
# time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM, Inc").click()
# time.sleep(6)
# # driver.close()
# driver.quit()

############### Navigational Commands ###############
driver.get("https://www.snapdeal.com")
driver.get("http://www.amazon.com")
# driver.back()  # snapdeal
# driver.forward()  # amazon
# driver.refresh()
