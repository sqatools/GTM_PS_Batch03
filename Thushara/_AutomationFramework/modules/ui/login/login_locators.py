from selenium.webdriver.common.by import By

sign_in_locator = (By.CSS_SELECTOR, "li.authorization-link>a")
email_field_locator = (By.CSS_SELECTOR, "input#email")
password_field_locator = (By.CSS_SELECTOR, "input[name='login[password]']")
sign_in_button_locator = (By.CSS_SELECTOR, "div+div>div.primary>button#send2")
sign_in_success_locator =(By.XPATH,"//span[contains(text(),'Welcome')]")
invalid_email_password_error_message_locator = (By.CSS_SELECTOR,"div[data-ui-id='message-error")
email_field_required_locator = (By.CSS_SELECTOR,"div#email-error")
password_field_required_locator=(By.CSS_SELECTOR,"div#pass-error")


log_in_options = (By.CSS_SELECTOR,"li[class='greet welcome']+li[class='customer-welcome']>span>button")
account_locator =(By.LINK_TEXT,"My Account")
wishlist_locator =(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/wishlist/']")
sign_out = (By.CSS_SELECTOR,"li[class='link wishlist']+li>a")