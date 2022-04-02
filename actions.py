from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookieCount = driver.find_element_by_id("cookies")
upgrades = [driver.find_element_by_id("product" + str(i)) for i in range(0, 1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookieCount.text.split(" ")[0])
    
    for upgrade in upgrades:
        cost = int(upgrade.text.split("\n")[1])
        if cost <= count:
            upgradeActions = ActionChains(driver)
            upgradeActions.click(upgrade)
            upgradeActions.perform()


driver.quit()