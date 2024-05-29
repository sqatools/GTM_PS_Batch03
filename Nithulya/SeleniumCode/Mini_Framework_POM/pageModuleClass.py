from SeleniumBase import SeleniumBase1
from pageLocator import *

class GoogleSearchP(SeleniumBase1):
    def __init__(self,driver):
        super().__init__(driver=driver)
    def enterValuetoSearch(self,searchValue):
        self.enterValue(searchValue,searchFieldLocator)
    def clickSearchButton(self):
        self.clickElement(searchGoogleButton)

