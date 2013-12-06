import subprocess, time
import jsonrpclib
import fileinput

if __name__ == '__main__':
	#
	#write current time into output file
	#
	f = open('outputfile', 'a')
	f.write("------------------------\n" + time.asctime() + "\n------------------------\n")
	#
	#test freq select
	#
	'''
	frequencies = []
	fre = open('frequencies', 'r')
	for line in fre:
		frequencies.append(line)
	fre.close()

	for freqline in frequencies:
		freq = str.rstrip(freqline)
		print "testing frequency " + freqline
		callString = "./freq_bw.py \'webinterface0.sh freq " + freq + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	
	#
	#test bw select
	#
	bw_options = ["5", "20"]
	for bw in bw_options:
		print "testing bandwidth " + bw
		callString = "./freq_bw.py \'webinterface0.sh bandwidth " + bw + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	
	#
	#test transmit power
	#
	power_dBm_options = ["0", "10", "12", "18", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]	
	for power_dBm in power_dBm_options:
		print "testing power_dBm " + power_dBm
		callString = "./freq_bw.py \'webinterface0.sh power_mw " + power_dBm + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	'''
	#
	#test gateway_disable
	#
	gateway_disable_options = ["Enable", "Disable"]
	for gateway_disable in gateway_disable_options:
		print "testing gateway_disable " + gateway_disable
		callString = "./freq_bw.py \'webinterface0.sh gateway_disable " + gateway_disable + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()

	#
	#end of basic test
	#
	print "----- End of basic test -----" 
	f.write("----- End of basic test -----")
	f.close()
	'''
	#jsonrpclib
	server = jsonrpclib.Server("http://172.20.4.127/streamscape_api")
	frequencies = server.supported_frequencies()
	print frequencies[0]
	'''
