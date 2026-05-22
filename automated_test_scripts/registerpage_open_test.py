from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://websites.co.in/register")

driver.maximize_window()

time.sleep(3)

print("Registration page opened!!")

driver.quit()