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
# driver.find_element(By.XPATH, "//button[text()='Login']").click()
# time.sleep(5)


#2).
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
text_msg=driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/companies/quantum-digital-vis/10650010']")
text_msg.click()
time.sleep(2)
selectMutual=driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/mutual-funds']").click()
time.sleep(2)
selectMutualSel=driver.find_element(By.XPATH,"//input[@name='radioBtn' and @value='M']").click()
time.sleep(2)
selectMutualSel=driver.find_element(By.XPATH,"//input[@name='simpleBtn' and @value='Submit']").click()
time.sleep(2)
selectMutualSel2=driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/mutual-funds/Nippon-India-Nifty-Next-50-Junior-BeES-FoF-Direct-Plan/140516420/2066']").click()
time.sleep(4)
driver.close()



