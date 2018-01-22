from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.kourts.com")
timeout = 20

try:
    element = driver.find_element_by_tag_name('h1')
except NoSuchElementException:
    print("No H1 rendered")
driver.save_screenshot('extra_one.png')

element = driver.find_element_by_xpath("//a[contains(text(), 'Login')]")
element.click()

try:
    element = driver.find_element_by_class_name("modal")
except NoSuchElementException:
    print("No modal displayed")

try:
    element = driver.find_element_by_xpath("//span[@class='button is-primary']")
except NoSuchElementException:
    print("No login button displayed")
element.click()

try:
    element_present = EC.presence_of_element_located((By.XPATH, "//ul[@class='error']" ))
    WebDriverWait(driver, timeout).until(element_present)
except NoSuchElementException:
    print("No error message displayed")
driver.save_screenshot('extra_two.png')


driver.close()
driver.quit()

