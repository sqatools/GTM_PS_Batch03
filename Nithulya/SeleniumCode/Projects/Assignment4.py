from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
driver.implicitly_wait(10)

def getTicket():
    driver.find_element(By.XPATH,"//input[@type='radio' and @value='radio_678']").click()
    time.sleep(1)

def addDetails():
    driver.find_element(By.XPATH, "//input[@id = 'firstname' and @name ='firstname'][1]").send_keys("Sarah")
    driver.find_element(By.XPATH, "//input[@id = 'firstname' and @name ='firstname'][2]").send_keys("Khan")
    driver.find_element(By.XPATH, "//input[@id = 'birthday']").send_keys("11/03/2024")
    driver.find_element(By.XPATH, "//input[@id = 'male']").click()
    time.sleep(1)

def addPassangerDetails():
    driver.find_element(By.XPATH,"//select[@id='admorepass']//child::option[@value='4']").click()
    time.sleep(2)

def addTravelDetails():
    driver.find_element(By.XPATH,"//input[@id='roundtrip']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys('Cochin')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='destcity']").send_keys('Los Angeles')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='departdate']").send_keys('05/20/2024')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='returndate']").send_keys('06/20/2024')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='visadate']").send_keys('05/16/2024')
    time.sleep(1)

def addDelivaryOption():
    driver.find_element(By.XPATH, "//input[@id='eamil']").click()
    time.sleep(1)
def addBillingDetails():
    driver.find_element(By.XPATH,"//input[@id='billing_name']").send_keys("Sarah Khan")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys('5156611089')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("boydkimberly@example.com")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='billing_address']").send_keys("Unit 9212 Box 7443,Salt Lake City")
    time.sleep(1)
    driver.find_element(By.XPATH, "//select[@id='billing_country']//child::option[text()='United Kingdom']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='postcode']").send_keys('84148')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='street_address1']").send_keys("Unit 9212 Box 7443")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='street_address2']").send_keys("Salt Lake City")
    time.sleep(2)

def addVisitedCities():
    for box in range(2,9):
        if box%2 !=0:
            box1=driver.find_element(By.XPATH, f"//tr[{box}]//parent::td//child::input[@type='checkbox']")
            box1.click()
        else:
            pass
        time.sleep(1)



getTicket()
addDetails()
addPassangerDetails()
addTravelDetails()
addDelivaryOption()
addBillingDetails()
addVisitedCities()

driver.close()