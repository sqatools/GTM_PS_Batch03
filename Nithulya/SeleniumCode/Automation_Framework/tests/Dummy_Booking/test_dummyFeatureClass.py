import pytest
from modules1.Dummy_Booking.dummyPageMClass import DummyBookingPage
from modules1.Dummy_Booking.test_dummyPageData import *

@pytest.mark.usefixtures("get_Driver")
class TestDummyBookingWebsite:

    @pytest.fixture(autouse=True)
    def setup(self,):
        self.dp = DummyBookingPage(self.driver)


    def test_dummy_Booking_Website(self):
        self.dp.navigate_to_dummy_booking_website()
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






