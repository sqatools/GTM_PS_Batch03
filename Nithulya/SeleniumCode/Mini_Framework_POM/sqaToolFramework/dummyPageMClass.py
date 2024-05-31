from DummySeleniumBase import SeleniumBase1
from dummyPageLocator import *


class DummyBookingPage(SeleniumBase1):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def choose_option_Ticket(self):
        self.clickElement(choose_option_ticket_locator)

    def get_FirstName(self, firstname):
        self.enterValue(firstname, textBox_firstName_locator)

    def get_LastName(self, lastname):
        self.enterValue(lastname, textBox_lastName_locator)

    def get_DateOfBirth(self, dob):
        self.enterValue(dob, textBox_dateOfBirth_locator)

    def get_radioButtonSex(self):
        self.clickElement(radioButton_Male_locator)

    def get_AdditionalPassenger(self, additionalPassenger):
        self.select_dropdown_value(additionalPassenger, select_Passanger_locator)

    def get_TravelTripDetails(self):
        self.clickElement(radioButton_TravelDetails_locator)

    def get_FromCity(self, FromCity):
        self.enterValue(FromCity, textBox_FromCity_locator)

    def get_DestinationCity(self, DestinationCity):
        self.enterValue(DestinationCity, textBox_DestinationCity_locator)

    def get_DepartureDate(self, DepartureDate):
        self.enterValue(DepartureDate, textBox_DepartureDate_locator)

    def get_ReturnDate(self, ReturnDate):
        self.enterValue(ReturnDate, textBox_ReturnDate_locator)

    def get_VisaInterviewDate(self, VisaInterviewDate):
        self.enterValue(VisaInterviewDate, textBox_VisaInterviewDate_locator)

    def get_dummyTicket(self):
        self.clickElement(radioButton_receiveDummyTicket_locator)

    def enter_value_billing_name_field(self, billing_name):
        self.enterValue(billing_name, billing_name_field_locator)

    def enter_value_billing_phone(self, phone):
        self.enterValue(phone, billing_phone_field_locator)

    def enter_value_billing_email(self, email):
        self.enterValue(email, billing_email_field_locator)

    def get_valueBillingAddress(self, billingAddress):
        self.enterValue(billingAddress, billing_address_field_locator)

    def select_country_name(self, country_name):
        self.select_dropdown_value(country_name, country_dropdown_locator)

    def get_PostalCode(self, postalcode):
        self.enterValue(postalcode, textBox_zip_locator)

    def get_streetAddress1(self, address1):
        self.enterValue(address1, textBox_streetAddress1_locator)

    def get_streetAddress2(self, address2):
        self.enterValue(address2, textBox_streetAddress2_locator)

    def get_MostVisitedCity(self):
        self.clickElement(checkBox_MostVisitedCities_locator)
