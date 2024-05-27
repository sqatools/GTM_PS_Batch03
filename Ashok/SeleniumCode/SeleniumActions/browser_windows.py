"""
Browser windows
-------------------------
switch_to.window(WindowID)

current_window_handle     --> Return windowID of single browser window
window_handles		--> Return window ID's of multiple browser windows
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
windowid = driver.current_window_handle
print(windowid)
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowsIDs = driver.window_handles

# Approach 1
parent_windowid = windowsIDs[0]
child_windowid = windowsIDs[1]
print(parent_windowid,child_windowid)

driver.switch_to.window(child_windowid)
print(driver.title)
print(driver.current_url)

driver.switch_to.window(parent_windowid)
print(driver.title)
print(driver.current_url)

# Approach2
for winid in windowsIDs:
    driver.switch_to.window(winid)
    print(driver.title)
    print(driver.current_url)