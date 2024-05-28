import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function', autouse=True)
def set_up_and_tear_down():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "div.form_group>input#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "div.form_group>input#password[name='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "div.form_group+div+div+input#login-button").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,"a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR,"button#checkout").click()
    yield
    driver.close()

@pytest.mark.smoke
def test_personal_details_with_all_fields():
    driver.find_element(By.CSS_SELECTOR,"input[class ='input_error form_input']#first-name").send_keys('Thushara')
    driver.find_element(By.CSS_SELECTOR, "div>div>input#last-name").send_keys("Anu")
    driver.find_element(By.CSS_SELECTOR, "div.form_group>input#postal-code").send_keys("2345")
    driver.find_element(By.CSS_SELECTOR, "div>input#continue").click()
    assert driver.find_element(By.CSS_SELECTOR,"div#header_container>div+div>span").is_displayed()

@pytest.mark.smoke
def test_personal_details_without_first_name():
    driver.find_element(By.CSS_SELECTOR, "input[class ='input_error form_input']#first-name").send_keys('')
    driver.find_element(By.CSS_SELECTOR, "div>div>input#last-name").send_keys("Anu")
    driver.find_element(By.CSS_SELECTOR, "div.form_group>input#postal-code").send_keys("4645")
    driver.find_element(By.CSS_SELECTOR, "div>input#continue").click()
    expected_error_message="Error: First Name is required"
    assert driver.find_element(By.CSS_SELECTOR, "div.error-message-container.error").text.__contains__(expected_error_message)


@pytest.mark.regression
def test_personal_details_without_last_name():
    driver.find_element(By.CSS_SELECTOR, "input[class ='input_error form_input']#first-name").send_keys('Thushara')
    driver.find_element(By.CSS_SELECTOR, "div>div>input#last-name").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "div.form_group>input#postal-code").send_keys("2345")
    driver.find_element(By.CSS_SELECTOR, "div>input#continue").click()
    expected_error_message = "Error: Last Name is required"
    assert driver.find_element(By.CSS_SELECTOR, "div.error-message-container.error").text.__contains__(expected_error_message)


def test_personal_details_without_postal_code():
    driver.find_element(By.CSS_SELECTOR, "input[class ='input_error form_input']#first-name").send_keys('Thushara')
    driver.find_element(By.CSS_SELECTOR, "div>div>input#last-name").send_keys("Anu")
    driver.find_element(By.CSS_SELECTOR, "div.form_group>input#postal-code").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "div>input#continue").click()
    expected_error_message="Error: Postal Code is required"
    assert driver.find_element(By.CSS_SELECTOR, "div.error-message-container.error").text.__contains__(expected_error_message)


@pytest.mark.smoke
def test_without_required_fields():
    driver.find_element(By.CSS_SELECTOR, "input[class ='input_error form_input']#first-name").send_keys('')
    driver.find_element(By.CSS_SELECTOR, "div>div>input#last-name").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "div.form_group>input#postal-code").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "div>input#continue").click()
    expected_error_message="Error: First Name is required"
    assert driver.find_element(By.CSS_SELECTOR, "div.error-message-container.error").text.__contains__(expected_error_message)



