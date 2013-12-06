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
	f.write("----- Start of basic test -----\n")
	ip = args[0]
	browser = args[1]

	#
	#test freq select
	#
	frequencies = [2420,2440,2452,2466.666667,2480,2492,4942.5,4947.5,4952.5,4955,4957.5,4960,4962.5,4967.5,4972.5,4975,4977.5,4982.5,4987.5,5120,5745,5765,5785,5805,5825]
	'''
	fre = open('frequencies', 'r')
	for line in fre:
		frequencies.append(line)
	fre.close()	
	'''
	for freqline in frequencies:
		freq = str(freqline)
		print "testing frequency " + freq
		callString = "./select.py '" + ip + " " + browser + " webinterface0.sh freq " + freq + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test bw select
	#
	bw_options = ["5", "20"]
	for bw in bw_options:
		print "testing bandwidth " + bw
		callString = "./select.py '" + ip + " " + browser + " webinterface0.sh bandwidth " + bw + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	
	#
	#test transmit power
	#
	power_dBm_options = ["0", "10", "12", "18", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]	
	for power_dBm in power_dBm_options:
		print "testing power_dBm " + power_dBm
		callString = "./select.py '" + ip + " " + browser + " webinterface0.sh power_mw " + power_dBm + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	
	#
	#test gateway_disable
	#
	gateway_disable_options = ["Enable", "Disable"]
	for gateway_disable in gateway_disable_options:
		print "testing gateway_disable " + gateway_disable
		callString = "./select.py '" + ip + " " + browser + " webinterface0.sh gateway_disable " + gateway_disable + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#end of basic test
	#
	print "----- End of basic test -----" 
	f.write("------------------------" + time.asctime() + "------------------------\n")
	f.write("----- End of basic test -----\n\n")
	f.close()
