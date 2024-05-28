import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(scope='function', autouse=True)
def setup():
    print(" 4 A function Execution initiated \n")
    yield
    print("\n  4 B function Execution completed \n")

@pytest.fixture(scope='module', autouse=True)
def setup_module():
    print(" 3 A module Execution initiated \n")
    yield
    print("\n 3 B module Execution completed \n")

@pytest.fixture(scope='session', autouse=True)
def setup_session():
    print("1 A session Execution initiated \n")
    yield
    print("\n 1 B session Execution completed \n")

@pytest.fixture(scope='package')
def setup_package():
    print(" 2  A package Execution initiated \n")
    yield
    print("\n 2 B package Execution completed \n")

@pytest.fixture(scope="module")
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in")
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope="class")
def get_selenium_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in")
    driver.implicitly_wait(10)
    request.cls.driver = driver




