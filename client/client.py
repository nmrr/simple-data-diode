import socket
import hashlib
import sys

CLIENT_PORT = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", CLIENT_PORT))

fileNameRequest = b''
sizeDataRequest = 0
newRequest = True
sizeDataStored = 0

arrayOutput = []

while True:
	data, addr = sock.recvfrom(1500)

	sha256 = data[len(data)-32:len(data)]
	dataHash = hashlib.sha256()
	dataHash.update(data[0:len(data)-32])

	if (dataHash.digest() == sha256):

		fileName = ""
		dataLength = ""
		dataPosition = ""

		position = 0
		for i in range(len(data)-32):
			if data[i] == 0x00:
				fileName = data[0:i]
				position = i+1
				break

		for i in range(position, len(data)-32, 1):
			if data[i] == 0x00:
				dataLength = int(data[position:i], base=10)
				position = i+1
				break

		for i in range(position, len(data)-32, 1):
			if data[i] == 0x00:
				dataPosition = int(data[position:i], base=10)
				position = i+1
				break

		if newRequest == True:
			newRequest = False
			fileNameRequest = fileName 
			sizeDataRequest = dataLength

		if newRequest == False and fileName == fileNameRequest and sizeDataRequest == dataLength:

			verify = False;
			for i in arrayOutput:
				if i[0] == dataPosition:
					verify = True
					break

			if (verify == False):
				arrayOutput.append([dataPosition, data[position:len(data)-32]])
				sizeDataStored += (len(data)-32-position)
				sys.stdout.write("\r%d/%d   %f%%" % (sizeDataStored, sizeDataRequest, (100*(sizeDataStored/sizeDataRequest))))
				sys.stdout.flush()


			if sizeDataStored == sizeDataRequest:
				print("\nfinish")
				arrayOutput.sort()

				with open("./output/" + fileNameRequest.decode('utf-8'), "wb") as outputFile:
					for i in arrayOutput:
						outputFile.write(i[1])
				break