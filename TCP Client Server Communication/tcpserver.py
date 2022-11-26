import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")
port = 12345

s.bind(('', port))
print ("socket binded to %s" %(port))
s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send("Thanks for connecting".encode())
    c.close()

    break