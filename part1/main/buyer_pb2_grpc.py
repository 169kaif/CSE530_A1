# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import buyer_pb2 as buyer__pb2


class BuyerServiceStub(object):
    """define services
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchItem = channel.unary_unary(
                '/BuyerService/SearchItem',
                request_serializer=buyer__pb2.SearchItemRequest.SerializeToString,
                response_deserializer=buyer__pb2.SearchItemResponse.FromString,
                )
        self.BuyItem = channel.unary_unary(
                '/BuyerService/BuyItem',
                request_serializer=buyer__pb2.BuyItemRequest.SerializeToString,
                response_deserializer=buyer__pb2.BuyItemResponse.FromString,
                )
        self.AddToWishList = channel.unary_unary(
                '/BuyerService/AddToWishList',
                request_serializer=buyer__pb2.AddToWishListRequest.SerializeToString,
                response_deserializer=buyer__pb2.AddToWishListResponse.FromString,
                )
        self.RateItem = channel.unary_unary(
                '/BuyerService/RateItem',
                request_serializer=buyer__pb2.RateItemRequest.SerializeToString,
                response_deserializer=buyer__pb2.RateItemResponse.FromString,
                )


class BuyerServiceServicer(object):
    """define services
    """

    def SearchItem(self, request, context):
        """search item
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuyItem(self, request, context):
        """buy item
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddToWishList(self, request, context):
        """add to wish list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RateItem(self, request, context):
        """rate item
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BuyerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchItem': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchItem,
                    request_deserializer=buyer__pb2.SearchItemRequest.FromString,
                    response_serializer=buyer__pb2.SearchItemResponse.SerializeToString,
            ),
            'BuyItem': grpc.unary_unary_rpc_method_handler(
                    servicer.BuyItem,
                    request_deserializer=buyer__pb2.BuyItemRequest.FromString,
                    response_serializer=buyer__pb2.BuyItemResponse.SerializeToString,
            ),
            'AddToWishList': grpc.unary_unary_rpc_method_handler(
                    servicer.AddToWishList,
                    request_deserializer=buyer__pb2.AddToWishListRequest.FromString,
                    response_serializer=buyer__pb2.AddToWishListResponse.SerializeToString,
            ),
            'RateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RateItem,
                    request_deserializer=buyer__pb2.RateItemRequest.FromString,
                    response_serializer=buyer__pb2.RateItemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BuyerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BuyerService(object):
    """define services
    """

    @staticmethod
    def SearchItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BuyerService/SearchItem',
            buyer__pb2.SearchItemRequest.SerializeToString,
            buyer__pb2.SearchItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuyItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BuyerService/BuyItem',
            buyer__pb2.BuyItemRequest.SerializeToString,
            buyer__pb2.BuyItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddToWishList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BuyerService/AddToWishList',
            buyer__pb2.AddToWishListRequest.SerializeToString,
            buyer__pb2.AddToWishListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BuyerService/RateItem',
            buyer__pb2.RateItemRequest.SerializeToString,
            buyer__pb2.RateItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)