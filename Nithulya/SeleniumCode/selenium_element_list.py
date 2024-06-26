import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def multiBrowser(browser):
    if browser.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach',True)
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == 'firefox':
        webdriver.Firefox()
    elif browser.lower() == 'edge':
        webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    element_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for element in element_list:
        element.click()
        time.sleep(2)
    driver.close()

multiBrowser('Chrome')
