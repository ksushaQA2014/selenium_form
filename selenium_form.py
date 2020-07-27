from selenium import webdriver
from selenium.webdriver.common.by import By

import time

TEST_DATA = {
        'single_input': 'My best message here!!',
        'two_input_first': 333,
        'two_input_second': 444
    }

driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
time.sleep(5)
if driver.find_element_by_id("at-cv-lightbox-close").size != 0:
   driver.find_element_by_id("at-cv-lightbox-close").click()


driver.find_element(By.CSS_SELECTOR, "input#user-message").send_keys(TEST_DATA['single_input'])
driver.find_element(By.CSS_SELECTOR, "form#get-input button").click()

assert driver.find_element(By.ID, "display").text == TEST_DATA['single_input']

driver.find_element(By.CSS_SELECTOR, "#sum1").send_keys(TEST_DATA['two_input_first'])
driver.find_element(By.CSS_SELECTOR, "#sum2").send_keys(TEST_DATA['two_input_second'])
driver.find_element(By.CSS_SELECTOR, "form#gettotal button").click()

assert driver.find_element(By.CSS_SELECTOR, "#displayvalue").text == str(TEST_DATA['two_input_first'] + TEST_DATA['two_input_second'])


driver.quit()


Часть Advanced




from selenium import webdriver
from selenium.webdriver.common.by import By
import time
TEST_DATA1 = {
        'username': 'tomsmith',
        'password': 'SuperSecretPassword!',

    }

TEST_DATA2 = {
        'username': 'tomsmith23',
        'password': 'SuperSecretPassword!',

    }

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(TEST_DATA1['username'])
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(TEST_DATA1['password'])
driver.find_element(By.CSS_SELECTOR, "#login > button").click()

assert 'You logged into a secure area!' in driver.page_source
driver.quit()


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(TEST_DATA2['username'])
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(TEST_DATA2['password'])
driver.find_element(By.CSS_SELECTOR, "#login > button").click()

assert 'Your username is invalid!' in driver.page_source
driver.quit()



