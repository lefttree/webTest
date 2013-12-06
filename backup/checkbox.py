from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys

class Checkbox(unittest.TestCase):
    args = sys.argv[1].split(" ")
    # args[0] --- radio_url
    # args[1] --- browser
    # args[2] --- element

    def setUp(self):
	args = self.args
        self.getBrowser(args[1])
        self.driver.implicitly_wait(30)
        self.base_url = "http://" + args[0] + "/"
        self.verificationErrors = []
        self.accept_next_alert = True
     
    def getBrowser(self, browser):
	if browser == "firefox" or browser == "Firefox":
		self.driver = webdriver.Firefox()
	elif browser == "chrome" or browser == "Chrome":
		self.driver = webdriver.Chrome()
	elif browser == "ie" or browser == "IE":
		print "No IE on Linux"
	else:
		self.driver = webdriver.Frefox()

    def test_checkbox(self):
	args = self.args
        self.driver.get(self.base_url + "netmgmt_dev.html")
	#find checkbox
	self.clickCheckbox(args[2])
	
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def clickCheckbox(self, element):
	chkb = self.driver.find_element_by_id(element)
	chkb.click()

if __name__ == "__main__":
	unittest.main(argv=sys.argv[1:])
