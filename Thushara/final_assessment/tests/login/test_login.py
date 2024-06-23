import pytest
from modules.LoginPageClass import LoginPage
from modules.login.login_page_data import *


@pytest.mark.usefixtures("set_up_and_tear_down")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.lp = LoginPage(self.driver)

    def test_login_with_invalid_user_name(self):
        lp = LoginPage(self.driver)
        lp.click_sign_in()
        lp.enter_value_to_username_field(valid_username)
        lp.enter_value_to_password_field(valid_password)
        lp.click_submit_btn()
        element= lp.invalid_email_message()
        assert element.is_displayed()

    def test_login_with_invalid_password(self):
        lp = LoginPage(self.driver)
        lp.click_sign_in()
        lp.enter_value_to_username_field(valid_username)
        lp.enter_value_to_password_field(valid_password)
        lp.click_submit_btn()
        element= invalid_password_message()
        assert element.is_displayed()

    def test_login_with_valid_credential(self):
        lp = LoginPage(self.driver)
        lp.click_sign_in()
        lp.enter_value_to_username_field(valid_username)
        lp.enter_value_to_password_field(valid_password)
        lp.click_submit_btn()
        element=success_message()
        assert element.is_displayed()



