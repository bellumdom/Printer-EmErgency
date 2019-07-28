#!/usr/bin/python2

import socket



print("""\ 

	___________ ___ _      .__        __                 _________
\______   \_______|__| _____/  |_  ___________  \_   _____/ _____   ___________  ____   ____   ____   ____ ___.__.
 |     ___/\_  __ \  |/    \   __\/ __ \_  __ \  |    __)_ /     \_/ __ \_  __ \/ ___\_/ __ \ /    \_/ ___<   |  |
 |    |     |  | \/  |   |  \  | \  ___/|  | \/  |        \  Y Y  \  ___/|  | \/ /_/  >  ___/|   |  \  \___\___  |
 |____|     |__|  |__|___|  /__|  \___  >__|    /_______  /__|_|  /\___  >__|  \___  / \___  >___|  /\___  > ____|
                          \/          \/                \/      \/     \/     /_____/      \/     \/     \/\/     

		""")
TCP_IP = raw_input("[*] Please enter the IP address of the printer: ")
TCP_PORT = 9100
BUFFER_SIZE = 1024
MESSAGE = raw_input("Please enter your emergency message: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("Received data from printer IP", TCP_IP, ":", data)
