import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

def select_browser(browser):
    if browser.lower() == 'chrome':
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('detach',True)
        driver1 = webdriver.Chrome(options=opts)
    elif browser.lower() == 'firefox':
        driver1 = webdriver.Firefox()
    elif browser.lower() == 'edge':
        driver1=webdriver.Edge()
    return driver1

driver = select_browser('chrome')
alert = Alert(driver)
driver.get("https://www.yatra.com/")
driver.maximize_window()
alert.dismiss()
driver.implicitly_wait(10)
movie =driver.find_element(By.XPATH,"//a[title='Mr & Mrs Mahi']/img[@class='conta iner large-banner']").click()


#driver.execute_script("arguments[0].click();",movie)





#driver.close()
