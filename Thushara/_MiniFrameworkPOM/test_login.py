import random
import pytest
from SeleniumBase import *
from login_locators import *
from home_page import HomePage
from sign_in_page import LoginPage
from test_data import *



@pytest.mark.usefixtures("set_up_and_tear_down")
class TestLogin:
    def test_login_with_valid_credential(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        sb = SeleniumBase(self.driver)
        hp.click_element(sign_in_locator)
        lp.enter_value_to_email_field(valid_email)
        lp.enter_value_to_password_field(valid_password)
        lp.click_sign_in_button()
        element= sb.get_element(sign_in_success_locator)
        assert element.is_displayed()
        #assert element.text.__contains__(sign_in_displayed_message)

    def test_login_with_invalid_email_valid_password(self):
        sb = SeleniumBase(self.driver)
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        hp.click_element(sign_in_locator)
        lp.enter_value_to_email_field(self.random_email())
        lp.enter_value_to_password_field(valid_password)
        lp.click_sign_in_button()
        element = sb.get_element(invalid_email_password_error_message_locator)
        assert element.is_displayed()

    def test_login_with_valid_email_invalid_password(self):
        sb = SeleniumBase(self.driver)
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        hp.click_element(sign_in_locator)
        lp.enter_value_to_email_field(valid_email)
        lp.enter_value_to_password_field(invalid_password)
        lp.click_sign_in_button()
        element = sb.get_element(invalid_email_password_error_message_locator)
        assert element.is_displayed()


    def test_login_with_no_credentials(self):
        sb = SeleniumBase(self.driver)
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        hp.click_element(sign_in_locator)
        lp.enter_value_to_email_field("")
        lp.enter_value_to_password_field("")
        lp.click_sign_in_button()
        element = sb.get_element(email_field_required_locator)
        assert element.text.__contains__(no_credential_expected_warning_message)
        element1 = sb.get_element(password_field_required_locator)
        assert element1.is_displayed()

    def random_email(self):
        num = random.randint(10,90)
        num =str(num)
        return 'thushara'+ num +'@gmail.com'