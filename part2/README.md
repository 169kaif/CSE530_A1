readme for part2

there are three python files in this part group.py which act as a group , user.py which acts as a user and message server.py which maintains the list of group.py ip:port and gives the list to user if sent a query for it

explaining message_server.py:
socket type used for message_server.py is a router socket which makes it easy to maintain a request-reply pattern, for that we do not even need a thread to maintain concurrency as router socket uses a roundrobbin pattern to send message to multiple client.
there are only two functions for message_server.py one is to register groups ip:port  and other is to send info of the groups ip:port to the user


explaining group.py:
two sockets are used for group.py,router socket and dealer socket, dealer socket is initiated for only once when the group has to register its router socket ip:port to the message_server.py,router socket is used to implement the group functionality such as a request reply service.group.py maintains a dictionary where each messages is stored with key being the time it received the message
makes it easier to handle the query when time stamp is mentioned other than that user also maintains aa uuid of the user connected 


explaining user.py 
in user.py multiple sockets are used as user is connected to many groups as well its connected to message_server.py every user has an uuid.users basic functionality is to send queries to message_server.py to get info about the groups and send messages to the groups its connected to and get messages from them


