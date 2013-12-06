#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import jsonrpclib
import sys
import re

class Textfield(unittest.TestCase):
    args = sys.argv[1].split(" ")
    # args[0] --- radio_url
    # args[1] --- browser
    # args[2] --- webinterface*.sh
    # args[3] --- name of element
    # args[4] --- value

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


    def test_textfield(self):
	args = self.args
	#go to webinterface*.sh
        self.driver.get(self.base_url + args[2])
	#find textfield element and type value
	self.typeText(args[3], args[4])
	#click button to submit form
	self.submitForm(args[3])
   	#check value on radio
	rResult = self.getRadioValue(args[0], args[3])
	#write result into output file
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

    def typeText(self, element, value):
	textElement = self.driver.find_element_by_name(element)
	textElement.clear()
	textElement.send_keys(value)
    
    def clickButton(self, buttonName):
	#click on submit button, double to make it wait		
	xpath = "(//input[@name='" + buttonName + "'])[1]"
	self.driver.find_element_by_xpath(xpath).click()
	self.driver.find_element_by_xpath(xpath).click()

    def submitForm(self, element):
	if element == "link_distance" or element == "enc_key":
		self.clickButton("advance1")
		return
	#use regular expression to match
	#Advanced
	matchVir = re.match(r'vir.*', element)
	if matchVir:
		self.clickButton("advance2")
		return
	matchVpn = re.match(r'vpn.*', element)
	if matchVpn:
		self.clickButton("advance2")
		return
	#qos
	matchQos = re.match(r'port_spec.*', element)
	if matchQos:
		self.clickButton("advance")
		return
	#Serial_port
	matchSerial = re.match(r'serial.*', element)
	if matchSerial:
		self.clickButton("advance")
		return
	#temp
	matchTemp = re.match(r'temp.*', element)
	if matchTemp:
		self.clickButton("checkpage0")
		return
	#rssi
	matchRssi = re.match(r'rssi.*', element)
	if matchRssi:
		self.clickButton("checkpage1")
		return
		
    def getRadioValue(self, radio_url, element):
	jsonrpc_url = "http://" + radio_url + "/streamscape_api"
	server = jsonrpclib.Server(jsonrpc_url)
	if element == "link_distance":
		radioResult = server.max_link_distance()
	elif element == "enc_key":
		radioResult = server.enc_key()
	elif element == "vir_addr":
		radioResult = server.virtual_ip_address()
	elif element == "vir_netmask":
		radioResult = server.virtual_ip_netmask()
	elif element == "vir_gw":
		radioResult = server.virtual_ip_gateway()
	elif element == "vpn_addr" or element == "vpn_port":
		radioResult = server.vpn_address()
	#webinterface3.sh
	elif element == "port_spec0T":
		radioResult = server.qos_class("5","1")
	elif element == "port_spec0U":
		radioResult = server.qos_class("5","0")
	elif element == "port_spec0B":
		radioResult = server.qos_class("5","2")
	elif element == "port_spec1T":
		radioResult = server.qos_class("6","1")
	elif element == "port_spec1U":
		radioResult = server.qos_class("6","0")
	elif element == "port_spec1B":
		radioResult = server.qos_class("6","2")
	#webinterface5.sh
	elif element == "serial_ip" or element == "serial_port":
		radioResult = server.serial_config()
	#webinterface7.sh
	elif element == "temp_reporting_ip" or element == "temp_reporting_port":
		radioResult = server.temp_reporting_address()
	elif element == "temp_reporting_min_threshold":
		radioResult = server.temp_reporting_min_threshold()
	elif element == "temp_reporting_max_threshold":
		radioResult = server.temp_reporting_max_threshold()
	elif element == "temp_reporting_period":
		radioResult = server.temp_reporting_period()
	elif element == "rssi_report_ip" or element == "rssi_report_port":
		radioResult = server.rssi_report_address()
	elif element == "rssi_report_period":
		radioResult = server.rssi_report_period()
	#
	#convert unicode
	#
	if element == "vpn_addr":
		rResult = radioResult[0].encode('ascii', 'ignore').split("_")[0]
	elif element == "vpn_port":
		rResult = radioResult[0].encode('ascii', 'ignore').split("_")[1]
	elif element == "serial_ip":
		rResult = radioResult[6].encode('ascii', 'ignore')
	elif element == "serial_port":
		rResult = radioResult[8].encode('ascii', 'ignore')
	elif element == "temp_reporting_ip":
		rResult = radioResult[0].encode('ascii', 'ignore')
	elif element == "temp_reporting_port":
		rResult = radioResult[1].encode('ascii', 'ignore')
	elif element == "rssi_report_ip":
		rResult = radioResult[0].encode('ascii', 'ignore')
	elif element == "rssi_report_port":
		rResult = radioResult[1].encode('ascii', 'ignore')
	else:
		rResult = radioResult[0].encode('ascii', 'ignore')
	#qos 
	matchObj = re.match(r'port_spec.*', element)
	if matchObj:
		rResult = ""
		for x in range(0,len(radioResult)):
			if x == 0:
				rResult = rResult + radioResult[x].encode('ascii', 'ignore')
			else:
				rResult = rResult + "," + radioResult[x].encode('ascii', 'ignore')

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
