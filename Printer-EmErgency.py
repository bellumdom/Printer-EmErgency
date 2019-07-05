#!/usr/bin/python

import os
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

helper = input("For Instructions on how to use the program, type help. For info about the creater, type info. To continue press enter: ")
if helper == "help":
       print("When prompted to enter the host you must Enter the local IP address of the printer.")
       print("If the given host is a printer and it is connected to the internet then you will see success and instructions")
       input("Press enter to continue: ")
elif helper == "info":
       print("This proggram was made by bellum Dom. Watch out for more projects by me such as redirecting malicious traffic")
       input("Press enter to continue: ")

host = input("[*] Enter The Host: ")
port = 9100

def ncscript(host):
	os.system("nc " + host + " 9100")

finalhelp = "Type in your message, press enter then finnaly do Control-C to finish and "

if sock.connect_ex((host,port)):
	print("Port 9100 is closed")
else:
    print("Port 9100 is open")
    print(finalhelp)
    ncscript(host)
