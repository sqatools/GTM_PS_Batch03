
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://collegedunia.com/engineering/indore-colleges")
list_of_colleges = driver.find_elements(By.XPATH,"//tbody[@class='jsx-4033392124 jsx-1933831621']//div/a[@href and @title]")
print("####",len(list_of_colleges))
count=1
for college in list_of_colleges:
    print("Number : ",count)
    print("College Name :", college.get_attribute("data-csm-title"))
    print("college Link :", college.get_attribute('href'))
    count+=1



#driver.close()
time.sleep(10)