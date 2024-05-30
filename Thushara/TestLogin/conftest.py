
import pytest
from selenium import webdriver
from test_data import *


@pytest.fixture()
def set_up_and_tear_down(request):
    """
    browser = browser1
    if browser.lower().__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.lower().__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.lower().__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid name")
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.close()
