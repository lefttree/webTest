from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import unittest
import sys

class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor="http://192.168.10.222:5556/wd/hub",desired_capabilities={ "browserName": browser, "platform": platform, "node":node })
   	self.driver.implicitly_wait(2)

    def test_example(self):
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
	args = sys.argv[1].split(" ")
	node = args[0]
	browser = args[1]
	platform = args[2]		
	unittest.main(argv=sys.argv[1:])
