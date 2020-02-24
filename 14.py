from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os

import math
import sys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element( (By.ID, "price"), "100" )
    ) # browser.find_element_by_id("price").text


    button = browser.find_element_by_id("book")
    button.click()
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)

    # # confirm = browser.switch_to.alert
    # # confirm.accept()
    

    
    x1 = browser.find_element_by_id("input_value")
    xnum = int(x1.text)
    # # //ln(abs(12*sin(x)))
    sum = math.log(abs(12*math.sin(xnum)))
    sumstyring = str(sum)

    inp = browser.find_element_by_id("answer")
    inp.send_keys(sumstyring)

    button = browser.find_element_by_id("solve")
    button.click()



    # # button = browser.find_element_by_css_selector("button.btn-primary")
    # # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    


    # # option1 = browser.find_element_by_id("robotCheckbox")
    # # option1.click()


   
    # # option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    # # option2.click()

    # # button.click()
except:
   print("Unexpected error:", sys.exc_info()[0])
   raise

finally:
    time.sleep(30)
    browser.quit()