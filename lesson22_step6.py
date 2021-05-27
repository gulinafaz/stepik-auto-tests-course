from selenium import webdriver
import math
import time

link = "http://SunInJuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_el = (browser.find_element_by_id("input_value").text)
    
    y = calc(x_el)
    
    button = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
  
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)   
    browser.quit()
    
