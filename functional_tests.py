from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_cv_resolves_to_correct_view(self):
    # User goes to /cv/
        self.browser.get('http://0.0.0.0:8000/cv/')

    # The page title is contains 'Declan Fisher - CV'
        self.assertIn('Declan Fisher - CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Declan Fisher - CV', header_text)
    # User can view the CV
        rows = self.browser.find_elements_by_tag_name('h3')
        self.assertIn('Profile', [row.text for row in rows])
        self.assertIn('Employment', [row.text for row in rows])
        self.assertIn('Education', [row.text for row in rows])
        self.assertIn('Skills', [row.text for row in rows])
        self.assertIn('Extra-Curricular Activities', [row.text for row in rows])
        self.assertIn('Hobbies', [row.text for row in rows])
        self.assertIn('References', [row.text for row in rows])

if __name__ == '__main__':
    unittest.main(warnings='ignore')