import pytest
from dummyPageMClass import DummyBookingPage
from test_dummyPageData import *

@pytest.mark.usefixtures("get_Driver")
class TestDummyBookingWebsite:

    def test_dummy_Booking_Website(self):
        self.dp = DummyBookingPage(self.driver)
        self.dp.choose_option_Ticket()
        self.dp.get_FirstName(firstname)
        self.dp.get_LastName(lastname)
        self.dp.get_DateOfBirth(dob)
        self.dp.get_radioButtonSex()
        self.dp.get_AdditionalPassenger(additionalPassenger)
        self.dp.get_TravelTripDetails()
        self.dp.get_FromCity(FromCity)
        self.dp.get_DestinationCity(DestinationCity)
        self.dp.get_DepartureDate(DepartureDate)
        self.dp.get_ReturnDate(ReturnDate)
        self.dp.get_VisaInterviewDate(VisaInterviewDate)
        self.dp.get_dummyTicket()
        self.dp.enter_value_billing_name_field(billing_name)
        self.dp.enter_value_billing_phone(phone)
        self.dp.enter_value_billing_email(email)
        self.dp.get_valueBillingAddress(billingAddress)
        self.dp.select_country_name(country_name)
        self.dp.get_PostalCode(postalcode)
        self.dp.get_streetAddress1(address1)
        self.dp.get_streetAddress2(address2)
        self.dp.get_MostVisitedCity()






