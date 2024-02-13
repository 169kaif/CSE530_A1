from concurrent import futures
import logging
import math
import time

#import grpc
import grpc

#import all classes generated by grpc
import all_pb2
import all_pb2_grpc

class AllServicesServicer(all_pb2_grpc.AllServicesServicer):
    """Add methods to listen for notifs from the market(when market acts as client)"""

    def __init__(self):
        self.notif = ""

    def NotifyClient(self, request, context):
        self.notif = request.Notification.message

        #print the notification
        print(self.notification)

        server_response=all_pb2.NotificationResponse()
        server_response.message = "SUCCESS"

        return server_response
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    all_pb2_grpc.add_AllServicesServicer_to_server(
        AllServicesServicer(), server
    )
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()