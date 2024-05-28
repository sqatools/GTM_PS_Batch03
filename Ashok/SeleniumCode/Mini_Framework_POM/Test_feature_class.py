import pytest

from Module_page_class import GooglePage
from Test_data import *


@pytest.mark.usefixtures("get_driver")
class TestGoogleSearch:
    def test_search_on_google(self):
        self.gp = GooglePage(self.cdriver)
        self.gp.enter_value_to_search(search_value)
        self.gp.click_search_button()
