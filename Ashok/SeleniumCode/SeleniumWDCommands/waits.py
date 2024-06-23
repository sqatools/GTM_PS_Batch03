"""
wait commands:
--------------
1. time sleep(): The program is paused for the given time and after that time has passed, the program gets
executed automatically

adv: simple to use
----
dis adv:
--------
i) performance of the script is very poor
ii) If the element is not available within the time mentioned , still there is a chance of getting exception.
iii) if the element is found also still it will wait for complete time.

Note: time.sleep() is a python related code and this is not a wait commands.Actual wait command in selenium are
2. implicit wait
3. explicit wait

Implicit wait:
-------------
i) Implicit wait in Selenium is a setting that allows the WebDriver to wait for a certain amount of time for an element
to appear on the page before throwing an exception.
ii) This wait is applied globally to all elements that the WebDriver interacts with, meaning it will be in effect for
the entire duration of the WebDriver's instance.
iii) When an implicit wait is set, Selenium will wait for the specified amount of time for the element to become
available in the DOM. If the element is found before the timeout expires, Selenium will proceed with the next steps
in the test script. If the element is not found within the specified time, a NoSuchElementException will be raised

Adv:
-----
i) Single statement
ii) Performance will not be reduced.(If the element is available within the time it
proceed to execute further statements.

DisAdv:
---
i) If the element is not available within the time mentioned , still there is a chance of getting exception.

Explicit Wait:
-------------
i) Explicit wait is condition based wait statement. The explicit wait is used to wait for specific conditions
(or) the maximum time exceeded before throwing "Element not visible exception"
ii) We need to import WebDriverWait class first and need to declare the explicit wait
ii) Later need to import "Expected conditions" module.
iv) Explicit wait is not for global it has to write at line level.

Syntax:
-------
mywait = WebDriverWait(driver, timeout=12, poll_frequency=2, ignored_exceptions=[Exception])
"""

############## Implicit Wait ##############
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
# driver.implicitly_wait(11)
# driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
# driver.find_element(By.ID, "btn1").click()
# # Below element will load after 5 seconds. If implicit wait is less than 5, it will throw error.
# driver.find_element(By.ID, "txt1").send_keys("abc")
# driver.find_element(By.ID, "btn2").click()
# # Below element will load after 10 seconds. If implicit wait is less than 10, it will throw error.
# driver.find_element(By.ID, "txt2").send_keys("def")

################ Explicit Wait #####################
# 1. Explicit wait with basic syntax
# driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
# driver.find_element(By.ID, "btn1").click()
#
# mywait = WebDriverWait(driver, timeout=11)
#
# text_box1 = mywait.until(EC.presence_of_element_located((By.ID, 'txt1')))
# text_box1.send_keys("abc")
# text_box2 = mywait.until(EC.element_to_be_clickable((By.ID, 'btn2')))
# text_box2.click()
# text_box3 = mywait.until(EC.presence_of_element_located((By.ID, 'txt2')))
# text_box3.send_keys("def")

# 2. Explicit wait with complete syntax

driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
driver.find_element(By.ID, "btn1").click()

mywait = WebDriverWait(driver, timeout=12, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                 ElementNotVisibleException,
                                                                                 ElementNotSelectableException,
                                                                                 Exception])

text_box1 = mywait.until(EC.presence_of_element_located((By.ID, 'txt1')))
text_box1.send_keys("abc")
text_box2 = mywait.until(EC.element_to_be_clickable((By.ID, 'btn2')))
text_box2.click()
text_box3 = mywait.until(EC.presence_of_element_located((By.ID, 'txt2')))
text_box3.send_keys("def")