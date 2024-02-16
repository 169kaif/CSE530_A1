import zmq
from datetime import datetime

messages=dict()
users=dict()

def connect_msg_server(zmq_context,port_no):
    print("Connecting to message server")
    msg_server_socket=context.socket(zmq.DEALER)
    msg_server_socket.connect("tcp://127.0.0.1:5558")
    msg_server_port='REGISTER 127.0.0.1:'+port_no
    msg_server_socket.send(msg_server_port.encode())
    x=msg_server_socket.recv()
    print(x.decode())

def run(context,port_no):
    socket1 = context.socket(zmq.ROUTER)#socket for group 
    socket1.bind("tcp://127.0.0.1:"+port_no)
    while True:
        msg = socket1.recv_multipart()
        identity = msg[0]
        decoded_msg = msg[1].decode()
        strlist=decoded_msg.split()
        if strlist[0]=="MSG":
            user_uuid=strlist[1]
            #get time in HH:MM:SS
            now = datetime.now()
            current_time = now.strftime('%H:%M:%S')
            print("Message sent from user "+user_uuid+" at "+current_time)
            if current_time not in messages:
                messages[current_time]=[]
            messages[current_time].append(" ".join(strlist[2:]))
            response="Success"
            socket1.send_multipart([identity,response.encode()])
        
        elif(strlist[0]=="QUERY"):
            user_uuid=strlist[1]
            print("Query request from user "+user_uuid)
            response=""
            if(len(strlist)==2):
                for _time in sorted(messages.keys()):
                    for msgs in messages[_time]:
                        response+=_time+": "+" "+msgs+"\n"
                        response+=" "
            else :
                time_stamp=strlist[2]
                timestamp=datetime.strptime(time_stamp,'%H:%M:%S')
                for _time in sorted(messages.keys()):
                    _timedt=datetime.strptime(_time,'%H:%M:%S')
                    if timestamp<=_timedt:
                        for msgs in messages[_time]:
                            response+=_time+": "+msgs+"\n"
            if response=="":
                    response="No messages found"  
            print(response)
            socket1.send_multipart([identity,response.encode()])
        elif strlist[0]=="JOIN":
            user_uuid=strlist[1]
            if user_uuid not in users:
                users[user_uuid]=identity
            print("User "+user_uuid+" joined")
        elif strlist[0]=="LEAVE":
            user_uuid=strlist[1]
            if user_uuid in users:
                del users[user_uuid]
            print("User "+user_uuid+" left")

if __name__ == "__main__":
    context=zmq.Context()
    my_port=input("Enter your port not 5558:")
    connect_msg_server(context,my_port)
    run(context,my_port)