from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")

print(driver.title)

# Search bar has name 'q' in HTML
search = driver.find_element_by_name("q")

# Clear search bar
search.clear()

# Send inpunt to search bar
search.send_keys("test")
search.send_keys(Keys.RETURN)

# Wait for page to load elements
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Fast.com: Internet Speed Test"))
    )
    element.click()
    #link = driver.find_element_by_partial_link_text("Fast.com: Internet Speed Test")
    #link.click()

    time.sleep(5)

    driver.back()
    driver.back()

    time.sleep(5)
finally:
    driver.quit()
