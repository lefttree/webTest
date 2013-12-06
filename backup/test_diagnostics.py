#!/usr/bin/python
import subprocess, time
import jsonrpclib
import fileinput
import sys

if __name__ == '__main__':
	args = sys.argv[1].split(" ")
	#args[0] --- radio_ip
	#args[1] --- browser
	#

	#
	#write current time into output file
	#
	f = open('outputfile', 'a')
	f.write("------------------------" + time.asctime() + "------------------------\n")
	f.write("----- Start of diagnostics test -----\n")
	ip = args[0]
	browser = args[1]

	#
	#test temp reporting mode
	#
	temp_mode_options = ["Disable", "heating", "periodically"]
	for temp_mode in temp_mode_options:
		print "testing temp_mode " + temp_mode
		callString = "./select.py '" + ip + " " + browser + " webinterface7.sh temp_reporting_mode " + temp_mode + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test temp reporting ip
	#
	temp_report_ip_options = ["192.168.10.207"]
	for temp_report_ip in temp_report_ip_options:
		print "testing temp_report_ip " + temp_report_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface7.sh temp_reporting_ip " + temp_report_ip + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test temp report port
	#
	temp_report_port_options = [ "9000" ]
	for temp_report_port in temp_report_port_options:
		print "testing temp_report_port " + temp_report_port
		callString = "./textfield.py '" + ip + " " + browser + " webinterface7.sh temp_reporting_port " + temp_report_port + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test min temp threshold
	#
	min_temp_threshold_options = ["70", "75"]
	for min_temp_threshold in min_temp_threshold_options:
		print "testing min_temp_threshold " + min_temp_threshold
		callString = "./textfield.py '" + ip + " " + browser + " webinterface7.sh temp_reporting_min_threshold " + min_temp_threshold + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test max temp threshold
	#
	max_temp_threshold_options = ["85", "90"]
	for max_temp_threshold in max_temp_threshold_options:
		print "testing max_temp_threshold " + max_temp_threshold
		callString = "./textfield.py '" + ip + " " + browser + " webinterface7.sh temp_reporting_max_threshold " + max_temp_threshold + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test temp report period
	#
	temp_period_options = ["5", "10"]
	for temp_period in temp_period_options:
		print "testing temp_report_period " + temp_period
		callString = "./textfield.py '" + ip + " " + browser + " webinterface7.sh temp_reporting_period " + temp_period + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#disable report
	temp_mode_options2 = ["Disable"]
	for temp_mode2 in temp_mode_options2:
		callString = "./select.py '" + ip + " " + browser + " webinterface7.sh temp_reporting_mode " + temp_mode2 + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()

	#
	#test rssi report mode
	#
	rssi_report_mode_options = ["Disable", "Enable"]
	for rssi_report_mode in rssi_report_mode_options:
		print "testing rssi_report_mode " + rssi_report_mode
		callString = "./select.py '" + ip + " " + browser + " webinterface7.sh rssi_report_enable " + rssi_report_mode + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test rssi ip
	#
	rssi_report_ip_options = ["192.168.10.207"]
	for rssi_report_ip in rssi_report_ip_options:
		print "testing rssi_report_ip " + rssi_report_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface7.sh rssi_report_ip " + rssi_report_ip + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test rssi port
	#
	rssi_report_port_options = [ "9000" ]
	for rssi_report_port in rssi_report_port_options:
		print "testing rssi_report_port " + rssi_report_port
		callString = "./textfield.py '" + ip + " " + browser + " webinterface7.sh rssi_report_port " + rssi_report_port + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test rssi report period
	#
	rssi_report_period_options = [ "5", "10" ]
	for rssi_report_period in rssi_report_period_options:
		print "testing rssi_report_period " + rssi_report_period
		callString = "./textfield.py '" + ip + " " + browser + " webinterface7.sh rssi_report_period " + rssi_report_period + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#end of serial test
	#
	print "----- End of diagnostics test -----" 
	f.write("------------------------" + time.asctime() + "------------------------\n")
	f.write("----- End of diagnostics test -----\n\n")
	f.close()
