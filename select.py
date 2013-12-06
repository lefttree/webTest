#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import jsonrpclib
import sys, os

class BasicTab(unittest.TestCase):
    args = sys.argv[1].split(" ")
    # args[0] --- radio_url
    # args[1] --- browser
    # args[2] --- webinterface*.sh
    # args[3] --- name of element
    # args[4] --- value
    
    def setUp(self):
	args = self.args
	self.getBrowser(args[1])  #setup browser
	self.driver.implicitly_wait(30)
        self.base_url = "http://" + args[0] + "/"  #set base radio_url
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

    def test_basic(self):
	args = self.args
	#go to url and find select element
        self.driver.get(self.base_url + args[2])
	#find select element and click
	self.clickSelect(args[3], args[4])
	#click button to submit form
	self.submitForm(args[3])
	#check value on radio
	rResult = self.getRadioValue(args[0], args[3])
	#convert value to text
	rResult = self.convertValue2Text(rResult, args[3])
	#write into output file
	self.writeToFile(rResult, args[3], args[4])
	
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

    def clickSelect(self, element, value):
	element2 = Select(self.driver.find_element_by_name(element))
	#go through select options
	for option in element2.options:
		text = option.text
		strtext = text.encode('ascii', 'ignore') #convert unicode
		if element == "power_mw":
			strtext = strtext.split(" ")[0]
			if value == strtext:
				option.click()
				break
		else:
			if value in strtext:
				option.click()
				break


    def clickButton(self, buttonName):
	#click on submit button, double to make it wait	
	xpath = "(//input[@name='" + buttonName + "'])[1]"
	self.driver.find_element_by_xpath(xpath).click()
	self.driver.find_element_by_xpath(xpath).click()
    
    def submitForm(self, element):
	if element == "freq" or element == "bandwidth":
		self.clickButton("checkpage0")
	elif element == "power_mw":
		self.clickButton("checkpage1")
	elif element == "gateway_disable":
		self.clickButton("checkpage2")

    def getRadioValue(self, radio_url, element):
	#using jsonrpclib to get value from radio
	jsonrpc_url = "http://" + radio_url + "/streamscape_api"
	server = jsonrpclib.Server(jsonrpc_url)
	if element == "freq":
		radioResult = server.freq()
	elif element == "bandwidth":
		radioResult = server.bw()
	elif element == "power_mw":
		radioResult = server.power_dBm()
	elif element == "gateway_disable":
		radioResult = server.wbg_disable()
	rResult = radioResult[0].encode('ascii', 'ignore')
	return rResult

    def convertValue2Text(self, rResult, element):
	#convert 0/1 to Enable/Disable
	if element == "gateway_disable":
		if rResult == "0":
			rResult = "Enable"
		else:
			rResult = "Disable"
	return rResult

    def writeToFile(self, rResult, element, value):
	f = open('outputfile', 'a')
	if rResult == value:
		print element + " "
		print rResult
		print "updated correctly\n"
	else:
		print element + " "
		print rResult
		print "! wrong !\n"
		f.write("wrong! ")
		f.write("radio value is " + rResult)
		f.write("; test value is " + value)
		f.write("\n")
	f.close()

if __name__ == "__main__":
	unittest.main(argv=sys.argv[1:])
