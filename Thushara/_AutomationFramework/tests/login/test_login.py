import pytest
from modules.login.sign_in_page import LoginPage
from modules.login.login_test_data import *
from utilities.random_email import RandomEmail






@pytest.mark.usefixtures("set_up_and_tear_down")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.lp=LoginPage(self.driver)
        self.re = RandomEmail()

    def test_login_with_valid_credential(self):
        self.lp.click_sign_in()
        self.lp.enter_value_to_email_field(valid_email)
        self.lp.enter_value_to_password_field(valid_password)
        self.lp.click_sign_in_button()
        element= sb.get_element(sign_in_success_locator)
        assert element.is_displayed()
        #assert element.text.__contains__(sign_in_displayed_message)

    def test_login_with_invalid_email_valid_password(self):
        re = RandomEmail()
        self.lp.click_sign_in()
        self.lp.enter_value_to_email_field(self.re.random_email())
        self.lp.enter_value_to_password_field(valid_password)
        self.lp.click_sign_in_button()
        element = self.lp.invalid_email_message()
        assert element.is_displayed()

    def test_login_with_valid_email_invalid_password(self):
        self.lp.click_sign_in()
        self.lp.enter_value_to_email_field(valid_email)
        self.lp.enter_value_to_password_field(invalid_password)
        self.lp.click_sign_in_button()
        #element = sb.get_element(invalid_email_password_error_message_locator)
        element = self.lp.invalid_email_message()
        assert element.is_displayed()
    

    def test_login_with_no_credentials(self):
        self.lp.click_sign_in()
        self.lp.enter_value_to_email_field("")
        self.lp.enter_value_to_password_field("")
        self.lp.click_sign_in_button()
        element = self.lp.empty_email_field()
        assert element.text.__contains__(no_credential_expected_warning_message)
        element1 = self.lp.empty_password_field()
        assert element1.is_displayed()


