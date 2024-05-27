
import pytest
from selenium import webdriver

@pytest.fixture()
def set_up_and_tear_down(request):
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    driver.close()


