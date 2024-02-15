#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

from email import message
import time
from urllib import request
import zmq
import sys
import concurrent.futures
import json
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
def add_group(msg:str,grp_dict:dict):
    if msg[1] in grp_dict.values():
        return "already Registered"
    else:
        grp_dict[len(grp_dict)+1]=msg[1]
        return "Group Port sucessfully ADDED"
def run():
    context = zmq.Context()
    socket = context.socket(zmq.ROUTER)
    socket.bind("tcp://127.0.0.1:5558")
    grp_dictionary = {}
    while True:
        msg = socket.recv_multipart()
        identity = msg[0]
        decoded_msg = msg[1].decode()
        request_msg=decoded_msg.split(" ")
        if(request_msg[0].lower()=="register"):
            response=add_group(request_msg,grp_dictionary)
            socket.send_multipart([identity, response.encode()])
        elif decoded_msg=='get group info':
            response=json.dumps(grp_dictionary)
            socket.send_multipart([identity,response.encode()])

if __name__ == "__main__":
    context=zmq.Context()
    run()

    
    
