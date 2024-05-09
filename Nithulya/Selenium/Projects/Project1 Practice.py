#1).
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys("Admin")
# driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys("admin123")
# driver.find_element(By.XPATH, "//button[text()='Login']").click()
# time.sleep(5)

#3).
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://money.rediff.com/gainers/bse/daily/groupall")

########### Parent : ################################################################################################
# parent1 = driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/companies/neil-industries/17024015']/parent::td").text
# print('Parent : ',parent1)               # Parent :  Neil Industries

########## Child #################################################################################################
# childs1 = driver.find_elements(By.XPATH,"//a[@href='//money.rediff.com/companies/neil-industries/17024015']/ancestor::tr/child::td")
# print('Number of child elements : ',len(child11))                # Number of child elements :  5

########### Ancestor ################################################################################################
# ancestor1 = driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/companies/neil-industries/17024015']/ancestor::tr").text
# print("Text of ancestor node : ",ancestor1)         # Text of ancestor node :  Neil Industries X 16.05 19.25 + 19.94

########## Descendant ##################################################################################################
# descendant1 = driver.find_elements(By.XPATH,"//a[@href='//money.rediff.com/companies/neil-industries/17024015']/ancestor::tr/descendant::*")
# print("Number of descendant nodes : ",len(descendant1))             # Number of descendant nodes :  7

######### Following ####################################################################################################
# following1 = driver.find_elements(By.XPATH,"//a[@href='//money.rediff.com/companies/neil-industries/17024015']/ancestor::tr/following::*")
# print('Number of following elements : ',len(following1))                 # Number of following elements :  16045

########### Following-sibling ##########################################################################################
# followingSibling1 = driver.find_elements(By.XPATH,"//a[@href='//money.rediff.com/companies/neil-industries/17024015']/ancestor::tr/following-sibling::*")
# print('Number of following-sibling elements : ',len(followingSibling1))       # Number of following-sibling elements :  1987

######## Preceeding ##################################################################################################
# preceding1 = driver.find_elements(By.XPATH,"//a[@href='//money.rediff.com/companies/neil-industries/17024015']/ancestor::tr/preceding::*")
# print('Number of preceding elements : ',len(preceding1))               # Number of preceding elements :  244

######## Preceeding-Sibling ##################################################################################################
# precedingSibling1 = driver.find_elements(By.XPATH,"//a[@href='//money.rediff.com/companies/neil-industries/17024015']/ancestor::tr/preceding-sibling::*")
# print('Number of preceding-sibling elements : ',len(precedingSibling1))      # Number of preceding-sibling elements :  10
#
# driver.close()

#2).
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
# text_msg=driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/companies/quantum-digital-vis/10650010']")
# text_msg.click()
# time.sleep(2)
# selectMutual=driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/mutual-funds']").click()
# time.sleep(2)
# selectMutualSel=driver.find_element(By.XPATH,"//input[@name='radioBtn' and @value='M']").click()
# time.sleep(2)
# selectMutualSel=driver.find_element(By.XPATH,"//input[@name='simpleBtn' and @value='Submit']").click()
# time.sleep(2)
# selectMutualSel2=driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/mutual-funds/Nippon-India-Nifty-Next-50-Junior-BeES-FoF-Direct-Plan/140516420/2066']").click()
# time.sleep(4)
# driver.close()



