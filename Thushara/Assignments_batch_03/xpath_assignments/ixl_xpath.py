import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.ixl.com/")

explring = driver.find_element(By.XPATH,"//button[@class='explore-btn']")
explring.click()


sign_in = driver.find_element(By.XPATH,"//button[@aria-label='Sign in']")
sign_in.click()
user_name = driver.find_element(By.XPATH,"//input[@id='username']")
user_name.send_keys("fgdhghjj")
pass_word = driver.find_element(By.XPATH,"//input[@id='password']")
pass_word.send_keys("43refegeg")

sign = driver.find_element(By.XPATH,"//button[@name='signin']")
sign.click()

incorrect_msg = driver.find_element(By.XPATH, "//div[text()='Your username or password is incorrect']")
print(incorrect_msg.text)
assert "incorrect" in incorrect_msg.text


time.sleep(10)