
#################################### Browser Windows ##################################################################
'''
switch_to.window(windowID)
current_window_handle --> Return windowID of single browser window.
window_handles --> Return window ID's of multiple browser windows.
every execution the windowID will change.
'''
#1). Handle single browser window.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# driver.implicitly_wait(10)
# windowID1 = driver.current_window_handle
# print(windowID1)        #1st execution:5A7DEDB8408D571B2AE822E02DB5210B, 2nd execution:4338DBC9E1BE564111E46054260577CC
# driver.close()


#2). Handle multiple browser windows :
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
# windowIDs1 = driver.window_handles  # Here will get two browser windows ID, It is in the form of list format.
# parentWindowID = windowIDs1[0]
# childWindowID = windowIDs1[1]
# print('Parent window ID :',parentWindowID)   # Parent window ID : 3FA375923109D27A57F4B86CD2D6D33C
# print('Child window ID :',childWindowID)     # Child window ID : 22473911779E2BE3B646BD1FD43FDA46
# driver.close()

#3). If want to switch perticular browser window.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
# windowIDs1 = driver.window_handles  # Here will get two browser windows ID, It is in the form of list format.
# parentWindowID = windowIDs1[0]
# childWindowID = windowIDs1[1]
# driver.switch_to.window(childWindowID)
# print('Title of the childWindow: ',driver.title)        # Title of the childWindow:  Human Resources Management Software | OrangeHRM
# driver.switch_to.window(parentWindowID)
# print('Title of parent window: ',driver.title)          # Title of parent window:  OrangeHRM
# driver.close()

#3). If have multiple windows, We can apply loop.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
# windowIDs1 = driver.window_handles  # Here will get two browser windows ID, It is in the form of list format.
# for winID in windowIDs1:
#     driver.switch_to.window(winID)
#     print('Tiltle : ',driver.title)    # Tiltle :  OrangeHRM,Tiltle :  Human Resources Management Software | OrangeHRM
# driver.close()

#3). If have multiple browser windows, We can apply loop.  Also can navigate to perticular window by using condition :
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
# windowIDs1 = driver.window_handles  # Here will get two browser windows ID, It is in the form of list format.
# for winID in windowIDs1:
#     driver.switch_to.window(winID)
#     if driver.title == 'OrangeHRM':
#         driver.close()
# print('Title :',driver.title)   # Title : Human Resources Management Software | OrangeHRM
# driver.close()

#3). If have multiple browser windows, We can apply loop.  Also can navigate to perticular window by using condition :
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
windowIDs1 = driver.window_handles  # Here will get two browser windows ID, It is in the form of list format.
for winID in windowIDs1:
    driver.switch_to.window(winID)
    if driver.title == 'Human Resources Management Software | OrangeHRM':
        driver.close()
driver.close()