from socket import *
serverPort = 2212
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    #capitalizedSentence = sentence.upper()
    #connectionSocket.send(capitalizedSentence.encode())
    if (sentence): print ('Got a sentence from client\n')
    returnsentence = "Hello, " + sentence + "!"
    connectionSocket.send(returnsentence.encode())
    connectionSocket.close()
