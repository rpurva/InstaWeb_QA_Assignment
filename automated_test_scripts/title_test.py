from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://websites.co.in/login")

driver.maximize_window()

time.sleep(3)

print("Page title is:")
print(driver.title)

driver.quit()