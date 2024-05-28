"""
Browser windows
-------------------------
Like alerts we need to use switch concept i.e, switch_to.window(WindowID)
Every window have dynamic id which will be created in run time.
Using that id, we can switch between windows.

current_window_handle     --> Return windowID of single browser window
window_handles		--> Return window ID's of multiple browser windows
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
windowid = driver.current_window_handle   # To handle only current window
print(windowid)
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowsIDs = driver.window_handles  # To handle multiple windows

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

#### Example 2 ###################

driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Abc")
windowid = driver.current_window_handle   # To handle only current window
print(windowid)
driver.find_element(By.XPATH, "//button[@id='newWindowBtn']").click()
WindowIDs = driver.window_handles
parent_windowId = WindowIDs[0]
child_windowId = WindowIDs[1]
print(parent_windowId, child_windowId)
driver.switch_to.window(child_windowId)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Ashok")
time.sleep(3)
driver.switch_to.window(parent_windowId)
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Def")




