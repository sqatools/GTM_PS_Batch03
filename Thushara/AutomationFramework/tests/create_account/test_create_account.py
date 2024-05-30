import pytest
import random
from modules.create_account.create_account_page import CreateAccount
from modules.create_account.create_account_test_data import *
from base.SeleniumBase import SeleniumBase
from tests.conftest import *
from modules.create_account.create_account_locators import *


@pytest.mark.usefixtures("set_up_and_tear_down")
class TestCreateAccount:
    """"
    @pytest.fixture(autouse=True)
    def setup(self):
        self.ca = CreateAccount(self.driver)
        self.sb= SeleniumBase(self.driver)
    """

    def test_create_account_with_required_fields(self):
        self.ca = CreateAccount(self.driver)
        self.sb = SeleniumBase(self.driver)
        self.ca.click_create_account()
        self.ca.enter_value_to_first_name_field(first_name)
        self.ca.enter_value_to_last_name_field(last_name)
        self.ca.enter_value_to_email_field(self.random_email())
        self.ca.enter_value_to_password_field(password)
        self.ca.enter_value_to_confirm_password_field(confirm_password)
        self.ca.click_create_account_button()
        element = self.sb.get_element(success_message_locator)
        assert element.is_displayed()
    """
    def test_create_account_with_duplicate_email(self):
        self.ca = CreateAccount(self.driver)
        self.sb = SeleniumBase(self.driver)
        self.ca.click_create_account()
        self.ca.enter_value_to_first_name_field(duplicate_email['first_name'])
        self.ca.enter_value_to_last_name_field(duplicate_email['last_name'])
        self.ca.enter_value_to_email_field(duplicate_email['email'])
        self.ca.enter_value_to_password_field(duplicate_email['password'])
        self.ca.enter_value_to_confirm_password_field(duplicate_email['confirm_password'])
        self.ca.click_create_account_button()
        element = self.sb.get_element(error_message_duplicate_email_locator)
        assert element.is_displayed()

    def test_create_account_with_different_confirmation_password(self):
        self.ca = CreateAccount(self.driver)
        self.sb = SeleniumBase(self.driver)
        self.ca.click_create_account()
        self.ca.enter_value_to_first_name_field(wrong_confirmation_pswd['firstname'])
        self.ca.enter_value_to_last_name_field(wrong_confirmation_pswd['lastname'])
        self.ca.enter_value_to_email_field(wrong_confirmation_pswd['emailid'])
        self.ca.enter_value_to_password_field(wrong_confirmation_pswd['pswd'])
        self.ca.enter_value_to_confirm_password_field(wrong_confirmation_pswd['confirm_pswd'])
        self.ca.click_create_account_button()
        element = self.sb.get_element(error_confirm_password_locator)
        assert element.is_displayed()

    # @pytest.mark.smoke
    def test_create_account_without_required_fields(self):
        self.ca = CreateAccount(self.driver)
        self.sb = SeleniumBase(self.driver)
        self.ca.click_create_account()
        self.ca.enter_value_to_first_name_field('')
        self.ca.enter_value_to_last_name_field('')
        self.ca.enter_value_to_email_field('')
        self.ca.enter_value_to_password_field('')
        self.ca.enter_value_to_confirm_password_field('')
        self.ca.click_create_account_button()
        element = self.sb.get_element(firstname_error_locator)
        assert element.is_displayed()
        element = self.sb.get_element(lastname_error_locator)
        assert element.is_displayed()
        element = self.sb.get_element(email_error_locator)
        assert element.is_displayed()
        element = self.sb.get_element(password_error_locator)
        assert element.is_displayed()
        element = self.sb.get_element(confirm_password_error_locator)
        assert element.is_displayed()

    """

    def random_email(self):
        num = random.randint(10, 900)
        num = str(num)
        return 'alayalatta' + num + '@gmail.com'

