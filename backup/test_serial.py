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
	f.write("----- Start of serial test -----\n")
	ip = args[0]
	browser = args[1]

	#
	#test baud rate
	#
	
	baud_rate_options = ["2400", "4800", "9600", "19200", "38400", "57600", "115200"]
	for baud_rate in baud_rate_options:
		print "testing baud_rate " + baud_rate
		callString = "./select.py '" + ip + " " + browser + " webinterface5.sh baud_rate " + baud_rate + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()

	#
	#test data_bits
	#
	data_bit_options = ["5", "6", "7", "8"]
	for data_bit in data_bit_options:
		print "testing data_bit " + data_bit
		callString = "./select.py '" + ip + " " + browser + " webinterface5.sh char_size " + data_bit + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test parity
	#
	parity_options = ["odd", "even", "none"]
	for parity in parity_options:
		print "testing parity " + parity
		callString = "./select.py '" + ip + " " + browser + " webinterface5.sh parity " + parity + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test stop bits
	#
	stop_bit_options = ["1", "2"]
	for stop_bit in stop_bit_options:
		print "testing stop_bit " + stop_bit
		callString = "./select.py '" + ip + " " + browser + " webinterface5.sh stop_bits " + stop_bit + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test sw_control_flow
	#
	sw_flow_options = ["Enable", "Disable"]
	for sw_flow in sw_flow_options:
		print "testing sw_flow_control " + sw_flow
		callString = "./select.py '" + ip + " " + browser + " webinterface5.sh sw_flow_control " + sw_flow + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test hw_control_flow
	#
	hw_flow_options = ["Enable", "Disable"]
	for hw_flow in hw_flow_options:
		print "testing hw_flow_control " + hw_flow
		callString = "./select.py '" + ip + " " + browser + " webinterface5.sh hw_flow_control " + hw_flow + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test protocol
	#
	proto_options = ["tcp", "udp"]
	for proto in proto_options:
		print "testing protocol " + proto
		callString = "./select.py '" + ip + " " + browser + " webinterface5.sh proto " + proto + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test peer ip
	#
	serial_ip_options = [ "123123"]
	for serial_ip in serial_ip_options:
		print "testing serial_ip " + serial_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface5.sh serial_ip " + serial_ip + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	serial_port_options = [ "4445"]
	for serial_port in serial_port_options:
		print "testing serial_port " + serial_port
		callString = "./textfield.py '" + ip + " " + browser + " webinterface5.sh serial_port " + serial_port + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()


	#
	#end of serial test
	#
	print "----- End of serial test -----" 
	f.write("------------------------" + time.asctime() + "------------------------\n")
	f.write("----- End of serial test -----\n\n")
	f.close()
