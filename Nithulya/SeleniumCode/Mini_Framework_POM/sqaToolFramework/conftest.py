import pytest
from selenium import webdriver
from test_dummyPageData import *


@pytest.fixture(scope="class")
def get_Driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(dummyWebsiteURL)
    request.cls.driver = driver