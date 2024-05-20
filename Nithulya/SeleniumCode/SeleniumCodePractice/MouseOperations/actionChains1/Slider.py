'''
Class : ActionChains
It include methods are,
1) Mouse Hover - ActionChains(driver), it is a class,import from selenium., move_to_element()
2) Right click - ActionChains(driver),context_click(element).perform()
3) Double click - ActionChains(driver),double_click(element).perform()
4) Drag and drop - ActionChains(driver),drag_and_drop(source element,target element)
    slider - ActionChains(driver), drag_and_drop_by_offset(element,value of x axis,value of y axis).perform()
'''
############################ Slider - Drag #############################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

start1 = driver.find_element(By.XPATH,"//span[@tabindex='0'][1]")
end1 =  driver.find_element(By.XPATH,"//span[@tabindex='0'][2]")

print('Location of slider before moving :',start1.location)  # {'x': 59, 'y': 250}  # x:horizontal,y: vertical(can not move)
print('Location of slider before moving :',end1.location)    # {'x': 612, 'y': 250} # x:horizontal,y: vertical(can not move)

act = ActionChains(driver)
act.drag_and_drop_by_offset(start1,100,0).perform()
act.drag_and_drop_by_offset(end1,-12,0).perform()

print('Location of slider after moving :',start1.location) # {'x': 159, 'y': 250} # (59+100=159)
print('Location of slider after moving :',end1.location)   # {'x': 601, 'y': 250} #(612-12=601),will not get exact value
time.sleep(2)
driver.close()