from selenium import webdriver
from LoginPageObjects import LoginPage


class TestLogin:
    def test_login(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.maximize_window()
        self.driver.get("https://admin-demo.nopcommerce.com/login")

        self.lp = LoginPage(self.driver)
        self.lp.setUserName("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.clickLogin()
        self.act_title = self.driver.title
        self.driver.close()
        assert self.act_title == "Dashboard / nopCommerce administration"




