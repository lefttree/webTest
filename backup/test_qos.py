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
	f.write("----- Start of qos test -----\n")
	ip = args[0]
	browser = args[1]
	qos_options = [2000,4000-5000,9000-7000]
	#
	#test low priority
	#
	for ports in qos_options:
		print "testing low_tcp " + ports_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface3.sh port_spec0T " + ports + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
		print "testing low_udp " + ports_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface3.sh port_spec0U " + ports + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
		print "testing low_both " + ports_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface3.sh port_spec0B " + ports + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()

		print "testing high_tcp " + ports_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface3.sh port_spec1T " + ports + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
		print "testing high_udp " + ports_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface3.sh port_spec1U " + ports + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
		print "testing high_both " + ports_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface3.sh port_spec1B " + ports + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	
	#
	#end of serial test
	#
	print "----- End of qos test -----" 
	f.write("------------------------" + time.asctime() + "------------------------\n")
	f.write("----- End of qos test -----\n\n")
	f.close()
