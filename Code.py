from selenium import webdriver
import time 

#creating the varible for the webdriver
browser = webdriver.Firefox(executable_path=/'/path/to/geckodriver')

#It will open the browser and then searches for this URL: https://www.caloriemama.ai/api
browser.get("https://www.caloriemama.ai/api")

#Find the class name "file-upload"
upload = browser.find_element_by_class_name('file-upload')

#Load your imaage here and then locate it at: /path/to/food.jpeg
upload.send_keys('/path/to/food.jpeg')
time.sleep(5)

#Return the value by class name
get = browser.find_element_by_class_name('group-name')
print(get. text)
