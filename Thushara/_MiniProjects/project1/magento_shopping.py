import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://magento.softwaretestingboard.com/")

def options(opt):
    if opt == 'new':
        driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-3' ]").click()
    elif opt=='women':
        driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-4' ]").click()
    elif opt == 'men':
        driver.find_element(By.XPATH, "//a[@class='level-top ui-corner-all' and  @id='ui-id-5' ]").click()
    elif opt=='gear':
         driver.find_element(By.XPATH, "//a[@class='level-top ui-corner-all' and  @id='ui-id-6' ]").click()
    elif opt =='training':
        driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-7' ]").click()
    else:
        print("Wrong choice")

def add_to_cart():
    add_to_cart = driver.find_element(By.XPATH,"//button[@type='submit' and @id='product-addtocart-button']")
    add_to_cart.click()
    time.sleep(2)
def mailing_address():
    email = driver.find_element(By.XPATH,"//fieldset[@id='customer-email-fieldset']//input[@class='input-text'and @id='customer-email']")
    email.send_keys("demo@gmail.com")


    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")
    first_name.send_keys("Abcd")

    last_name = driver.find_element(By.XPATH,"//input[@name='lastname']")
    last_name.send_keys("Efghi")

    company = driver.find_element(By.XPATH,"//input[@name='company']")
    company.send_keys("ABC")

    address1 = driver.find_element(By.XPATH,"//input[@name='street[0]']")
    address1.send_keys("23455")

    address2 = driver.find_element(By.XPATH,"//input[@name='street[1]']")
    address2.send_keys("Demo street")

    address3 = driver.find_element(By.XPATH,"//input[@name='street[2]']")
    address3.send_keys("Demo")

    city = driver.find_element(By.XPATH,"//input[@name='city']")
    city.send_keys("Abcde")

    select_province = driver.find_element(By.XPATH,"//select[@name='region_id']")
    select_province.click()
    select_province.send_keys("l")
    select_province.click()

    zip=driver.find_element(By.XPATH,"//input[@name='postcode']")
    zip.send_keys("70081")
    """
    country = driver.find_element(By.XPATH,"//select[@name='country_id']")
    country.click()
    country.send_keys("U")
    country.click()
    """


    phone = driver.find_element(By.XPATH,"//input[@name='telephone']")
    phone.send_keys("56_879_890")

def click_cart():
    driver.find_element(By.XPATH, "//a[@class='action showcart']").click()

def check_out():
    driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']").click()
def place_order():
    place_order = driver.find_element(By.XPATH,"//button[@title='Place Order']")
    place_order.click()

options('women')
jacket = driver.find_element(By.XPATH,"//a[text()='Jackets']")
jacket.click()
select = driver.find_element(By.XPATH,"//a[contains(text(), 'Juno Jacket ')]")
select.click()
size = driver.find_element(By.XPATH,"//div[@id='option-label-size-143-item-169']")
size.click()
color = driver.find_element(By.XPATH,"//div[@id='option-label-color-93-item-57']")
color.click()


add_to_cart()
options('women')


pants = driver.find_element(By.XPATH,"//a[text()='Pants']")
pants.click()
select1 = driver.find_element(By.XPATH,"//strong[@class='product name product-item-name']//parent::a[@href='https://magento.softwaretestingboard.com/ida-workout-parachute-pant.html']")
select1.click()
size1 = driver.find_element(By.XPATH,"//div[@id='option-label-size-143-item-172']")
size1.click()
color1 = driver.find_element(By.XPATH,"//div[@id='option-label-color-93-item-49']")
color1.click()
add_to_cart()

options('men')
hoodies_and_sweatshirts = driver.find_element(By.XPATH,"//a[text()='Hoodies & Sweatshirts']")
hoodies_and_sweatshirts.click()

select1 = driver.find_element(By.XPATH,"//*[contains(text(),'Ajax Full-Zip Sweatshirt')]")
select1.click()
color1 = driver.find_element(By.XPATH,"//div[@class='swatch-option color' and @id='option-label-color-93-item-53']")
color1.click()
size1 = driver.find_element(By.XPATH,"//div[@class='swatch-option text' and @id='option-label-size-143-item-170']")
size1.click()
add_to_cart()

options('gear')
bags = driver.find_element(By.XPATH,"//div[@class='block filter']//following::a[text()='Bags'][2]")
bags.click()
bag_select= driver.find_element(By.XPATH,"//img[@alt='Fusion Backpack']")
bag_select.click()
add_to_cart()
time.sleep(2)


options('training')
options('sale')

click_cart()

time.sleep(6)

check_out()

##################### Shipping Address #############
mailing_address()

shipping_method=driver.find_element(By.XPATH,"//td[@id='label_method_bestway_tablerate']")
shipping_method.click()

next=driver.find_element(By.XPATH,"//span[text()='Next']")
next.click()
time.sleep(10)

################ PLACING ORDER ###############
place_order()


time.sleep(6)
driver.close()