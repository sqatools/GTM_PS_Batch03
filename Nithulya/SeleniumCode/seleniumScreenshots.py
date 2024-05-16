'''
save_screenshot  - all kind of extension like .jpg,.png file
self.get_screenshot_as_file(filename) - only for .png file.
'''

#1.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# time.sleep(1)
# driver.save_screenshot(r"C:\PythonAutomation\GTM_PS_Batch03\Nithulya\SeleniumCode\Screenshot\HomePage1.jpg")
# driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys("Admin")
# admin1=driver.find_element(By.XPATH,'//input[@placeholder="Password"]')
# admin1.send_keys("admin123")
#admin1.screenshot(r"C:\PythonAutomation\GTM_PS_Batch03\Nithulya\SeleniumCode\Screenshot\Admin1.png")
# time.sleep(1)
# login1 = driver.find_element(By.CSS_SELECTOR, ".oxd-button ")
# login1.click()
# time.sleep(1)
# driver.save_screenshot(r"C:\PythonAutomation\GTM_PS_Batch03\Nithulya\SeleniumCode\Screenshot\HomePage2.png")
# time.sleep(5)
#
# driver.close()


#2.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from datetime import datetime
#
# driver = webdriver.Chrome()
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# t1 = time.time()
# element = driver.find_element(By.ID, "billing_name")
# element.send_keys("Mumbai")
# var1 = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
# driver.save_screenshot(f"C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\SeleniumCode\\Screenshot\\{var1}Dummy.png")
# element.screenshot(f"C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\SeleniumCode\\Screenshot\\{var1}Billing.png")
#
#
# time.sleep(2)
# driver.close()