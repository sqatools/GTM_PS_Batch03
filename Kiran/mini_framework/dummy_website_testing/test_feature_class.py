import pytest

from feature_page_module import DummyModulePage
from test_data import *


@pytest.mark.usefixtures("get_driver")
class TestDummyTicketBookingWebsite:

    def test_dummy_ticket_booking(self):
        self.dmp = DummyModulePage(self.driver)
        self.dmp.check_radio_button()
        self.dmp.enter_pd_first_name(firstname)
        self.dmp.enter_pd_last_name(lastname)

