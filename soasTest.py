from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class SoasTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.soastastore.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_soas(self):
        driver = self.driver
        driver.get(self.base_url + "/?page_id=167")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
	select = driver.find_element_by_id("sfquicklinksPost")
	select2 = Select(driver.find_element_by_xpath("//select[@name='sfquicklinks']"))
	print select2.options
	print select
	for o in select2.options:
		print o.text
	select3 = driver.find_element_by_xpath("//select[@name='sfquicklinks']/option[text()='Website Issues']")
	select3.click()
	
    
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

if __name__ == "__main__":
    unittest.main()
