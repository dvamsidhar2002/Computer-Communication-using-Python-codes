# importing required libraries
import socket
import threading
import datetime
import sys, subprocess

#creates and returns a socket
def create_socket():
    #Protocol = UDB, addressFamily = ipv4
    protocol = socket.SOCK_STREAM
    address_family = socket.AF_INET
    #socket creation
    skt = socket.socket(address_family, protocol)
    #Bind information
    server_ip = ""
    server_port = 9008
    #Binding port and ip
    skt.bind((server_ip, server_port))
    return skt
skt = create_socket()

# listening for incomming connection requests from clients
skt.listen()

# runs infinitely waiting for a connection request
while True:
    # accepts a request to connect from client
    skt_object, address_info = skt.accept()
    skt_object.send(b"Connected")
    #creates a thread on the fly for each new user
    threading.Thread(name=str(datetime.datetime.now()), target=lambda : request_processor(skt_object, address_info)).start()


# processing requests
def request_processor(skt_object, address_info):
    # constandly listens for data from client
    while True:
        request = skt_object.recv(1024)

        # checks whether user wants to terminate session
        if request.decode() == "exit()":
            skt_object.send(b"Session terminated")
            skt_object.close()
            break

        # executes requests and returns output
        status_output = subprocess.getstatusoutput(request)

        # returns output to user
        skt_object.send(status_output[1].encode())

        # logs request
        logger({"request": request, "address_info": address_info, "datetime": datetime.datetime.now(),
                "return_code": status_output[0]})


skt = create_socket()


# logging data
def logger(request_dict: dict):
    # creating a log dictionary
    log = {
        "datetime": str(request_dict['datetime']),
        "request": request_dict['request'],
        "ip_address": request_dict['address_info'][0],
        "port": request_dict['address_info'][1],
        "return_code": request_dict['return_code']
    }

    # writes data to file in json format
    # creates a log file every day
    try:
        log_file = open("{}-log.txt".format(str(datetime.date.today())), "a")
        log_file.write("{}\n".format(log))
        print(log)
    except Exception as e:
        print("Error: ", sys.exc_info()[1], " ", str(datetime.datetime.now()))
