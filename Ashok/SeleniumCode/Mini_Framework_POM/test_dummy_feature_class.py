import pytest
from Dummy_module_page_class import DummyModulePage
from Dummy_page_testdata import *


@pytest.mark.usefixtures("get_driver")
class TestDummyTicketBookingWebsite:

    def test_dummy_ticket_booking(self):
        self.dmp = DummyModulePage(self.cdriver)
        self.dmp.check_radio_button()
        self.dmp.enter_pd_first_name(firstname)
        self.dmp.enter_pd_last_name(lastname)
