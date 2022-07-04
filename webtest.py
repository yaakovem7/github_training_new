from selenium import webdriver

# Windows:
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:/Third/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(10) #will wait up to 10 ms for elements to exist


# Mac and linux:
#driver = webdriver.Chrome(executable_path="/users/user/chromedriver")

driver.get("https://translate.google.com")
print(driver.current_url)
print(driver.title)



#driver.find_element_by_class_name("er8xn") #old syntax
my_list=driver.find_elements(by=By.CLASS_NAME, value="er8xn") #new syntax, but required to import the by "import. will return 1, the amount of classname he found
print(len(my_list))

my_list=driver.find_elements(by=By.TAG_NAME, value="div") #new syntax, but required to import the by "import. will return 1, the amount of classname he found
print(len(my_list))

driver.find_element(by=By.CLASS_NAME, value="er8xn").send_keys("Hello")
driver.find_element(by=By.CLASS_NAME, value="er8xn").send_keys(Keys.F3)

#x= driver.find_element(by=By.CLASS_NAME, value="er8xn").is_displayed() #will diplay true or false
#print(x)



#driver.close()#close recent tab
#driver.quit() #will close the entire tabs