from selenium.webdriver.common.by import By

radio_button_locator = (By.XPATH, "//input[@value='radio_123']"),
firstname_locator = (By.XPATH, "[@id='firstname'][1]"),
lastname_locator = (By.XPATH, "[@id='firstname'][2]"),
dob_locator = (By.ID, "birthday"),
gender_locator = (By.ID, "male"),
additional_passengers_locator = (By.XPATH, "//select[@id='admorepass']"),
travel_locator = (By.ID, "//input[@id='oneway']"),
from_city_locator = (By.NAME, "fromcity"),
destination_city_locator = (By.NAME, "destcity"),
departure_date_locator = (By.NAME, "departdate"),
return_date_locator = (By.NAME, "returndate"),
interview_date_locator = (By.NAME, "visadate"),
receive_dummy_ticket_locator = (By.ID, "whatsapp"),
billing_name_locator = (By.ID, "billing_name"),
billing_phone_locator = (By.ID, "billing_phone"),
billing_email_address_locator = (By.ID, "billing_email"),
billing_street_address_locator = (By.ID, "billing_address"),
billing_country_locator = (By.XPATH, "//select[@id='billing_country']"),
billing_postcode_locator = (By.ID, "postcode"),
billing_street_address1_locator = (By.ID, "street_address1"),
city_option_locator = (By.XPATH, "//input[@type='checkbox'][1]")

