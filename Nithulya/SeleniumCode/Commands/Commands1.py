'''
Commands:
1. Application Commands
2.Conditional Commands
3.Browser Commands
4.Navigational Commands
5.Wait Commands
----------------------------------------------------------------------------------------------------------------------
1). Application Commands :
     a) get() - opening the application url
     b) title(keyword) - to capture the title of the current webpage
     c) current_url - to capture the url of the current webpage
     d) page_source - to capture the source code of the current webpage
2). Conditional Commands :
    a) is_displayed() - method (check whether element is available or not)
    b) is_enabled() - (check whether the element is enabled or diabled)
    c) is_selected() - for radio buttons and check boxes whether it is selected or not
3). Browser Commands :
    a) close() - close single browser window(where driver focused)
    b) quit() - close multiple browser windows (This will kill the process)
4). Navigational Commands :
    a) back()
    b) forward()
    c) refresh

'''
import time

#1).Application Commands :
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# print('Title: ',driver.title)
# print('URL of Website : ',driver.current_url)
# print('Page Source : \n',driver.page_source)
# driver.close()

#2). Conditional Commands :
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://demo.nopcommerce.com/register")
# driver.maximize_window()
# searchBox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# print('Display status : ',searchBox.is_displayed())           # Display status :  True
# print('Enable status : ',searchBox.is_enabled())              # Enable status :  True
# # is_selected() - for radio buttons and check boxes :
# rdMale = driver.find_element(By.XPATH,"//input[@id='gender-male']")
# rdFemale = driver.find_element(By.XPATH,"//input[@id='gender-female']")
#
# print('Before selecting male radio button : ',rdMale.is_selected())       # Before selecting male radio button :  False
# print('Before selecting female radio button : ',rdFemale.is_selected())   # Before selecting female radio button :  False
#
# rdMale.click()
# print('After selecting male radio button : ',rdMale.is_selected())        # After selecting male radio button :  True
# print('Female radio button : ',rdFemale.is_selected())                    # Female radio button :  False
#
# rdFemale.click()
# print('Male radio button : ',rdMale.is_selected())                        # Male radio button :  False
# print('After selecting female radio button : ',rdFemale.is_selected())    # After selecting female radio button :  True
# driver.close()


#3). Browser Commands :
#1). close()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element(By.XPATH,"//a[@href='http://www.orangehrm.com']").click()
# time.sleep(6)
# driver.close()

#2).quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element(By.XPATH,"//a[@href='http://www.orangehrm.com']").click()
# time.sleep(6)
# driver.quit()

#4). Navigational Commands :
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://snapdeal.com/")             # snapdeal
# driver.get("https://www.amazon.jobs/en/")       # amazon
# time.sleep(2)
# driver.back()                                   # snapdeal
# driver.forward()                                # amazon
# driver.refresh()                                # refresh
# driver.quit()


