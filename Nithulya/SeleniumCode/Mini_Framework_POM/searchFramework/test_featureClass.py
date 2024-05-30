import pytest
from pageModuleClass import GoogleSearchP
from test_Data import *

@pytest.mark.usefixtures("get_driver")
class TestGoogleSeach:

    def test_searchOnGoogle(self):
        self.gp = GoogleSearchP(self.driver)
        self.gp.enterValuetoSearch(searchValue)
        self.gp.clickSearchButton()



