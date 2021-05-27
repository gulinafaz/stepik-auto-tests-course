from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_css_selector("button.btn").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()

    
    x_el = (browser.find_element_by_id("input_value").text)
    y = calc(x_el)
    
 
    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)   
    browser.quit()
    
