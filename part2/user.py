import json
import zmq
import time
import uuid
context = zmq.Context()

#get user uuid
user_uuid=str(uuid.uuid1())

specific_socket=dict()
msg_server_socket=context.socket(zmq.DEALER)


msg_server_socket.connect("tcp://127.0.0.1:5558")
specific_socket['msg_server']=msg_server_socket


while True:

    print("1)get a list of available groups")
    print("2)connect to group")
    print("3)disconnect from a group")
    print("4)exit")

    choice=input("Enter choice")

    if(choice=='1'):
        specific_socket['msg_server'].send("get group info".encode())
        msg_recv=specific_socket['msg_server'].recv()
        msg_recv=json.loads(msg_recv.decode())
        print(msg_recv)


    elif(choice=='2'):
        group_ip_port=input("ENTER GROUP IP:PORT")

        if group_ip_port not in specific_socket:
            specific_socket[group_ip_port]=context.socket(zmq.DEALER)
            specific_socket[group_ip_port].connect("tcp://"+group_ip_port)

            #send uuid to group
            grp_msg= f"JOIN {user_uuid}"
            specific_socket[group_ip_port].send(grp_msg.encode())
        else:
            print("ALREADY CONNECTED TO GROUP")

        while True:
            print("1)send message to group")
            print("2)Get past messages")
            print("3)Exit menu")
            hj=input("Enter choice: ")
            if(hj=='1'):
                msg=input("Enter message to send: ")
                msg="MSG "+user_uuid+" "+msg
                specific_socket[group_ip_port].send(msg.encode())
                msg_recv=specific_socket[group_ip_port].recv()
                print(msg_recv.decode())
            elif(hj=='2'):
                time_stamp=input("Enter time stamp or leave empty for all messages:")
                grp_msg="QUERY "+user_uuid+" "+time_stamp
                specific_socket[group_ip_port].send(grp_msg.encode())
                msg_recv=specific_socket[group_ip_port].recv()
                print(msg_recv)
            elif(hj=='3'):
                break
            else:
                print("INVALID INPUT")
    elif(choice=='3'):

        #take group ip:port as input
        group_ip_port=input("ENTER GROUP IP:PORT")

        #check if ip:port is invalid
        if group_ip_port not in specific_socket:
            print("INVALID IP:PORT")

        #disconnect from the group
        else:
            #message to group to leave
            grp_msg= f"LEAVE {user_uuid}"
            specific_socket[group_ip_port].send(grp_msg.encode())
            specific_socket[group_ip_port].close()
            del specific_socket[group_ip_port]
    elif(choice=='4'):
        break
    else:
        print("INVALID INPUT")