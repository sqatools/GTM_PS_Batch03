"""
XPATH :
XPath is defined as XML path. It is a syntax or language for finding any element on the web page using XML Path expression.
XPath is used to find the location of any element on a webpage using HTML DOM structure.
XPath is used to navigate through elements and attributes in DOM. (DOM - Document Object Model)
>>Types of XPath:
 1)Absolute XPath/Full XPath
 2).Relative/Partial XPath
    Ex: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login to ORANGE HRM image
    Full XPath:
          /html/body/div/div[1]/div/div[1]/div/div[1]/img
    Relative XPath:
          //*[@id="app"]/div[1]/div/div[1]/div/div[1]/img
>>Difference b/w Absolute & Relative XPath
  >Absolute XPath starts  from root html node, Relative XPath directly jump to element on DOM
  >Absolute XPath starts with /. Relative XPath starts with //
  >In Absolute XPath we use only tags/nodes.In Relative XPath we use attributes.
>>Syntax of writing Relative XPath:
  //tagname[@attribute='value'], If don't know the tagname, we can use *.
>>Reason to select Relative XPath
  1)If developer introduced a new element then Absolute XPAth will be broken.
  2)If the developer changed the location then Absolute XPath will be broke.
    Absolute XPath is unstable.

>>Basic XPath Methods:
    1) Text Method :  //tagname[text()= 'text value']
    2) Contains Method :
        //tagname[contains(text(), 'partial value')]
        //tagname[contains(@attribute, 'attribute value')]


"""
#1).
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.get("https://www.facebook.com/")
# driver.find_element(By.XPATH,"//input[@data-testid='royal_email']").send_keys("testuser@gmail.com")
# driver.find_element(By.XPATH,"//input[@data-testid='royal_pass']").send_keys('Admin@12345')
# login_button=driver.find_element(By.XPATH,"//Button[@data-testid='royal_login_button']").click()
# incorrect_msg = driver.find_element(By.XPATH, """//div[text()="The password that you've entered is incorrect. "]""")
# print(incorrect_msg.text)
# assert "incorrect" in incorrect_msg.text
#
# time.sleep(10)
# driver.close()

#2).
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.get("https://us.shein.com/?url_from=usgooglebrandshein_srsa_Shein01_20210124&cid="
#            "370313608&setid=25652838688&adid=494298278806&pf=GOOGLE&gad_"
#            "source=1&gclid=CjwKCAjw88yxBhBWEiwA7cm6pcKyic-4IL3ujo2CEdbs8VLgISYBvNVu2hG7d2vzXUpGYF3e35Cc1BoCf2sQAvD_BwE")
# driver.find_element(By.XPATH,'//div[@hidefocus="true"]').send_keys("tops")
# driver.find_element(By.XPATH,"//path[@clip-rule='evenodd']").click()
#
#
# time.sleep(10)
# driver.close()

#3).
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.walmart.com/")
driver.find_element(By.XPATH,'//input[@aria-autocomplete="list"]').send_keys("Apple")
driver.find_element(By.XPATH,"//button[@aria-label='Search icon']").click()


time.sleep(10)
driver.close()


###Basic XPath Methods

# 1) Text Method :  //tagname[text()= 'text value']
#                  //div[text()="The password that you've entered is incorrect. "]
#
# 2) Contains Method :
#                  //tagname[contains(text(), 'partial value')]
#                  //div[contains(text(), 'incorrect')]
#
#                  //tagname[contains(@attribute, 'attribute value')]
#                  //button[contains(@id, 'login')]
#                  //*[contains(@id, 'loginb')]
