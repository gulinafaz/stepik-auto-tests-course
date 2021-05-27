from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()	
	browser.get(link)
	
	browser.find_element_by_css_selector("[name='firstname']").send_keys("Ivan")
	browser.find_element_by_css_selector("[name='lastname']").send_keys("Ivanov")
	browser.find_element_by_css_selector("[name='email']").send_keys("gmail")

	
	

	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
	
	browser.find_element_by_css_selector("#file").send_keys(file_path)
	
	browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)   
    browser.quit()
    
