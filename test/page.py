# Base class for all pages
# Other pages will inherit from this class
from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    # name for search bar
    #locator = "q"
    locator = MainPageLocators.SEARCH_BAR[1]

class BasePage(object):
    # Base class to initalize the base page that will be called by all pages.
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    # Home page actions here. (Python.org)
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultPage(BasePage):
    # Search results page actions here.
    def is_results_found(self):
        return "No results found." not in self.driver.page_source