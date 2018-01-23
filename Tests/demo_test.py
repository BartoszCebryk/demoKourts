from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


#setting up basic chrome driver
driver = webdriver.Chrome()
driver.get("http://www.kourts.com")
timeout = 20


#1 locating H1 tag on page
try:
    element = driver.find_element_by_tag_name('h1')
except NoSuchElementException:
    print("No H1 rendered")

#extra step with screenshot
driver.save_screenshot('extra_one.png')

#2 step - clicking on login button
element = driver.find_element_by_xpath("//a[contains(text(), 'Login')]")
element.click()

#4 checking if modal is present
try:
    element = driver.find_element_by_class_name("modal")
except NoSuchElementException:
    print("No modal displayed")

#5 clicking on second login button - the one on pop up
try:
    element = driver.find_element_by_xpath("//span[@class='button is-primary']")
except NoSuchElementException:
    print("No login button displayed")
element.click()

#6 checking if error message is displayed - as this may take a while on processing
# explicit wait is used
try:
    element_present = EC.presence_of_element_located((By.XPATH, "//ul[@class='error']" ))
    WebDriverWait(driver, timeout).until(element_present)
except NoSuchElementException:
    print("No error message displayed")

# extra step for taking another screenshot
driver.save_screenshot('extra_two.png')

#post test activities
driver.close()
driver.quit()

