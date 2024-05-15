"""
CSS Selector:
--------------
      Scenario          -  Syntax
      ----------------------------
    1) Tag #ID (OR) #id - tagname#valueofID or  #id
    2) Tag .class (OR) .class - tagname.valueofClass or .class
    3) Tag & attribute (OR) [attribute=value] - tagname[attribute=value] or [attribute=value]
    4) Tag, class & attribute - tagname.valueofClass[attribute=value]
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.facebook.com/")
driver.maximize_window()

##################  Tag#ID or #ID  ######################################

# driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("admin123")
# driver.find_element(By.CSS_SELECTOR,"#pass").send_keys("admin123")

################## Tag.class or .class ####################################
# Here, class = "inputtext _55r1 _6luy _9npi"  but spaces will create an error so taking first value before spaces

# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("admin123")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("admin123")

################ Tag & attribute (OR) [attribute=value] ##################################

# driver.find_element(By.CSS_SELECTOR, "input[name=pass]").send_keys("admin123")
# driver.find_element(By.CSS_SELECTOR, "[name=pass]").send_keys("admin123")

################# Tag, class and attribute ##################################
driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=pass]").send_keys("Admin123")
