#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

from email import message
from socket import socket
import time
import zmq
import sys
import concurrent.futures
#context = zmq.Context()
#socket = context.socket(zmq.DEALER)
#socket.bind("tcp://*:5555")

#while True:
    #  Wait for next request from client
    #message = socket.recv()
    #print(f"Received request: {message}")
    #if(message==b"1"):
        #print("HLLO")

#        socket.send(b"NIGGA")
def connect_msg_server(zmq_context):
    print("Connecting to message server")
    msg_server_socket=context.socket(zmq.DEALER)
    msg_server_socket.connect("tcp://127.0.0.1:5558")
    autist='Register 127.0.0.1:5557'
    msg_server_socket.send(autist.encode())
    x=msg_server_socket.recv()
    print(x.decode())
def run(context):
    socket1 = context.socket(zmq.ROUTER)#socket for group 
    socket1.bind("tcp://127.0.0.1:5557")
    while True:
        msg = socket1.recv_multipart()
        print(msg)
        identity = msg[0]
        decoded_msg = msg[1].decode()
        print(f"Received request from {identity}: {decoded_msg}")
        response = "HI"
        socket1.send_multipart([identity, response.encode()])

if __name__ == "__main__":
    context=zmq.Context()
    connect_msg_server(context)
    run(context)

    
    
