# CC0 1.0 Universal (CC0 1.0)
# Public Domain Dedication
# https://github.com/nmrr

import socket
import hashlib
from time import sleep
import random
import sys

CLIENT_IP = "127.0.0.1"
CLIENT_PORT = 7777
CLIENT_FILENAME = 'output.txt'

file = open(CLIENT_FILENAME, 'rb')
data = file.read()
file.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sequence = []
for i in range(0,len(data),1350):
	sequence.append(i)

for j in range(10):
	
	if (j != 0):
		print("\n")
	print("New sequence")

	random.shuffle(sequence)
	counter = 0

	for i in sequence:

		outputData = b""
		outputData += str(CLIENT_FILENAME).encode('ascii')
		outputData += str('\0').encode('ascii')
		
		outputData += str(len(data)).encode('ascii')
		outputData += str('\0').encode('ascii')

		outputData += str(i).encode('ascii')
		outputData += str('\0').encode('ascii')


		maximum = i+1350
		if maximum >= len(data):
			maximum = len(data)

		outputData += data[i:maximum]

		sys.stdout.write("\r%d/%d   %f%%" % (counter, len(sequence), (100*(counter/len(sequence)))))
		sys.stdout.flush()

		dataHash = hashlib.sha256()
		dataHash.update(outputData)
		outputData += dataHash.digest()

		sock.sendto(outputData, (CLIENT_IP, CLIENT_PORT))
		counter += 1
		sleep(0.001)