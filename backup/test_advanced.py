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
	f.write("----- Start of advanced test -----\n")
	ip = args[0]
	browser = args[1]

	#
	#test link distance
	#
	
	distance_value = ["500"]
	for distance in distance_value:
		print "testing link_distance " + distance
		callString = "./textfield.py '" + ip + " " + browser + " webinterface2.sh link_distance " + distance + "'"
		#callString = "./textfield.py '172.20.4.180 firefox webinterface2.sh link_distance " + str(distance) + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	
	#
	#test rts_disable
	#
	rts_cts = ["Enable", "Disable"]
	for E_D in rts_cts:
		print "testing rts_disable " + E_D
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh rts_disable " + E_D + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test threshold
	#
	thresholds = ["1600", "800", "400", "200"]
	for threshold in thresholds:
		print "testing fragmentation threshold " + threshold
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh aggr_thresh " + threshold + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test max_gound_speed
	#
	max_speeds = ["0", "2", "10", "20", "40", "70"]
	for max_speed in max_speeds:
		print "testing max_ground_speed " + max_speed
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh max_speed " + max_speed + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test burst time
	#
	burst_times = ["2", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
	for burst_time in burst_times:
		print "testing burst_time " + burst_time
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh burst_time " + burst_time + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test encryption_disable
	#
	encryption_disable = ["Disable", "Enable"]
	for enc_disable in encryption_disable:
		print "testing enc_disable " + enc_disable
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh enc_disable " + enc_disable + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test enc_key_len 
	#
	enc_key_lens = ["128", "256"]
	for enc_key_len in enc_key_lens:
		print "testing enc_key_len " + enc_key_len
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh enc_key_len " + enc_key_len + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test enc_key
	#
	enc_key = ["silvus745"]
	for key in enc_key:
		print "testing enc_key " + key
		callString = "./textfield.py '" + ip + " " + browser + " webinterface2.sh enc_key " + key + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#disable encryption_disable
	#
	enc_disable = ["Disable"]
	for en_disable in enc_disable:
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh enc_disable " + en_disable + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()

	#
	#test mcs
	#
	mcs_options = ["Auto", "mcs0", "mcs1", "mcs2", "mcs3", "mcs4", "mcs8", "mcs9", "mcs10", "mcs11", "mcs12", "mcs16", "mcs17", "mcs18", "mcs19", "mcs20", "mcs24", "mcs25", "mcs26", "mcs27", "mcs28"]
	for mcs in mcs_options:
		print "testing mcs " + mcs
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh enc_key " + mcs + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test phytest
	#
	phytest_options = ["Network", "PHY"]
	for phytest in phytest_options:
		print "testing phytest " + phytest
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh phytest " + phytest + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()


	
	#
	#test virtual ip
	#
	virtual_ip_disable = ["Disable", "Enable"]
	for virtual_disable in virtual_ip_disable:
		print "testing virtual_ip_disable " + virtual_disable
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh vir_ip_disable " + virtual_disable + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	vir_addrs = ["192.168.10.254", "192.168.10.253"]
	for vir_addr in vir_addrs:
		print "testing virtual_ip_address " + vir_addr
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh vir_addr " + vir_addr + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	vir_netmasks = ["255.255.255.0"]
	for vir_netmask in vir_netmasks:
		print "testing virtual_ip_netmask " + vir_netmask
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh vir_netmask " + vir_netmask + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	vir_gws = ["192.168.10.1"]
	for vir_gw in vir_gws:
		print "testing virtual_ip_gw " + vir_gw
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh vir_gw " + vir_gw + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#disable
	vir_ip_disable = ["Disable"]
	for vir_disable in vir_ip_disable:
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh vir_ip_disable " + vir_disable + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()

	#
	#test vpn
	#
	vpn_disable_options = ["Disable", "Enable"]
	for vpn_disable in vpn_disable_options:
		print "testing vpn_disable " + vpn_disable
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh vpn_disable " + vpn_disable + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test vpn_ip
	#
	vpn_ip_options = ["10.0.1.4"]
	for vpn_ip in vpn_ip_options:
		print "testing vpn_ip " + vpn_ip
		callString = "./textfield.py '" + ip + " " + browser + " webinterface2.sh vpn_addr " + vpn_ip + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#
	#test vpn_port
	#
	vpn_port_options = ["9000"]
	for vpn_port in vpn_port_options:
		print "testing vpn_port " + vpn_port
		callString = "./textfield.py '" + ip + " " + browser + " webinterface2.sh vpn_addr " + vpn_port + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()
	#disable
	disable_vpn = ["Disable"]
	for vpn_d in disable_vpn:
		callString = "./select.py '" + ip + " " + browser + " webinterface2.sh vpn_disable " + vpn_d + "'"
		proc = subprocess.Popen(callString, shell=True)
		proc.wait()


	#
	#end of advanced test
	#
	print "----- End of advanced test -----" 
	f.write("------------------------" + time.asctime() + "------------------------\n")
	f.write("----- End of advanced test -----\n\n")
	f.close()
