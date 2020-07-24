from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_cv_resolves_to_correct_view(self):
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')