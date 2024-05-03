import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
username = driver.find_element(By.XPATH, "//input[@data-testid='royal_email']")
username.send_keys("testuser@gmail.com")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("Admin@12345")
login_button = driver.find_element(By.XPATH, "//button[@data-testid='royal_login_button']")
login_button.click()

incorrect_msg = driver.find_element(By.XPATH, """//div[text()="The password that you've entered is incorrect. "]""")
print(incorrect_msg.text)
assert "incorrect" in incorrect_msg.text
time.sleep(10)
driver.close()

# --------------------------------------------------------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/")
username = driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']")
username.send_keys("testuser@gmail.com")
password = driver.find_element(By.XPATH, "//input[@aria-label='Password']")
password.send_keys("Admin@12345")
login_button = driver.find_element(By.XPATH, "//button[@class='_acan _acap _acas _aj1- _ap30']")
login_button.click()
incorrect_msg = driver.find_element(By.XPATH, """//div[text()="The password that you've entered is incorrect. "]""")
print(incorrect_msg.text)
assert "incorrect" in incorrect_msg.text
time.sleep(10)
driver.close()


# --------------------------------------------------------------------------------------------------------------

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.snapchat.com/download")
username = driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']")
username.send_keys("testuser@gmail.com")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(10)
driver.close()


# --------------------------------------------------------------------------------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://brainly.in/login?entry=2&source=unlogged+homepage+header+button")
username = driver.find_element(By.XPATH, "//input[@placeholder='Username or email']")
username.send_keys("kykiran68@gmail.com")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("Kiran@123")
login_button = driver.find_element(By.XPATH, "//button[@class='sg-button__text']")
login_button.click()
incorrect_msg = driver.find_element(By.XPATH, """//div[text()="The password that you've entered is incorrect. "]""")
print(incorrect_msg.text)
assert "incorrect" in incorrect_msg.text
time.sleep(10)
driver.close()


# ---------------------------------------------------------------------------------------------------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://in.linkedin.com/?src=go-pa&trk=sem-ga_campid.14650114788_asid.151761418307_crid."
           "657403558715_kw.linkedin%20login_d.c_tid.kwd-12704335873_n.g_mt.e_geo.9302483&mcid=6844056167778418689&"
           "cid=&gad_source=1&gclid=CjwKCAjw88yxBhBWEiwA7cm6pUDV_e4eCvZ5zbHyttGMXW3bh_1DF_"
           "fsj4nc8IDQ6TG1KHP_2gBoJxoC44AQAvD_BwE&gclsrc=aw.ds")
username = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
username.send_keys("testuser@gmail.com")
password = driver.find_element(By.XPATH, "//input[@id='session_password']")
password.send_keys("Admin@12345")
login_button = driver.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn']")
login_button.click()
incorrect_msg = driver.find_element(By.XPATH, """//div[text()="The password that you've entered is incorrect. "]""")
print(incorrect_msg.text)
assert "incorrect" in incorrect_msg.text
time.sleep(10)
driver.close()



# ------------------------------------------------------------------------------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.pw.live/users/login")
username = driver.find_element(By.XPATH, "//input[@placeholder='test@example.com']")
username.send_keys("testuser@gmail.com")
password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys("Admin@12345")
login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
login_button.click()
incorrect_msg = driver.find_element(By.XPATH, """//div[text()="The password that you've entered is incorrect. "]""")
print(incorrect_msg.text)
assert "incorrect" in incorrect_msg.text
time.sleep(10)
driver.close()