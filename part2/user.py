#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import json
import zmq

context = zmq.Context()

#  Socket to talk to server

address_dict=dict()
address_dict["msg_server"]='tcp://127.0.0.1:5558'
specific_socket=dict()
msg_server_socket=context.socket(zmq.DEALER)
msg_server_socket.connect("tcp://127.0.0.1:5558")
specific_socket['msg_server']=msg_server_socket
#  Do 10 requests, waiting each time for a response
while True:
    print("1)get a list of available groups")
    print("2)connect to group")
    print("3)disconnect to a group")
    print("4)exit")
    choice=input("Enter choice")
    if(choice=='1'):
        specific_socket['msg_server'].send("get group info".encode())
        msg_recv=specific_socket['msg_server'].recv()
        msg_recv=json.loads(msg_recv.decode())
        print(msg_recv)
    elif(choice=='2'):
        group_ip_port=input("enter group ip:port: ")
        if group_ip_port not in specific_socket:
            specific_socket[group_ip_port]=context.socket(zmq.DEALER)
            specific_socket[group_ip_port].connect("tcp://"+group_ip_port)
        while True:
            grp_msg=input("Enter msg(enter EXIT to leave):")
            if(grp_msg=='EXIT'):
                break
            specific_socket[group_ip_port].send(grp_msg.encode())
    elif(choice=='3'):
        group_ip_port=input("enter group ip:port: ")
        if group_ip_port not in specific_socket:
            print("INVALID IP:PORT")
        else:
            print("YET TO IMPLEMENT")
            #delete group 
        


    else:
        print("INVALID INPUT")
        
