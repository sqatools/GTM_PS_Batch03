from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
driver.implicitly_wait(10)
#1.
# driver.find_element(By.XPATH, "//tr[2]//parent::td//child::input[@type='checkbox']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//tr[3]//parent::td//child::input[@type='checkbox']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//tr[4]//parent::td//child::input[@type='checkbox']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//tr[5]//parent::td//child::input[@type='checkbox']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//tr[6]//parent::td//child::input[@type='checkbox']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//tr[7]//parent::td//child::input[@type='checkbox']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//tr[8]//parent::td//child::input[@type='checkbox']").click()
# time.sleep(3)
#
# driver.close()

## (OR)

# for box in range(2,9):
#     box1=driver.find_element(By.XPATH, f"//tr[{box}]//parent::td//child::input[@type='checkbox']")
#     box1.click()
#     time.sleep(1)
#
# driver.close()


#2.
# for box in range(2,9):
#     if box%2 !=0:
#         box1=driver.find_element(By.XPATH, f"//tr[{box}]//parent::td//child::input[@type='checkbox']")
#         box1.click()
#     else:
#         pass
#     time.sleep(1)
#
# driver.close()


#3
# for box in range(2,9):
#     if box>=7:
#         box1=driver.find_element(By.XPATH, f"//tr[{box}]//parent::td//child::input[@type='checkbox']")
#         box1.click()
#     else:
#         pass
#     time.sleep(1)
#
# driver.close()

#4
# boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# for box in boxes:
#     box.click()
#     time.sleep(1)
# for box in boxes:
#     if box.is_selected():
#         box.click()
#         time.sleep(1)
#
# driver.close()

#5
boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for box in range(2,9):
    if box%2 !=0:
        box1=driver.find_element(By.XPATH, f"//tr[{box}]//parent::td//child::input[@type='checkbox']")
        box1.click()
    else:
        pass
    time.sleep(1)
for box in boxes:
    if box.is_selected():
        box.click()
        time.sleep(1)

driver.close()