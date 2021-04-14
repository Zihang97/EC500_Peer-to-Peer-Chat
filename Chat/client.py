import socket
import sys
from Database.database import *

serverAddressPort = ("168.122.206.223", 20001)

bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

status = input('Do you want to be discovered? ')

print('please input messages that you what to send: ')

# Send to server using created UDP socket
if status == 'yes':
	messages = msg_sending(cursor)
	for message in messages:
		bytesToSend = message.encode()
		UDPClientSocket.sendto(bytesToSend, serverAddressPort)

	while True:

		line = input()

		bytesToSend = line.encode()

		UDPClientSocket.sendto(bytesToSend, serverAddressPort)

		msgFromServer = UDPClientSocket.recvfrom(bufferSize)

		msg = "Message from Server {}".format(msgFromServer[0])
		print(msg)

		

else:
	name = input('Who do you want to talk to? ')
	for line in sys.stdin:
		try:
			msg_to_send(cursor, name, line)
		except:
			print('The person you want to chat is not in address book, please add it')
			ip = input('please enter his/her ip address: ')
			create_user(cursor, name, ip)
