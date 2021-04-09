from selenium import webdriver          # (1)
import unittest

class NewVisitorTest(unittest.TestCase): #

    def setUp(self): # (3)
        self.browser = webdriver.Firefox()

    def tearDown(self): #(3)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): # (2)
    # Edith has heard about a cool new online to-do app. She goesto check out its homepage
        self.browser.get('http://localhost:8000')
    # She notices the page title and header mention to-do lists
        self.assertIn( 'To-Do', self.browser.title)
    #(4）
        self.fail('Finish the test!')
    # C5

if __name__ == '__main__':  # (6)
    unittest.main(warnings='ignore')  # (7)
