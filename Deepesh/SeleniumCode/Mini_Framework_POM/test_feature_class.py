import pytest

from page_module_class import GooglePage
from test_data import *

@pytest.mark.usefixtures("get_driver")
class TestGoogleSeach:
    def test_search_on_google(self):
        self.gp = GooglePage(self.driver)
        self.gp.enter_value_to_search_field(search_value)
        self.gp.click_search_button()
