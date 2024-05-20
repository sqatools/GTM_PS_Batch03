'''
Class : ActionChains
It include methods are,
1) Mouse Hover - ActionChains(driver), it is a class,import from selenium., move_to_element()
2) Right click - ActionChains(driver),context_click(element).perform()
3) Double click - ActionChains(driver),double_click(element).perform()
4) Drag and drop - ActionChains(driver),drag_and_drop(source element,target element)
    slider =ActionChains(driver), drag_and_drop_by_offset(element,value of x axis,value of y axis).perform()

'''

############################ Right Click #############################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

frame1 = driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")
driver.switch_to.frame(frame1)
field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys('Welcome')
button1 = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
act = ActionChains(driver)
act.double_click(button1).perform()
time.sleep(2)
driver.close()