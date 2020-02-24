from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

import math
import sys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    inp1 = browser.find_element_by_name("firstname")
    inp1.send_keys("name")

    inp2 = browser.find_element_by_name("lastname")
    inp2.send_keys("lastname")

    inp3 = browser.find_element_by_name("email")
    inp3.send_keys("email@gmail.com")


    __file__ = "/home/igor/Desktop/vu/testing/"
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt') 
    print(file_path)          # добавляем к этому пути имя файла 
    xpath ="//*[@id=\"file\"]"
    element = browser.find_element_by_xpath(xpath).send_keys(file_path)


    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()
    
    # x1 = browser.find_element_by_id("input_value")
    # xnum = int(x1.text)

    # sum = math.log(abs(12*math.sin(xnum)))
    # sumstyring = str(sum)

    # inp = browser.find_element_by_id("answer")
    # inp.send_keys(sumstyring)



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