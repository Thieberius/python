from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/ich/Python-lernen.de/fs/chromedriver')

driver.get('https://www.google.de/')

time.sleep(3)
