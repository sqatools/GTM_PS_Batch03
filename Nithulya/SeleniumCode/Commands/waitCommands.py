"""
1. Static waits(time.sleep() - this from python) : This is hard corded sleep between two steps
     Adv :
        1. Simple to use
    Dis Adv :
        1.Performance of the script is very poor.
        2.If the element is not available within the time mentioned, still there is a chance of getting the exception.
2. implicit wait : This wait will apply on all the element of the webpage (it is from selenium webdriver)
       Adv :
        1. Single statement
        2.Performance will not be reduced.(If the element is available within the time, it proceed to execute further statement.
    Dis Adv :
        1.If the element is not available within the time mentioned, still there is a chance of getting the exception.

3. explicit wait : This wait will apply on specific element of the page. It works based on conditions.
    Adv :
        1.More effectively works.
    Dis. Adv:
        1.Multiple places feel some difficulty.
4. Fluent wait : This wait will apply on specific element of the page with customize frequency of poll.

"""
#1. Static Wait :##################################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# driver.maximize_window()
# time.sleep(3)   # static time
# search1 = driver.find_element(By.NAME,"fromcity")
# time.sleep(3)   # static time
# search1.send_keys('Cochin')


#2. Implicit wait:#####################################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# t1 = time.time()
# try:
#     element = driver.find_element(By.ID, "billing_name")
#     element.send_keys("Mumbai")
# except Exception as e:
#     print(e)
# t2 = time.time()
# print("total time taken :", t2-t1)

#3.Explicit wait ####################################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# driver.maximize_window()
# wait = WebDriverWait(driver, timeout=15)  # explicit wait declaration
#
# t1 = time.time()
# try:
#     element = driver.find_element(By.ID, "billing_name")    # If ID of the web element is correct
#     element.send_keys("Mumbai")
# except Exception as e:
#     print(e)
# t2 = time.time()
# print("total time taken :", t2-t1)
#
#
# b1 = time.time()
# try:
#     #element = wait.until(EC.visibility_of_element_located((By.ID, "billing_phone234")))
#     element = wait.until(EC.element_to_be_clickable((By.ID, "billing_phone234"))) # if the condition is satisfied, perform next action (send.key())
#                                                                     # if the condition is not satisfying, it will wait untill 15sec and then exit()
#     print(element)
#     element.send_keys("9889798789")
# except Exception as e:
#     print(e)
# b2 = time.time()
# print("total time taken :", b2-b1)
#
# driver.close()


#4.Fluent wait : ######################################################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
wait = WebDriverWait(driver, timeout=10, poll_frequency=2)  # fluent wait with custom poll frequency
             # it will check the element every 2sec in total 10sec(total 5 poll), poll_frequency always lesser than timeout value.
t1 = time.time()
try:
    element = driver.find_element(By.ID, "billing_name")
    element.send_keys("Mumbai")
except Exception as e:
    print(e)
t2 = time.time()
print("total time taken :", t2-t1)

b1 = time.time()
try:
    #element = wait.until(EC.visibility_of_element_located((By.ID, "billing_phone234")))
    element = wait.until(EC.element_to_be_clickable((By.ID, "billing_phone234")))
    print(element)
    element.send_keys("9889798789")
except Exception as e:
    print(e)
b2 = time.time()
print("total time taken :", b2-b1)

driver.close()
