'''
Links :
--------------------------------
1). Internal Link
2). External Link
3). Broken Link : If the error code number is greater than or equal to 400,it is broken link.

'''

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)

#1).Click on link :
# driver.find_element(By.LINK_TEXT,'Digital downloads').click()
# time.sleep(1)
# driver.close()

#2). Find number of links in the page.
# allLinks = driver.find_elements(By.TAG_NAME,'a')
# print('Total number of links :',len(allLinks))              # Total number of links : 87
# time.sleep(1)
#(OR)
# allLinks = driver.find_elements(By.XPATH,'//a')
# print('Total number of links :',len(allLinks))                # Total number of links : 87
# time.sleep(1)
# driver.close()

#3). Print all the link names.
# allLinks = driver.find_elements(By.XPATH,'//a')
# print('Total number of links :',len(allLinks))                # Total number of links : 87
# for link in allLinks:
#     print('>> ',link.text)
# driver.close()


#################### Broken Link ####################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests as requests
# import time
#
# driver = webdriver.Chrome()
# driver.get("http://www.deadlinkcity.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# allLinks = driver.find_elements(By.TAG_NAME,'a')
# count = 0
# for link in allLinks:
#     url = link.get_attribute('href')
#     try:
#         res = (requests.head(url))
#     except:
#         None
#     if res.status_code >= 400:
#         print(url, ' is broken link.')
#         count += 1
#     else:
#         print(url, ' is valid link.')
# print('Total number of broken link : ',count)
# time.sleep(1)
# driver.close()

