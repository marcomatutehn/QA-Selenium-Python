from selenium import webdriver

browser = webdriver.Chrome(executable_path='/Users/marcomartinez/PycharmProjects/Test/src/drivers/chromedriver')

browser.get('http://www.yahoo.com/')
browser.close()