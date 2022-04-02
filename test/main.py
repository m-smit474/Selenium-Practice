import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    # Create variables that will be available for each test case
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    # Methods that start with keyword "test" will be run as test cases
    def test_search_python(self):
        # Load the main page
        mainPage = page.MainPage(self.driver)

        # Check that page title is "Python"
        assert mainPage.is_title_matches()

        # Put string in search bar element and search
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()

        # Check search result
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()



    # Runs after each test case has finished
    def tearDown(self):
        self.driver.close()

# Runs tests
if __name__ == "__main__":
    unittest.main()