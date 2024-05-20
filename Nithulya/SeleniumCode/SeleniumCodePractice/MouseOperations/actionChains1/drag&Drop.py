'''
Class : ActionChains
It include methods are,
1) Mouse Hover - ActionChains(driver), it is a class,import from selenium., move_to_element()
2) Right click - ActionChains(driver),context_click(element).perform()
3) Double click - ActionChains(driver),double_click(element).perform()
4) Drag and drop - ActionChains(driver),drag_and_drop(source element,target element)
    slider - ActionChains(driver), drag_and_drop_by_offset(element,value of x axis,value of y axis).perform()

'''

############################ Drag and Drop #############################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source1 = driver.find_element(By.XPATH,"//div[@id='box5']")
dest1 =  driver.find_element(By.XPATH,"//div[@id='box105']")
act = ActionChains(driver)
act.drag_and_drop(source1,dest1).perform()
time.sleep(2)
driver.close()
