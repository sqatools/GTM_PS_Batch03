import pytest
import random
from create_account_page import CreateAccount
from create_account_test_data import  *

@pytest.mark.usefixtures("set_up_and_tear_down")
class TestCreateAccount:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.ca = CreateAccount(self.driver)

    def test_create_account_with_required_fields(self):
        self.ca.click_create_account()
        self.ca.enter_value_to_first_name_field(first_name)
        self.ca.enter_value_to_last_name_field(last_name)
        self.ca.enter_value_to_email_field(self.random_email())
        self.ca.enter_value_to_password_field(password)
        self.ca.enter_value_to_confirm_password_field(confirm_password)
        element = self.ca.message_displayed()
        assert element.isdisplayed

    def test_create_account_with_duplicate_email(self):
        self.ca.click_create_account()
        self.ca.enter_value_to_first_name_field(['first_name'])
        self.ca.enter_value_to_last_name_field(['last_name'])
        self.ca.enter_value_to_email_field(self.random_email())
        self.ca.enter_value_to_password_field(['password'])
        self.ca.enter_value_to_confirm_password_field(['confirm_password'])
        element = self.ca.duplicate_email()
        assert element.isdisplayed
    def test_create_account_with_different_confirmation_password(self):
        self.ca.click_create_account()
        self.ca.enter_value_to_first_name_field(['firstname'])
        self.ca.enter_value_to_last_name_field(['lastname'])
        self.ca.enter_value_to_email_field(['emailid'])
        self.ca.enter_value_to_password_field(['pswd'])
        self.ca.enter_value_to_confirm_password_field(['confirm_pswd'])
        element = self.ca.confirm_password_error()
        assert element.isdisplayed
    # @pytest.mark.smoke
    def test_create_account_without_required_fields(self):
        self.ca.click_create_account()
        self.ca.enter_value_to_first_name_field('')
        self.ca.enter_value_to_last_name_field('')
        self.ca.enter_value_to_email_field('')
        self.ca.enter_value_to_password_field('')
        self.ca.enter_value_to_confirm_password_field('')
        element = self.ca.firstname_error()
        assert element.isdisplayed
        element = self.ca.lastname_error()
        assert element.isdisplayed
        element = self.ca.email_error()
        assert element.isdisplayed
        element = self.ca.password_error()
        assert element.isdisplayed
        element = self.ca.confirm_pswd_error()
        assert element.isdisplayed
    def random_email(self):
        num = random.randint(10, 900)
        num = str(num)
        return 'alayalatta' + num + '@gmail.com'

