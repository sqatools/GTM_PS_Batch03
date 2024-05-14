'''
find_element() : Return single webelement. find_element returns a webelement object
find_elements() : Return multiple webelement. find_elements returns a list collections object.
find_element()     vs  find_elements()
text vs get_attribute('value')
text --> Returns inner text of the element.If inner text is not available returns nothing.
get_attribute('value') --> Returns values of any attribute of web element.
eg:get_attribute('id') - 'id' value will return, get_attribute('class') - class value will return.

'''

#1). find_element() :
#1 - Locator matching with the single webelement :
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register")
# element1 = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")    # value 1 of 1, and printing the same web-element
# time.sleep(2)
# element1.send_keys("Apple MacBook Pro 13-inch")
# time.sleep(1)
# driver.close()

########################################################################################################################
#2 - Locator matching with the multiple webelements :
import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register")
# element1 = driver.find_element(By.XPATH,"//div[@class='footer']//a")    # value 1 of 23 but printing the first web-element
# print(element1.text)                # Sitemap - prints first link from the footer

########################################################################################################################
#3) - Element not available then throw NoSuchElementException :
# #(element1 = driver.find_element(By.LINK_TEXT,"Log in") - We will get the same web-element,Instead of that if made any mistakes in text -
# # it provides NoSuchElementException)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register")
# element1 = driver.find_element(By.LINK_TEXT,"Log")
# element1.click()            # selenium.common.exceptions.NoSuchElementException

########################################################################################################################
########################################################################################################################
#1). find_elements() :
#1 - Locator matching with the single webelement :
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register")
# element1 = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")    #(element1 is list object)
# print('Counting how many items in the list : ',len(element1))       # Counting how many items in the list :  1
# element1[0].send_keys("Apple MacBook Pro 13-inch")
# time.sleep(1)
# driver.close()

########################################################################################################################
#2 - Locator matching with the multiple webelements :
import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register")
# element1 = driver.find_elements(By.XPATH,"//div[@class='footer']//a")    # value 1 of 23 and printing all 23 web-element
# print('Counting how many items in the list : ', len(element1))      # Counting how many items in the list :  23
# print('First web-element : ',element1[0].text)                      # First web-element :  Sitemap
# print('Last web-element : ',element1[22].text)                      # Last web-element :  nopCommerce
# print('-'*40)
# #(If I need to print all the 23 text,)
# print('All the 23 text :')
# for texts in element1:
#     print(texts.text)

#driver.close()

########################################################################################################################
#3) - Element not available :
# #(element1 = driver.find_elements(By.LINK_TEXT,"Log in") - We will get the same web-element,Instead of that if made any mistakes in text -
# # it provides '0')
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register")
# element1 = driver.find_elements(By.LINK_TEXT,"Log")
# print('Counting how many items in the list : ', len(element1))         # Counting how many items in the list :  0
#
# driver.close()

########################################################################################################################
########################################################################################################################
# text vs get_attribute()

#1).
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/login")
# emailBox = driver.find_element(By.XPATH,"//input[@id='Email']")
# emailBox.clear()
# emailBox.send_keys('abc@gmail.com')
# print('Result of the text : ',emailBox.text)                               # Result of the text :
# print('Result of the get_attribute() : ',emailBox.get_attribute('value'))  # Result of the get_attribute() :  abc@gmail.com

#driver.close()

#2.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/login")
# loginButton = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
# print('Result of the text : ',loginButton.text)        # Result of the text :  LOG IN
# print('Result of the get_attribute() : ',loginButton.get_attribute('value'))  # Result of the get_attribute() :
# print('Result of the get_attribute() : ',loginButton.get_attribute('type'))   # Result of the get_attribute() :  submit


