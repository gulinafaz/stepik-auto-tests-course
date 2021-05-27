from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
def calc(a, b):
  return str(a + b)

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    a = int(browser.find_element_by_id("num1").text)
    b = int(browser.find_element_by_id("num2").text)
    y = calc(a, b)
      
      
    select = Select(browser.find_element_by_css_selector(".custom-select"))
    select.select_by_value(y) 
    
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)   
    browser.quit()
    
    
    
