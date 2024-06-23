import pytest

from selenium import webdriver


@pytest.fixture()
def setup(browser):
    driver = None
    if browser == "chrome":
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opt)
    elif browser == "firefox":
        opt = webdriver.FirefoxOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Firefox(options=opt)
    elif browser == "edge":
        opt = webdriver.EdgeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=opt)
    return driver


# this is a configuration method
def pytest_addoption(parser):  # This will get the value from CommandLine
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    _browser = request.config.getoption("--browser")  # request.config.getoption is pre-defined commands
    return _browser


# customizing the HTML Report
# It is a hook for Adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'Orange HRM'
    config._metadata['Module Name'] = 'Login Module'
    config._metadata['Tester Name'] = 'Ashok'


# It is a hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
