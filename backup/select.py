#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import jsonrpclib
import sys

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

    def clickSelect(self, element, value):
	selectElement = Select(self.driver.find_element_by_name(element))
	#go through select options
	for option in selectElement.options:
		text = option.text
		strtext = text.encode('ascii', 'ignore') #convert unicode
		
		value = value.upper()
		strtext = strtext.upper()
		
		#match all options
		if element == "temp_reporting_mode" or element == "phytest" or element == "parity":
			if value in strtext:
				print "click " + strtext
				option.click()
				break
		else:
			strtext = strtext.split(" ")[0]
			if element == "class0_mcs":
				strtext - strtext.split(":")[0]
				if value == strtext:
					print "click " + strtext + "\n"
					option.click()
					break
			else:
				if value == strtext:
					print "click " + strtext + "\n"
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
	#webinterface2
	elif element == "rts_disable" or element == "aggr_thresh" or element == "max_speed" or element == "burst_time" or element == "enc_disable" or element == "enc_key_len" or element == "class0_mcs" or element == "phytest":
		self.clickButton("advance1")
	elif element == "vir_ip_disable" or element == "vpn_disable":
		self.clickButton("advance2")
	#webinterface5
	#elif element == "serial_mode":
	#	self.clickButton("mode_change")
	elif element == "baud_rate" or element == "char_size" or element == "parity" or element == "stop_bits" or element == "sw_flow_control" or element == "hw_flow_control" or element == "proto":
		self.clickButton("advance")
	#webinterface7
	elif element == "temp_reporting_mode":
		self.clickButton("checkpage0")
	elif element == "rssi_report_enable":
		self.clickButton("checkpage1")

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
	#webinterface2	
	elif element == "rts_disable": 
		radioResult = server.rts_disable()
	elif element == "aggr_thresh":
		radioResult = server.aggr_thresh()
	elif element == "max_speed":
		radioResult = server.max_speed()
	elif element == "burst_time":
		radioResult = server.burst_time()
	elif element == "enc_disable":
		radioResult = server.enc_disable()
	elif element == "enc_key_len":
		radioResult = server.enc_key_len()
	elif element == "class0_mcs":
		radioResult = server.mcs()
	elif element == "phytest":
		radioResult = server.radio_mode()
	elif element == "vir_ip_disable":
		radioResult = server.virtual_ip_disable()
	elif element == "vpn_disable":
		radioResult = server.vpn_disable()
	#webinterface5.sh
	#elif element == "serial_mode":	
	elif element == "baud_rate" or element == "char_size" or element == "parity" or element == "stop_bits" or element == "sw_flow_control" or element == "hw_flow_control" or element == "proto":
		radioResult = server.serial_config()
	#webinterface7.sh
	elif element == "temp_reporting_mode":
		radioResult = server.temp_reporting_mode()
	elif element == "rssi_report_enable":
		radioResult = server.rssi_report_enable()

	#convert unicode
	if element == "baud_rate":
		rResult = radioResult[0].encode('ascii', 'ignore')
	elif element == "char_size":
		rResult = radioResult[1].encode('ascii', 'ignore')
	elif element == "parity":
		rResult = radioResult[2].encode('ascii', 'ignore')
	elif element == "stop_bits":
		rResult = radioResult[3].encode('ascii', 'ignore')
	elif element == "sw_flow_control":
		rResult = radioResult[5].encode('ascii', 'ignore')
	elif element == "hw_flow_control":
		rResult = radioResult[4].encode('ascii', 'ignore')
	elif element == "proto":
		rResult = radioResult[7].encode('ascii', 'ignore')
	else:
		rResult = radioResult[0].encode('ascii', 'ignore')
	return rResult
	
    def convertValue2Text(self, rResult, element):
	#convert 0/1 to Enable/Disable
	if element == "gateway_disable" or element == "vpn_disable" or element == "vir_ip_disable" or element == "enc_disable" or element == "rts_disable":
		if rResult == "0":
			rResult = "Enable"
		else:
			rResult = "Disable"
	elif element == "parity":
		if rResult == "0":
			rResult = "Even"
		elif rResult == "1":
			rResult = "Odd"
		elif rResult == "2":
			rResult = "None"
	elif element == "stop_bits":
		if rResult == "0":
			rResult = "1"
		elif rResult == "1":
			rResult = "2"
	elif element == "sw_flow_control" or element == "hw_flow_control":
		if rResult == "1":
			rResult = "Enable"
		elif rResult == "0":
			rResult = "Disable"
	elif element == "proto":
		rResult = rResult.upper()
	elif element == "temp_reporting_mode":
		if rResult == "0":
			rResult = "Disable"
		elif rResult == "1":
			rResult = "heating"
		elif rResult == "2":
			rResult = "periodically"
	elif element == "rssi_report_enable":
		if rResult == "0":
			rResult = "Disable"
		elif rResult == "1":
			rResult = "Enable"
	elif element == "burst_time":
		rResult = int(rResult)
		rResult = rResult / 1000
		rResult = str(rResult)
	return rResult

    def writeToFile(self, rResult, element, value):
	rResult = rResult.upper()
	value = value.upper()
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
