"""
Alerts are written in JavaScript. We will not have html/dom for alerts. We can't do inspect element or
alerts as it is written in JavaScript.

1. Alert box:  It is having simple message box with Ok button
2. Confirm box: It is having simple/confirm message box with OK, Cancel buttons
3. Prompt box: It is having simple message box with text field
---------------
4. Authentication popup:
   i) We will have two text boxes, and we cannot use send_keys, so we need to inject the UN & PWD and by pass the
   pop-up.
   ii) To bypass the authentication we need to follow below steps.

    URL: http://the-internet.herokuapp.com/basic_auth
    syntax: http://username:password@url.com
    Example: http://admin:admin@the-internet.herokuapp.com/basic_auth

To work with alerts we need to use "switch_to.alert" which is available in webdriver

myalert=driver.switch_to.alert
myalert.text    - Prints the alert/pop up text message
myalert.accept()  - close alert window by using OK button
myalert.dismiss()  - close alert window by using Cancel button

5. Notifications pop-ups - Sometimes browser will show pop up for location with Allow and  Block pop-ups
We cannot interact/inject(bypass) these pop up. To avoid these we need to use ChromeOptions.
we need to add argument as "--disable_notification

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

########  Using Alert box ##########
# driver.implicitly_wait(5)
# # //button[text()='Click for JS Alert']
# # //button[normalize-space()='Click for JS Alert']
# # For text method we need to provide exact spaces but for normalize-space, if we have extra spaces it will ignore
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()
# # using switch_to.alert method
# alertwindow = driver.switch_to.alert
# print(alertwindow.text)
# time.sleep(2)
# alertwindow.accept()  # close alert window by using OK button

########  Using confirm box ##########
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
# confirm_box = driver.switch_to.alert
# time.sleep(1)
# print(confirm_box.text)
# confirm_box.accept()    # close alert window by using OK button
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
# time.sleep(1)
# confirm_box.dismiss()   # close alert window by using Cancel button

######## Using prompt box ###########
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
# prompt_box = driver.switch_to.alert
# time.sleep(1)
# print(prompt_box.text)
# prompt_box.send_keys("abc")
# time.sleep(3)
# prompt_box.accept()
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
# prompt_box.send_keys("abc")
# time.sleep(2)
# prompt_box.dismiss()

######## Using Authentication pop up ###########
# driver.get("http://the-internet.herokuapp.com/basic_auth")
# # providing UN and PWD
# driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")


########### Notification pop ups ###########################
driver.get("https://whatmylocation.com/")
driver.maximize_window()


