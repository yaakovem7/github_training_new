#1
from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:/Third/chromedriver_win32/chromedriver.exe")

# driver.get("https://www.walla.com")

#2
# title1 = driver.title
# driver.refresh()
# title2 = driver.title
# if title1 == title2:
#     print ("same title")
# else:
#     print ("not same title")

#3
#yes -same element


#4
# driver.get("https://translate.google.com")
# driver.find_element(by=By.CLASS_NAME, value="er8xn").send_keys("my name is Yaakov")

#5
#driver.get("https://www.youtube.com/")
#driver.find_element(by=By.NAME, value="search_query").send_keys("Civil war")
#driver.find_element(by=By.ID, value="search-icon-legacy").click()
#driver.find_element_by_id("search-icon-legacy").click()

#6
#driver.get("https://translate.google.com/")
# print(driver.find_element(by=By.CLASS_NAME, value="er8xn"))
# print(driver.find_element(by=By.ID, value="er8xn"))
#print(driver.find_element(by=By.XPATH,value="//textarea[@aria-label='Source text']"))
# print(driver.find_element_by_xpath("//textarea[@aria-label='Source text']"))

#7
# driver.get("https://www.facebook.com/")
# driver.find_element_by_id("email").send_keys("a@a.com")
# driver.find_element_by_id("pass").send_keys("Aa123456")






