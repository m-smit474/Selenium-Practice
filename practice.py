from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")

print(driver.title)

# Search bar has name 'q' in HTML
search = driver.find_element_by_name("q")

search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(10)

#driver.close()
driver.quit()