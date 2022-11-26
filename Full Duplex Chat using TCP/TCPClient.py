from socket import *


HOST = 'localhost'                #Just for testing, can change it later
PORT = 8000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    message = input(">")             #The sending data loop for the client, 'go' stops the loop
    if message == '':
        break
    while message.lower() != 'go':
        message += '\r\n'
        tcpCliSock.send(message.encode())
        message = input(">")
    if message == '':
        break
    else:                            # Receiving data loop, stops when empty symbol received.
        message = 'continue\r\n'
        tcpCliSock.send(message.encode())
        data = tcpCliSock.recv(BUFSIZ)
        data = data.decode().strip()
    if not data:
        break
    while data.lower() != 'continue':        # sent by the server when it is done typing.
        print(data)
        data = tcpCliSock.recv(BUFSIZ)
        data = data.decode().strip()
tcpCliSock.close()