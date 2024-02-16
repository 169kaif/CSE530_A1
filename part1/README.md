Part1 involves using grpc to implement an online shopping platform

We've used python3 as the programming language for this project.

so, to begin with first of we install the necessary dependencies
1) python3
2) pip
3) grpcio
4) grpcio-tools

After installing the dependencies, we create a proto file for our project called `all.proto` stored inside the protos folder.
This 'all.proto' file contains the protocol buffer definitions for our services.

The next step is to generate the server and client code from the proto file. To do this, we compile the proto file using python grpc.

This generates two files:
1) all_pb2.py
2) all_pb2_grpc.py

The `all_pb2.py` file contains the message classes and the `all_pb2_grpc.py` file contains the server and client classes.

Next, we implement the server and client code using the generated files.

The market acts as the server for the buyer and seller in most cases.
The buyer and seller request a service using the rpc call. The market server replies to the same after processing the request.

However, the server can also act as a client when it has to send notifications to the seller and buyer. In that case, the buyer and seller act as the server.
(ie buyer and seller act as client when requesting a service from the market and host a notification server when receiving notifications from the market)

Both the server and client code for the market is implemented in the `market.py` file.
The client code for the buyer and seller is implemented in the `buyer.py` and `seller.py` files respectively.
The server code for the buyer and seller is implemented in the `buyer_notif_server.py` and `seller_notif_server.py` files respectively.

All the code files have been commented and are easy to follow.