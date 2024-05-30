from SeleniumBase import SeleniumBase1
from pageLocator import *

class GoogleSearchP(SeleniumBase1):
    def __init__(self,driver):
        super().__init__(driver=driver)
    def enterValuetoSearch(self,searchValue):
        self.enterValue(searchValue,searchFieldLocator)  # Calling the SeleniumBase1 class method here
    def clickSearchButton(self):
        self.clickElement(searchGoogleButton)   # Calling the SeleniumBase1 class method here

