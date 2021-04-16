from selenium import webdriver          #(1)
import unittest


class NewVisitorTest(unittest.TestCase): #(1)
    def setUp(self):    #(3)
        self.browser=webdriver.Firefox() 

    def tearDown(self): #(3)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new online to-do app. She goes
        #to check out its homepage
        self.browser.get('http://localhost:8000')
        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
        
        inputbox.send_keys('Buy peacock feathers')
        
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.fin_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text=='1:Buy peacock feathers' for row in rows)
            )

        self.fail('Finish the test!')

if __name__=='__main__':
    unittest.main(warnings='ignore')
