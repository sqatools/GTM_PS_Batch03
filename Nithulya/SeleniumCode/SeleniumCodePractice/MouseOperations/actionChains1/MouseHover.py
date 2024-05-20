'''
Class : ActionChains
It include methods are,
1) Mouse Hover - ActionChains(driver), it is a class,import from selenium., move_to_element()
2) Right click - ActionChains(driver),context_click(button1).perform()
3) Double click - ActionChains(driver),double_click(element).perform()
4) Drag and drop - ActionChains(driver),drag_and_drop(source element,target element)
  slider =ActionChains(driver), drag_and_drop_by_offset(element,value of x axis,value of y axis).perform()

'''
############################## Mouse Hover ############################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
driver.maximize_window()
driver.implicitly_wait(10)

act = ActionChains(driver)
testerHub = driver.find_element(By.XPATH, "//a[@href='https://www.globalsqa.com/testers-hub/' and text()='Tester’s Hub']")
demoTesting = driver.find_element(By.XPATH, "//a[@href='https://www.globalsqa.com/demo-site/']")
toolBar = driver.find_element(By.XPATH, "//a[@href='https://www.globalsqa.com/demo-site/toolbar/']")
act.move_to_element(testerHub).move_to_element(demoTesting).move_to_element(toolBar).click().perform()
time.sleep(5)


driver.close()