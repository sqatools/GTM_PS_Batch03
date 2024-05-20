
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

def personalDetails():
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Sarah Khan")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("boydkimberly@example.com")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='phone']").send_keys('5156611089')
    time.sleep(1)
    driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys('Unit 9212 Box 7443\nSalt Lake City\nzip code: 84148')
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='male']").click()
    time.sleep(1)

def getDays():
    driver.find_element(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")
    for i in range(1,8):
        if i==1 or i==2 or i==4 or i==5:
            day11 = driver.find_element(By.XPATH, f"//div[{i}][@class='form-check form-check-inline']//child::input[@class='form-check-input' and @type='checkbox']")
            day11.click()
            time.sleep(1)
        else :
            pass
    time.sleep(1)
    for i in range(1,8):
        if i==4:
            day11 = driver.find_element(By.XPATH, f"//div[{i}][@class='form-check form-check-inline']//child::input[@class='form-check-input' and @type='checkbox']")
            day11.is_selected()
            day11.click()
            time.sleep(1)
        else :
            pass
    time.sleep(2)

def selectCountry():
    element1 = driver.find_element(By.XPATH,"//select[@id='country']")
    dropCountry = Select(element1)
    dropCountry.select_by_visible_text('Australia')
    time.sleep(2)
def selectColor():
    element1 = driver.find_element(By.XPATH,"//select[@id='colors']")
    dropCountry = Select(element1)
    dropCountry.select_by_index(1)
    time.sleep(2)
def getDate():
    driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys('19/05/2024')
    time.sleep(2)







personalDetails()
getDays()
selectCountry()
selectColor()
getDate()
driver.close()
