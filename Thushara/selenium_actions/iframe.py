import time
from selenium import webdriver
from selenium.webdriver.common.by import By


opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
"""
iframe_element = driver.find_element(By.NAME,"globalSqa")
driver.switch_to.frame(iframe_element)
driver.find_element(By.XPATH,"//span[@class='link_span' and text()='Draggable Boxes']").click()

driver.switch_to.default_content()

"""


iframe_element = driver.find_element(By.NAME, "globalSqa")
driver.switch_to.frame(iframe_element)

driver.find_element(By.XPATH, "//div[@id='mobile_menu_toggler']").click()

driver.switch_to.default_content()

page_heading = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
print(page_heading.text)

home_page = driver.find_element(By.XPATH, "//a[text()='Home']")
home_page.click()




time.sleep(10)

#driver.close()



