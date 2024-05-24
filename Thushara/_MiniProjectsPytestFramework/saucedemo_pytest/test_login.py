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
    yield
    driver.close()



@pytest.mark.smoke
def test_login_valid_credentials():
    user_name = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#user-name")
    user_name.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#password[name='password']")
    password.send_keys("secret_sauce")
    login=driver.find_element(By.CSS_SELECTOR,"div.form_group+div+div+input#login-button")
    login.click()
    message ='Products'
    assert driver.find_element(By.CSS_SELECTOR,"div.header_secondary_container>span").text.__contains__(message)


def test_login_invalid_username_valid_password():
    user_name = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#user-name")
    user_name.send_keys("abc")
    password = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#password[name='password']")
    password.send_keys("secret_sauce")
    login=driver.find_element(By.CSS_SELECTOR,"div.form_group+div+div+input#login-button")
    login.click()
    assert driver.find_element(By.CSS_SELECTOR,"div.error-message-container.error>h3").is_displayed()


def test_login_valid_username_invalid_password():
    user_name = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#user-name")
    user_name.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#password[name='password']")
    password.send_keys("123")
    login=driver.find_element(By.CSS_SELECTOR,"div.form_group+div+div+input#login-button")
    login.click()
    assert driver.find_element(By.CSS_SELECTOR,"div.error-message-container.error>h3").is_displayed()

@pytest.mark.smoke
def test_login_with_no_credentials():
    user_name = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#user-name")
    user_name.send_keys("")
    password = driver.find_element(By.CSS_SELECTOR,"div.form_group>input#password[name='password']")
    password.send_keys("")
    login=driver.find_element(By.CSS_SELECTOR,"div.form_group+div+div+input#login-button")
    login.click()
    message='Epic sadface: Username is required'
    assert driver.find_element(By.CSS_SELECTOR,"div.error-message-container.error>h3").text.__contains__(message)


