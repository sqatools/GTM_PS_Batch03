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
Explicit wait is condition based wait statement. The explicit wait is used to wait for specific conditions
(or) the maximum time exceeded before throwing "Element not visible exception"
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
# driver.implicitly_wait(10)
# driver.get("https://www.google.com/")
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Selenium")
# search_box.submit()

################ Explicit Wait #####################
mywait = WebDriverWait(driver, timeout=10)  # explicit wait declaration
mywait1 = WebDriverWait(driver, timeout=10, poll_frequency=2, ignored_exceptions=[
                                           NoSuchElementException,
                                           ElementNotVisibleException,
                                           ElementNotSelectableException,
                                           Exception])

driver.get("https://www.google.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()
search_link = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()