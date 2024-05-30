import pytest
from selenium import webdriver
from base.WebdriverFactory import WebdriverFactory


@pytest.fixture(scope="class")
def get_driver(request):
    wf = WebdriverFactory('Chrome')
    driver = wf.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()
