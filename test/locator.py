from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_BAR = (By.NAME, "q")
    GO_BUTTON = (By.ID, "submit")

class SearchReultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""
    pass