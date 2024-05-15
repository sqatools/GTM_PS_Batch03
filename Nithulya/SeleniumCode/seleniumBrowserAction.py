import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def multiBrowser(browser):
    if browser.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    # get current title
    title = driver.title
    print("Website title :", title)

    # get current URL of website
    current_url = driver.current_url
    print("Current URL :", current_url)

    driver.find_element(By.CSS_SELECTOR, "#fromcity").send_keys("Mumbai")
    driver.find_element(By.CSS_SELECTOR, "div>input#destcity").send_keys("Cochin")

    # check element is selected or not
    email_radio_button = driver.find_element(By.ID, "eamil")
    print("Email radio is selected :", email_radio_button.is_selected())
    email_radio_button.click()
    print("Email radio is selected :", email_radio_button.is_selected())

    checkbox = driver.find_element(By.XPATH, "//td[text()='Mumbai']//preceding-sibling::td/input")
    print("Checkbox is_displayed :", checkbox.is_displayed())
    print("Checkbox is_enabled :", checkbox.is_enabled())
    print("Checkbox is_selected :", checkbox.is_selected())
    checkbox.click()
    print("Checkbox is_selected :", checkbox.is_selected())

    # navigate to other website
    driver.get("https://www.facebook.com/")

    # get attribute
    username_elem = driver.find_element(By.ID, "email")
    placeholder_text = username_elem.get_attribute("placeholder")
    print("Placeholder text :", placeholder_text)
    print("Name attribute :", username_elem.get_attribute("name"))

    time.sleep(5)
    driver.close()


multiBrowser('Chrome')
