import pytest
from selenium import webdriver
# from test_Data import *
from test_Data import *


@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)  # getting the url from Test_data file
    request.cls.driver = driver