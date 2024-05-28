"""
Checkbox:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# 1) select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='sunday']").click()

# 2) select all the checkboxes
all_checkboxes = driver.find_elements(By.XPATH, "//input[contains(@id,'day')]")
print(len(all_checkboxes))
# all_checkboxes[0].click()
# to select all checkboxes we need to use for loop
# for i in range(len(all_checkboxes)):
#     all_checkboxes[i].click()

# 3. select multiple checkboxes by choice
# for checkbox in all_checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname == 'monday' or weekname == 'tuesday':
#         checkbox.click()


# 4. select last 2 checkboxes
# for i in range(len(all_checkboxes)-2, len(all_checkboxes)):
#     all_checkboxes[i].click()

# 5. select first 2 checkboxes
# for i in range(len(all_checkboxes)):
#     if i < 2:
#         all_checkboxes[i].click()

# 6. clearing all the checkboxes
for i in range(len(all_checkboxes)):
    all_checkboxes[i].click()
for checkbox in all_checkboxes:
    if checkbox.is_selected():
        checkbox.click()




