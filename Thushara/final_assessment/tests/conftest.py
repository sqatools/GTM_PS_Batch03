
import pytest
from base.WebdriverFactory import WebdriverFactory


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    wf = WebdriverFactory('Chrome')
    driver = wf.get_driver_instance()
    driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
    request.cls.driver = driver
    yield
    driver.close()

