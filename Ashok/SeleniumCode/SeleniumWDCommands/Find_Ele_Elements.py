"""
findElement: A command to uniquely identify a web element within the web page.
-----------
1. Returns the first matching web element if the locator discovers multiple web elements
2. Throws NoSuchElementException if the element is not found
3. Detects a unique web element

findElements: A command to identify a list of web elements within the web page.
------------
1. Returns a list of multiple matching web elements
2. Returns an empty list if no matching element is found
3. Returns a collection of matching elements

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Locator matching with single web element
element = driver.find_element(By.ID, "small-searchterms")
element.send_keys("Apple MacBook Pro 13-inch")

# Locator matching with multiple elements - As we are using find element, so it returns first element only
element1 = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(element1.text)   # prints first link from the footer "Sitemap"

# Element not available then throw NoSuchElementException
# element2 = driver.find_element(By.LINK_TEXT, "Log")
# element2.click()

# FindElements - Locator matching with single web element
element3 = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
print(len(element3))   # 1
element3[0].send_keys("Apple MacBook Pro 13-inch")

# FindElements - Locator matching with multiple webelements
element4 = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(element4))      # 23
print(element4[1].text)   # Shipping & returns

# FindElements - Element is not available
element5 = driver.find_elements(By.LINK_TEXT, "Log")
print(len(element5))   # 0







