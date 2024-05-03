import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/")

user_name = driver.find_element(By.XPATH,"//input[@aria-label='Phone number, username, or email']")
user_name.send_keys("etetr@guguy")
pass_wd = driver.find_element(By.XPATH,"//input[@aria-label='Password']")
pass_wd.send_keys("tdt5e65")
login = driver.find_element(By.XPATH,"//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
login.click()

incorrect_msg = driver.find_element(By.XPATH, "//div[text()='Sorry, your password was incorrect. Please double-check your password.']")
print(incorrect_msg.text)
assert "incorrect" in incorrect_msg.text
time.sleep(10)
driver.close()