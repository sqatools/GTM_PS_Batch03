import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://magento.softwaretestingboard.com/")
whats_new = driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-3' ]")
whats_new.click()
women = driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-4' ]")
women.click()
jacket = driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html' and text()='Jackets']")
jacket.click()
select = driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html']")
select.click()
size = driver.find_element(By.XPATH,"//div[@id='option-label-size-143-item-168']")
size.click()

color = driver.find_element(By.XPATH,"//div[@class='swatch-option color' and @option-label='Black']")
color.click()

add_to_cart=driver.find_element(By.XPATH,"//button[@type='submit' and @id='product-addtocart-button']")
add_to_cart.click()
time.sleep(2)

men=driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-5' ]")
men.click()
hoodies_and_sweatshirts = driver.find_element(By.XPATH,"//div[@class='widget block block-static-block']//following::a[@href='https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html']")
hoodies_and_sweatshirts.click()
select1 = driver.find_element(By.XPATH,"//a[@class='product-item-link' and @href='https://magento.softwaretestingboard.com/ajax-full-zip-sweatshirt.html']")
select1.click()
color1 = driver.find_element(By.XPATH,"//div[@class='swatch-option color' and @id='option-label-color-93-item-53']")
color1.click()
size1 = driver.find_element(By.XPATH,"//div[@class='swatch-option text' and @id='option-label-size-143-item-170']")
size1.click()
add_to_cart1 = driver.find_element(By.XPATH,"//button[@type='submit' and @title='Add to Cart']")
add_to_cart1.click()
time.sleep(2)

gear=driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-6' ]")
gear.click()
training=driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-7' ]")
training.click()
sale=driver.find_element(By.XPATH,"//a[@class='level-top ui-corner-all' and  @id='ui-id-8' ]")
sale.click()

cart=driver.find_element(By.XPATH,"//a[@class='action showcart' and @href='https://magento.softwaretestingboard.com/checkout/cart/']")
cart.click()


time.sleep(5)
driver.close()