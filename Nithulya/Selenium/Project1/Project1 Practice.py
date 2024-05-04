#1).
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys("Admin")
# driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys("admin123")
# driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
# time.sleep(5)

#2).
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
text_msg=driver.find_element(By.XPATH,"//a[@contains(text(),'Quantum Digital Vis.')]/self::a").text
print(text_msg)
time.sleep(5)
driver.close()
