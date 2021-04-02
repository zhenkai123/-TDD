from selenium import webdriver          #(1)
import unittest


class NewVisiotorTest(unittest.TestCase): #(1)
    def sutUp(self):    #(3)
        self.browser=webdriver.Firefox() 

    def tearDown(self): #(3)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new online to-do app. She goes
        #to check out its homepage
        self.brower.get('http://localhost:8000')
        #She notices the page title and header mention to-do lists
        self.assertIn('TO-DO',self.browser.title)
        self.fail('Finish the test')

if __name__=='__main__':
    unittest.main(warnings='ignore')
