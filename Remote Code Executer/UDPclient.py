# modules used
import socket

client_address_family = socket.AF_INET
client_protocol = socket.SOCK_STREAM
client_skt = socket.socket(client_address_family, client_protocol)
client_ip = socket.gethostbyname("localhost") # gets the ip address of the hosting system
client_port = 9001
server_port = 9008
server_ip = "127.0.0.1"
client_skt.bind((client_ip, client_port))

# connecting to server
client_skt.connect((server_ip, server_port))
client_skt.recv(1024)

# connecting to server
client_skt.connect((server_ip, server_port))
client_skt.recv(1024)
while True:
    command = input()

    if command.strip() == "":
        print("Empty command")
    else:
        client_skt.send(command.strip().encode())
        response = client_skt.recv(1024)
        print(response, "\n")
    if command.strip() == "exit()":
        break