from socket import *
serverPort = 2212
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.decode().upper()
    if (message): print ('Got a message from client\n')
    modifiedMessage = "Howdy there, " + message + "!"
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
