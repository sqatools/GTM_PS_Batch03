import pytest
from selenium import webdriver
from Test_data import *


@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)  # getting the url from Test_data file
    request.cls.cdriver = driver
