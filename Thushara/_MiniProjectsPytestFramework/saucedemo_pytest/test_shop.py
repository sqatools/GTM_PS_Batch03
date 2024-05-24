import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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
    global wait
    wait = WebDriverWait(driver, 10, 2)
    driver.find_element(By.CSS_SELECTOR, "div.form_group>input#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "div.form_group>input#password[name='password']").send_keys("secret_sauce")
    login = driver.find_element(By.CSS_SELECTOR, "div.form_group+div+div+input#login-button")
    login.click()
    time.sleep(10)
    yield
    driver.close()


def test_select_item_add_to_cart():
    driver.find_element(By.CSS_SELECTOR, "a#item_4_title_link>div.inventory_item_name ").click()
    time.sleep(10)
    try:
        wait.until(ec.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR,"button#add-to-cart"))).click()
    except Exception as e :
        print(e)
    button = "Remove"
    assert driver.find_element(By.CSS_SELECTOR,"button#remove").text.__contains__(button)

@pytest.mark.smoke
def test_click_cart():
    driver.find_element(By.CSS_SELECTOR,"a.shopping_cart_link").click()
    assert driver.find_element(By.CSS_SELECTOR,"button#checkout").is_displayed()


def test_check_out():
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR,"button#checkout").click()
    message = "Checkout: Your Information"
    assert driver.find_element(By.CSS_SELECTOR,"div#header_container>div+div>span").text.__contains__(message)






