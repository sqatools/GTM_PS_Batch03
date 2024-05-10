from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# driver.get("https://www.google.com/")
# driver.maximize_window()
# search_element = driver.find_element(By.NAME, "q")
# print(search_element)
# search_element.send_keys("Python Selenium")

# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# driver.find_element(By.NAME, "email").send_keys("ashok.pusarla@test.com")
# driver.find_element(By.ID, "pass").send_keys("password")
# driver.find_element(By.NAME, "login").click()
# driver.implicitly_wait(5)
# incorrect_msg = driver.find_element(By.XPATH, """//div[text()="The email address you entered isn't connected to an
# account. "]""")
# print(incorrect_msg.text)
# assert "incorrect" in incorrect_msg.text

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@value='radio_123']").click()
driver.find_element(By.XPATH, "//input[@id='firstname'][1]").send_keys("Ashok")
driver.find_element(By.XPATH, "//input[@id='firstname'][2]").send_keys("Pusarla")
driver.find_element(By.XPATH, "//*[@id='birthday']").send_keys("01/31/1990")
driver.find_element(By.ID, "male").click()
driver.find_element(By.ID, "oneway").click()
driver.find_element(By.NAME, "fromcity").send_keys("Hyderabad")
driver.find_element(By.NAME, "destcity").send_keys("Vizag")
driver.find_element(By.XPATH, "//input[@id='departdate']").send_keys("05/10/2024")
driver.find_element(By.XPATH, "//input[@name='returndate']").send_keys("05/12/2024")
driver.find_element(By.XPATH, "//input[@id='visadate']").send_keys("05/11/2024")
driver.find_element(By.XPATH, "//input[@id='billing_name']").send_keys("Ashok")
driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("12345678")
driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("test@test.com")
driver.find_element(By.XPATH, "//input[@id='billing_address']").send_keys("test")
driver.find_element(By.XPATH, "//select[@id='billing_country']").send_keys("Algeria")
driver.find_element(By.XPATH, "//input[@name='postcode']").send_keys("23456")
driver.find_element(By.NAME, "prefecture").send_keys("12")
driver.find_element(By.ID, "street_address1").send_keys("test2")
driver.find_element(By.ID, "street_address2").send_keys("test3")

