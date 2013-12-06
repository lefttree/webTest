#!/usr/bin/python
import subprocess, time
import jsonrpclib
import fileinput
import sys

if __name__ == '__main__':
	print "testing basic"
	callString = "./test_basic.py '172.20.4.180 firefox'"
	proc = subprocess.Popen(callString, shell=True)
	proc.wait()
	print "testing advanced"
	callString = "./test_advanced.py '172.20.4.180 firefox'"
	proc = subprocess.Popen(callString, shell=True)
	proc.wait()
	print "testing qos"
	callString = "./test_qos.py '172.20.4.180 firefox'"
	proc = subprocess.Popen(callString, shell=True)
	proc.wait()
	print "testing serial"
	callString = "./test_serial.py '172.20.4.180 firefox'"
	proc = subprocess.Popen(callString, shell=True)
	proc.wait()
	print "testing diagnostics"
	callString = "./test_diagnostics.py '172.20.4.180 firefox'"
	proc = subprocess.Popen(callString, shell=True)
	proc.wait()


