"""
Frames/Iframes
--------------
switch_to_frame()   # selenium3

#selenium4
switch_to.frame(name of the frame)
switch_to.frame(id of the frame)
switch_to.frame(webelement)
switch_to.frame(0)

switch_to.default_content()

frame or iframe or form  - HTML tags of Iframes

inner frames

"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

######## Switching between multiple frames #############
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID, "name").send_keys("abc")
# Switch to iframe1
first_frame = driver.find_element(By.ID, "frm1")
driver.switch_to.frame(first_frame)
first_frame_dd = Select(driver.find_element(By.ID, "course"))
first_frame_dd.select_by_visible_text("Java")
time.sleep(2)
# Switch to main page
driver.switch_to.default_content()
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("efg")
# Switch to iframe1 and changing the course
driver.switch_to.frame("frm1")  # using id of the frame.
first_frame_dd1 = Select(driver.find_element(By.ID, "course"))
first_frame_dd1.select_by_visible_text("Python")
driver.switch_to.default_content()

# Switching to second frame
driver.switch_to.frame("frm2")
driver.find_element(By.ID, "firstName").send_keys("Ashok")
driver.switch_to.default_content()

# Switch to frame1
driver.switch_to.frame("frm1")  # using id of the frame.
first_frame_dd1 = Select(driver.find_element(By.ID, "course"))
first_frame_dd1.select_by_visible_text("Java")
driver.switch_to.default_content()

############# Inner Frames ##################
driver.implicitly_wait(5)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()
outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(inner_frame)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")

# directly switch to parent frame(outer_frame). This command introduced in Selenium 4
driver.switch_to.parent_frame()

