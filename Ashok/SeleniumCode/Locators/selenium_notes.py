"""
Locators:
---------
1. We can identify various elements on the webpage using locators.
2. Locators are addresses that identify a web element uniquely with in the page.

What are Locators Used For?
---------------------------
Locators are used to identify and navigate web elements on a webpage. Once an element is found,
we can perform various actions like clicking, typing, selecting, etc. Locators also verify an element’s
presence, absence, or visibility on a webpage.

Types of locators: There are to types of locators.

a. Locators:
------------
1. Below are the built-in locators which is directly supported by selenium webdriver
2. We can access all these locators as a method

▪ id
▪ name
▪ linkText
▪ Partial LinkText
▪ class
▪ TagName

b. Customized locators:
-----------------------
CSS Selector -
    ▪ Tag & ID (OR) #id
    ▪ Tag & class (OR) .class
    ▪ Tag & attribute (OR) [attribute=value]
    ▪ Tag , class & attribute

XPath -
    ▪ Absolute XPath
    ▪ Relative XPath

Xpath methods -
    ▪ and
    ▪ or
    ▪ contains()
    ▪ starts-with()
    ▪ text()

HTML Structure:
---------------ss
<input type="text" class="inputtext _55r1 _6luy" name="email" id="email" data-testid="royal_email"
placeholder="Email address or phone number" autofocus="1" aria-label="Email address or phone number">

TagName -> input,
name="email" -> name is Attribute and "email" is value
Attributes -> type, name, id, data-testid, placeholder,  autofocus, aria-label
"""
"""
#######################################################################################
ID:
---
# Used to find an element using its unique ID.
# The fastest and most reliable way to locate an element.
# Ideal when the ID of an element is unique on a webpage.

Ex:
---
<input class="search_query form-control ac_input" type="text" id="search_query_top" 
name="search_query" placeholder="Search" value autocomplete="off"> == $0

driver.find_element(By.ID, "search_query_top").send_keys("T-shirt")
######################################################################################

Name:
-----
# Used to find an element using its name attribute.
# Name attribute may not be unique, but it is commonly used to identify elements.

Ex:
---
<button type="submit" name="submit_search" class="btn btn-default button-search">...</button> == $0
Usage: driver.find_element(By.NAME, “button1”)

driver.find_element(By.NAME, "submit_search").click()
#######################################################################################

Class Name:
-----------
# Used to find an element using its class name.
# Multiple elements can have the same class name, but it is still a reliable way to locate elements.

Ex:
---
<ul id homeslider" style="max-height: 448px; width: 515%; position: relative; Left: 960px;"> == 50
<li class="homeslider-container bx-clone" style="float: left; list-style: none; position: relative; width: 480px;">
</li>
►<li class="homeslider-container" style="float: left; list-style: none; position: relative; width: 480px;">
</li>
<li class="homeslider-container" style "float: left; list-style: none; position: relative; width: 480px;">...
</ul>

sliders=driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(sliders))
#######################################################################################

Tag Name:
---------
# Used to find an element using its HTML tag name.
# Useful when only one element has a particular tag name

Ex: 
----
html tag: <a> 

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
#######################################################################################

Link Text:
---------- 

# Used to find an anchor element (a tag) with a specific link text.
# Used to identify links on a webpage.

Ex:
---
<a class="product-name" href="http://automationpractice.com/index.php?id_product=7&controller=product" title> 
Printed Chiffon Dress </a> == $0

driver.find_element(By.LINK_TEXT,"Printed Chiffon Dress").click()
#######################################################################################

Partial Link Text:
-----------------
# Used to find an anchor element (a tag) with partial link text.
# Used to identify links with a familiar pattern.

Ex:
---
<a class="product-name" href="http://automationpractice.com/index.php?id_product=7&controller=product" title> 
Printed Chiffon Dress </a> == $0

driver.find_element(By.PARTIAL_LINK_TEXT,"Chiffon Dress").click()
#######################################################################################

CSS Selector:
--------------
# Used to identify elements using CSS selectors.
# CSS selectors are used to define the style of elements on a webpage.

1. Tag and ID:          syntax: tagname#valueofId
------------
<input type="text" class="inputtext_55r1_6luy" name="email" id=
"email" data-testid="royal_email" placeholder="Email address or phone
number" autofocus="1" aria-label="Email address or phone number"> == $0

driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc@gmail.com")
(or)
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmail.com")

2. Tag and class:        syntax: tagname.valueofClass
-----------------
<input type="text" class="inputtext _55r1 _6luy" name="email" id=
email" data-testid="royal_email" placeholder="Email address or phone
" number" autofocus="1" aria-label="Email address or phone number"> == $0

driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")
(or)
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")


3. Tag and attribute:    syntax: tagname[attribute=value]
---------------------
<input type="text" class="inputtext_55r1_6luy" name="email" id=
"email" data-testid="royal_email" placeholder="Email address or phone
number" autofocus="1" aria-label="Email address or phone number"> == $0

driver.find_element(By.CSS_SELECTOR,"[name=email]").send_keys("abc@gmail.com")
(or)
driver.find_element(By.CSS_SELECTOR,"input[name=email]").send_keys("abc@gmail.com")


4. Tag, class and attribute:   syntax: tagname.valueofClass[attribute=value]
----------------------------
<div class="_6lux">
<input type="text" class="inputtext_55r1_6luy" name= "email" id="email" data-testid="royal_email" 
placeholder= "Email address or phone number" autofocus="1" aria-label= "Email address or phone number" style>
</div>
<div class="_6lux">
<input type="password" class="inputtext_55r1_6luy" name= "pass" id="pass" data-testid="royal_pass" placeholder=
"Password" aria-label="Password">
</div>

driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("abc@gmail.com") #Email
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("abc") #Password

#################################################################################################################

XPath:
-------
XPath is defined as XML path.
▪ It is a syntax or language for finding any element on the web page using XML path expression.
▪ XPath is used to find the location of any element on a webpage using HTML DOM structure.
▪ XPath can be used to navigate through elements and attributes in DOM.

DOM - Document Object Model
---------------------------
DOM is an API Interface provided by browser.
▪ When a web page is loaded, the browser creates a Document Object Model of the page

Absolute XPath:
---------------
It is the direct way to find the element.
▪ The disadvantage of the absolute XPath is that if there are any changes made in the path of the element then
that XPath gets failed.
▪ It begins with the single forward slash(/) ,which means you can select the element from the root node.
▪ Below is the example of an absolute XPath expression of the element

▪ Ex:
Absolute Xpath : /html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[1]/a[1]/img[1]

Relative XPath:
---------------
Relative XPath the path starts from the middle of the HTML DOM structure.
▪ It starts with the double forward slash (//), which means it can search the element anywhere at the webpage.
▪ You can start from the middle of the HTML DOM structure and no need to write long XPath.

Ex:
Relative Xpath : //img[@class='logo img-responsive']

Syntax for Relative XPath:
--------------------------
XPath contains the path of the element situated at the web page. Standard syntax for creating XPath is

Xpath=//tagname[@attribute='value']

▪ // : Select current node.
▪ Tagname: Tagname of the particular node.
▪ @: Select attribute.
▪ Attribute: Attribute name of the node.
▪ Value: Value of the attribute.

XPath with OR:
--------------
<div class="form-group">
<input type="text" placeholder="Company Name" name= "organization_name" value class="form-control xpath="1"> == $0 style
</div>

driver.find_element(By.XPATH,"//input[@name='organization_name' or 
                    @placeholder='Organization']").send_keys("abc")

XPath with AND:
---------------
<div class="form-group">
<input type="text" placeholder="Full Name*" name="name" value required="required" class= "form-control xpath="1"> == $0
</div>

driver.find_element(By.XPATH,"//input[@name='name' and @placeholder='FullName*']").send_keys("abc")

XPath with contains():
  1. contains function will have two parameters
  2. Ex: will use for dynamic elements(button name can be Start/Stop)
----------------------
<a class="nav-link" href="https://accounts.lambdatest.com/register" onclick=onStartTesting()" 
xpathtest="1" style xpath="1">...</a>

driver.find_element(By.XPATH,"//a[contains(text(), 'Testing')]")
driver.find_element(By.XPATH,"//a[contains(@id, ‘value’)]")

XPath with starts-with():
  1. starts-with function will have two parameters
  2. Ex: will use for dynamic elements(button name can be Start/Stop)
-------------------------
<a class="nav-link" href="https://accounts.lambdatest.com/register" onclick=onStartTesting()" 
xpathtest="1" style xpath="1">...</a>

driver.find_element(By.XPATH,"//a[starts-with(text(), 'Start')]")
driver.find_element(By.XPATH,"//a[starts-with(@name,'value')]")

XPath with Text():
------------------
<li class="nav-item">
<a class="nav-link" href="https://www.lambdatest.com/pricing" xpathtest="1" 
xpath="1" style>...</a> == $0 </li>

driver.find_element(By.XPATH,"//a[text()='Pricing']")

X Path Axes:
------------
▪ XPath axes are those axes that are used to search for the multiple nodes in the XML document
from the current node context.

▪ These methods are mainly used when the web element is not identified with the help of ID,
name, class name, link text, CSS selector and XPath, etc. locators.

###############################################################################################

Webdriver commands:
-------------------


"""
