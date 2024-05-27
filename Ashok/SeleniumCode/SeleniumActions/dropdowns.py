"""
1. Every drop down will have "select" as tag name.
2. To work on drop down, we need to import "select" class and use it.
3. Drop down is an element. Each value from drop down also a web element

Popular methods in select class:
--------------------------------
select_by_index()
select_by_value()
select_by_visible_text()
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
# without using select class
# dropdown = driver.find_element(By.XPATH, "//div[@class='form-group']//select[@id='country']")
# dropdown.send_keys("Canada")
# using select class
dropdown1 = Select(driver.find_element(By.XPATH, "//div[@class='form-group']//select[@id='country']"))
# Below are the methods from select class
# dropdown1.select_by_index(1)
# dropdown1.select_by_value("canada")
dropdown1.select_by_visible_text("Canada")

#  Capture all the options from dropdown and print them
all_options = dropdown1.options
print(len(all_options))

# Printing the all options names
for option in all_options:
    print(option.text)






