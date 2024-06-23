import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='search']").send_keys("mens t-shirt")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.LINK_TEXT, "Balboa Persistence Tee").click()
time.sleep(1)
driver.find_element(By.ID, "option-label-size-143-item-169").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-52']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='product-addtocart-button']").click()
time.sleep(2)

driver.find_element(By.ID, "search").send_keys("men hoodie")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Marco Lightweight").click()
time.sleep(1)
# using tagname.valueofClass[attribute=value]
driver.find_element(By.CSS_SELECTOR, "div.swatch-option[id=option-label-size-143-item-169]").click()
time.sleep(1)
# using tagname[attribute=value]
driver.find_element(By.CSS_SELECTOR, "div[id=option-label-color-93-item-50]").click()
time.sleep(1)
# using [attribute=value]
driver.find_element(By.CSS_SELECTOR, "[id=product-addtocart-button]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='search']").send_keys("mens pants")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.LINK_TEXT, "Aether Gym Pant").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-176']").click()
driver.find_element(By.XPATH, "//div[@class ='swatch-option color' and @id='option-label-color-93-item-50']").click()
driver.find_element(By.XPATH, "//span[contains(text(), 'Add to Cart')]").click()
time.sleep(1)

driver.find_element(By.XPATH,
                    "//a[contains(@href, 'softwaretestingboard')]/parent::div[@data-block='minicart']").click()
driver.find_element(By.XPATH, "//button[contains(@id, 'top-cart-btn-checkout')]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='customer-email' and @class='input-text']").send_keys("abc@test.com")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@class='input-text' and @name='firstname']").send_keys("Ashok")
driver.find_element(By.XPATH, "//*[@name='lastname']").send_keys("Pusarla")
driver.find_element(By.XPATH, "//*[@class='input-text' and @name='company']").send_keys("ValueLabs")
driver.find_element(By.XPATH, "//*[@name='street[0]' or @id='VX70X9S']").send_keys("1-123")
driver.find_element(By.XPATH, "//*[@name='city' or @id='NYUM91A']").send_keys("Hyderabad")
time.sleep(2)
driver.find_element(By.XPATH, "//option[@data-title='Alabama']").click()
driver.find_element(By.XPATH, "//*[@name='postcode' or @id='GVU9G59']").send_keys("53500")
driver.find_element(By.XPATH, "//*[@name='country_id' or @id='BOBGWFV']").send_keys("United States")
driver.find_element(By.XPATH, "//*[@name='telephone' or @id='T125134']").send_keys("1234567892")
