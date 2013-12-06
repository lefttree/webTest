#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import jsonrpclib
import sys, os

class FreqBw(unittest.TestCase):
    def setUp(self):
	#chromedriver = "/usr/local/bin/chromedriver"
	#os.environ["webdriver.chrome.driver"] = chromedriver
        #self.driver = webdriver.Chrome(chromedriver)
	self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.20.4.127/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_freq_bw(self):
	args=sys.argv[1].split(" ") #split arguments
	#go to url and get element
        driver = self.driver
        driver.get(self.base_url + args[0])
	element2 = Select(driver.find_element_by_name(args[1]))
	#go through select options
	for option in element2.options:
		text = option.text
		strtext = text.encode('ascii', 'ignore') #convert unicode
		if args[1] == "power_mw":
			strtext = strtext.split(" ")[0]
			if args[2] == strtext:
				option.click()
		else:
			if args[2] in strtext:
				option.click()
        #click on submit button, double to make it wait	
	if args[1] == "freq" or args[1] == "bandwidth":
		driver.find_element_by_xpath("(//input[@name='checkpage0'])[1]").click()	
		driver.find_element_by_xpath("(//input[@name='checkpage0'])[1]").click()
	elif args[1] == "power_mw":
		driver.find_element_by_xpath("(//input[@name='checkpage1'])[1]").click()	
		driver.find_element_by_xpath("(//input[@name='checkpage1'])[1]").click()
	elif args[1] == "gateway_disable":
		driver.find_element_by_xpath("(//input[@name='checkpage2'])[1]").click()	
		driver.find_element_by_xpath("(//input[@name='checkpage2'])[1]").click()

	#check value on radio
        server = jsonrpclib.Server('http://172.20.4.127/streamscape_api')
	#radiofreq = str(server.freq())
	#rfreq = radiofreq.split("'")[1]
	if args[1] == "freq":
		radioResult = server.freq()
	elif args[1] == "bandwidth":
		radioResult = server.bw()
	elif args[1] == "power_mw":
		radioResult = server.power_dBm()
	elif args[1] == "gateway_disable":
		radioResult = server.wbg_disable()

	rResult = radioResult[0].encode('ascii', 'ignore')
	if args[1] == "gateway_disable":
		if rResult == "0":
			rResult = "Enable"
		else:
			rResult = "Disable"
	#write into output file
	f = open('outputfile', 'a')
	if rResult == args[2]:
		print args[1] + " "
		print rResult
		print "updated correctly\n"
	else:
		print args[1] + " "
		print rResult
		print "! wrong !\n"
		f.write("wrong! ")
		f.write("radio value is " + rResult)
		f.write("; test value is " + args[2])
		f.write("\n")
	f.close()

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
	unittest.main(argv=sys.argv[1:])
