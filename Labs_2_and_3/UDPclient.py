from socket import *
serverName = 'storm.cise.ufl.edu'
#serverName = 'localhost'
serverPort = 2212
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('What\'s your name, and what city were you born in?\n> ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
