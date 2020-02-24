from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

import math
import sys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    

    
    x1 = browser.find_element_by_id("input_value")
    xnum = int(x1.text)

    sum = math.log(abs(12*math.sin(xnum)))
    sumstyring = str(sum)

    inp = browser.find_element_by_id("answer")
    inp.send_keys(sumstyring)

    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()



    # button = browser.find_element_by_css_selector("button.btn-primary")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    


    # option1 = browser.find_element_by_id("robotCheckbox")
    # option1.click()


   
    # option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    # option2.click()

    # button.click()
except:
   print("Unexpected error:", sys.exc_info()[0])
   raise

finally:
    time.sleep(30)
    browser.quit()