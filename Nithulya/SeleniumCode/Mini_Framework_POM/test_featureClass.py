import pytest

from pageModuleClass import GoogleSearchP
from test_Data import *

@pytest.mark.usefixtures("get_driver")
class TestGoogleSeach:

    def test_searchOnGoogle(self):
        self.GPage = GoogleSearchP(self.driver)
        self.GPage.enterValuetoSearch(searchValue)
        self.GPage.clickSearchButton()

