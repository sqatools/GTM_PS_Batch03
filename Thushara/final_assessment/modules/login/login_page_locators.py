from selenium.webdriver.common.by import By
user_name_locator = (By.XPATH,"//input[@id ='username']")
pass_word_locator = (By.CSS_SELECTOR,"input#password")
login_btn_locator =(By.XPATH,"//*[@id='submit']")
invalid_email_locator = (By.XPATH,"//*[@id='error']")
invalid_password_locator =(By.XPATH,"//*[@id='top']/div/div[2]")
success_message_locator=(By.XPATH,"//*[@id='content']/ul[1]/li[1]/a")