import pytest
from modules1.searchLogin.pageModuleClass import GoogleSearchP
from modules1.searchLogin.test_Data import *

@pytest.mark.usefixtures("get_Driver")
class TestGoogleSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp = GoogleSearchP(self.driver)
        self.gp.open_google_website(URL)
    def test_search_google_website(self):
        self.gp.enterValuetoSearch(searchValue)
        self.gp.clickSearchButton()



