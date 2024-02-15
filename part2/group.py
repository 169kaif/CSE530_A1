import zmq
from datetime import datetime

messages=dict()
users=dict()

def connect_msg_server(zmq_context):
    print("Connecting to message server")
    msg_server_socket=context.socket(zmq.DEALER)
    my_port=input("Enter your port not 5557:")
    msg_server_socket.connect("tcp://127.0.0.1:"+my_port)
    msg_server_port='REGISTER 127.0.0.1:5557'
    msg_server_socket.send(msg_server_port.encode())
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
        strlist=decoded_msg.split()
        if strlist[0]=="MSG":
            print(f"Message from {identity}")
            #get time in HH:MM:SS
            now = datetime.now()
            current_time = now.strftime('%H:%M:%S')
            if current_time not in messages:
                messages[current_time]=[]
            messages[current_time].append(" ".join(strlist[1:]))
            response="Success"
            socket1.send_multipart([identity,response.encode()])
        elif(strlist[0]=="QUERY"):
            print(f"Query from {identity}")
            response=""
            if(len(strlist)==1):
                for _time in sorted(messages.keys()):
                    response+=_time+": "+" ".join(messages[_time])+"\n"
            else :
                time_stamp=strlist[1]
                for _time in sorted(messages.keys()):
                    if _time>=time_stamp:
                        response+=_time+": "+" ".join(messages[_time])+"\n"
                if response==" ":
                    response="No messages found"    
            socket1.send_multipart([identity,response.encode()])
        elif strlist[0]=="JOIN":
            user_uuid=strlist[1]
            if user_uuid not in users:
                users[user_uuid]=identity
        elif strlist[0]=="LEAVE":
            user_uuid=strlist[1]
            if user_uuid in users:
                del users[user_uuid]

if __name__ == "__main__":
    context=zmq.Context()
    connect_msg_server(context)
    run(context)