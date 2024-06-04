from base.Base_Google_Search import SeleniumBase1
from modules.searchLogin.pageLocator import *

class GoogleSearchP(SeleniumBase1):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def open_google_website(self, URL):
        self.driver.get(URL)
    def enterValuetoSearch(self,searchValue):
        self.enterValue(searchValue,searchFieldLocator)  # Calling the SeleniumBase1 class method here
    def clickSearchButton(self):
        self.clickElement(searchGoogleButton)   # Calling the SeleniumBase1 class method here

