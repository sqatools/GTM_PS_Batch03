from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
driver.implicitly_wait(10)

select1=driver.find_element(By.XPATH,"//input[@id='search']").send_keys("women's top")
search1=driver.find_element(By.XPATH,"//button[@type='submit' and @aria-label='Search']").click()

selectTop1=driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/gabrielle-micro-sleeve-top.html']").click()
time.sleep(1)
searchSize=driver.find_element(By.XPATH,"//div[@id='option-label-size-143-item-167']").click()
time.sleep(1)
searchColor=driver.find_element(By.XPATH,"//div[@id='option-label-color-93-item-50']").click()
time.sleep(1)
selectClick=driver.find_element(By.XPATH,"//span[text()='Add to Cart']").click()
time.sleep(3)

selectNext = driver.find_element(By.XPATH,"//span[text()='Men']").click()
selectDress1 = driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/geo-insulated-jogging-pant.html' and @class='product-item-link']").click()
time.sleep(1)
selectSize2 = driver.find_element(By.XPATH,"//div[@option-id='178' and @option-tooltip-value='36']").click()
time.sleep(1)
selectColor2 = driver.find_element(By.XPATH,"//div[@option-id='53' and @option-label='Green']").click()
time.sleep(1)
selectClear2 = driver.find_element(By.XPATH,"//input[@name='qty' and @class='input-text qty']").clear()
time.sleep(1)
selectQuantity2 = driver.find_element(By.XPATH,"//input[@name='qty' and @class='input-text qty']").send_keys(2)
SelectSubmit2=driver.find_element(By.XPATH,"//button[@type='submit']//parent::span[text()='Add to Cart']").click()
time.sleep(3)

SelectFitEq=driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/gear.html' and @role='menuitem']")
SelectFitEq.click()
time.sleep(3)
SelectFitEq1=driver.find_element(By.XPATH,"//ol[@class='items']//ancestor::a[@href='https://magento.softwaretestingboard.com/gear/fitness-equipment.html' and text()='Fitness Equipment']").click()
time.sleep(2)
SelectItem3=driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/set-of-sprite-yoga-straps.html' and @class='product photo product-item-photo']")
SelectItem3.click()
time.sleep(2)
SelectClear3=driver.find_element(By.XPATH,"//input[@type='number' and @data-errors-message-box='#validation-message-box' and @name='super_group[33]']").clear()
time.sleep(1)
SelecQty1=driver.find_element(By.XPATH,"//input[@type='number' and @data-errors-message-box='#validation-message-box' and @name='super_group[33]']").send_keys(2)
SelectSubmit3=driver.find_element(By.XPATH,"//button[@id='product-addtocart-button']").click()
time.sleep(3)

SelectTraining=driver.find_element(By.XPATH,"//a[@id='ui-id-7']")
SelectTraining.click()
time.sleep(1)

SelectSale=driver.find_element(By.XPATH,"//a[@id='ui-id-8']").click()
time.sleep(2)
SelectSale1=driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/promotions/women-sale.html']").click()
time.sleep(1)
SelectSale2=driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/josie-yoga-jacket.html' and @tabindex='-1']").click()
time.sleep(1)
SelectSaleSize=driver.find_element(By.XPATH,"//div[@id='option-label-size-143-item-167']").click()
time.sleep(1)
SelectSaleColor=driver.find_element(By.XPATH,"//div[@id='option-label-color-93-item-52']").click()
time.sleep(1)
SelectSaleQty=driver.find_element(By.XPATH,"//input[@id='qty']")
SelectSaleQty.clear()
time.sleep(1)
SelectSaleQty.send_keys(3)
time.sleep(2)
SelectAdd3=driver.find_element(By.XPATH,"//button[@id='product-addtocart-button']").click()
time.sleep(3)
selectHome1=driver.find_element(By.XPATH,"//a[@title='Go to Home Page']").click()
time.sleep(4)
selectCart=driver.find_element(By.XPATH,"//a[@class='action showcart'and @href='https://magento.softwaretestingboard.com/checkout/cart/']").click()
time.sleep(3)
selectCheckout=driver.find_element(By.XPATH,"//button[@id='top-cart-btn-checkout']").click()
time.sleep(2)
def getAddressDetails():
    driver.find_element(By.XPATH,"//input[@id='customer-email' and @class='input-text']").send_keys("boydkimberly@example.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='text' and @name='firstname']").send_keys("Sarah")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='text' and @name='lastname']").send_keys("Khan")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='text' and @name='company']").send_keys("Johnson, Kennedy and Garcia")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='text' and @name='street[0]']").send_keys("Unit 9212 Box 7443")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='text' and @name='city']").send_keys("Salt Lake City")
    time.sleep(1)
    driver.find_element(By.XPATH,"//option[@data-title='Utah']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@name='postcode']").send_keys('84148')
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@name='telephone']").send_keys('5156611089')
    time.sleep(3)
    selectShipping=driver.find_element(By.XPATH,"//td[@id='label_method_bestway_tablerate']")
    selectShipping.click()
    time.sleep(2)
    selectNext=driver.find_element(By.XPATH,'''//span[@data-bind="i18n: 'Next'"]''')
    selectNext.click()
    time.sleep(4)
def summaryReport():
    selectSummary=driver.find_element(By.XPATH,"//div[@class='opc-block-summary']").text
    with open('Assignment2Summary.txt','w') as file1Obj:
        for i in selectSummary:
            file1Obj.write(i)
def summaryRead():
    with open ('Assignment2Summary.txt','r') as file2Obj:
        file2=file2Obj.read()
        str = ' '
        for i in file2:
            str += i
    print(str)
    time.sleep(2)
def selectButton():
    selectOrder=driver.find_element(By.XPATH,"//button[@title='Place Order']")
    selectOrder.click()
    time.sleep(6)

getAddressDetails()
summaryReport()
summaryRead()
selectButton()
driver.close()
