from concurrent import futures
import logging
import math
import time

#import grpc
import grpc

#import seller classes generated by grpc
import seller_pb2
import seller_pb2_grpc

#import buyer classes generated by grpc
import buyer_pb2
import buyer_pb2_grpc

#import market classes generated by grpc
import all_pb2
import all_pb2_grpc

#import all classes generated by grpc
import all_pb2
import all_pb2_grpc

class ProductDetails:
    def __init__(self, name,item_id, item_price, quantity, category, description, rating, seller_address):
        self.name = name
        self.item_id = item_id
        self.item_price = item_price
        self.quantity = quantity
        self.category = category
        self.description = description
        self.rating = rating
        self.seller_address = seller_address

class AllServicesServicer(all_pb2_grpc.AllServicesServicer):
    """ Add methods to implement functionality of the services required by the seller"""

    def __init__(self):
        self.registered_sellers = []
        self.products=[]

    def RegisterSeller(self, request, context):
        #extract uuid and add key to dictionary
        curr_seller_uuid = request.message
        server_response=all_pb2.RegisterSellerResponse()
        #validate user
        if (curr_seller_uuid in self.registered_sellers):
            server_response.message= "FAILURE: USER ALREADY EXISTS"
        else:
            self.registered_sellers.append(curr_seller_uuid)
            server_response.message= "SUCCESS: USER ADDED w/ UUID " + curr_seller_uuid
        print(self.products)
        print(self.registered_sellers)
        return server_response
    
    def SellItem(self, request, context):

        #retrieve item info
        curr_item_id = request.item.item_id
        curr_item_name = request.item.name
        curr_item_price = request.item.item_price
        curr_item_quantity = request.item.quantity
        curr_item_category = request.item.category
        curr_item_description = request.item.description
        curr_item_selleraddress = request.item.seller_address
        server_response = all_pb2.SellItemResponse()

        if (curr_item_selleraddress not in self.registered_sellers):
            server_response.message = "FAILURE, USER NOT REGISTERED"
            return server_response

        new_prod = ProductDetails(curr_item_name,
                                  curr_item_id, 
                                  curr_item_price,
                                  curr_item_quantity,
                                  curr_item_category,
                                  curr_item_description,
                                  -1,
                                  curr_item_selleraddress)
        

        #add products to product list if it doesn't already exist
        for product in self.products:
            if (product.item_id == curr_item_id): #product already exists, return failure
                server_response.message = "FAILURE, ITEM ALREADY EXISTS"
                return server_response
            
        #product doesn't exist
        self.products.append(new_prod)

        #debug
        print(self.registered_sellers)
        print(self.products)

        server_response.message = "SUCCESS, ITEM ADDED SUCCESSFULLY"
        return server_response
    
    def UpdateItem(self, request, context):

        #retrieve info from the update item request
        some_id = request.seller_id #this is the seller uuid that the product originally has
        req_item_id = request.item_id
        new_item_price = request.new_item_price
        new_item_quantity = request.new_quantity

        #new seller uuid not needed but too lazy to change and recompile the proto files

        server_response = all_pb2.UpdateItemResponse()

        #search for item in the products list, validate seller credentials and update
        for item in self.products:
            if (item.item_id == req_item_id and item.seller_address == some_id):
                item.item_price = new_item_price
                item.quantity = new_item_quantity
                server_response.message = "SUCCESS"

                #debug
                print(self.registered_sellers)
                print(self.products)

                return server_response
            
        #debug
        print(self.registered_sellers)
        print(self.products)
        
        #failed either because no item match found or invalid credentials
        server_response.message = "FAILURE"
        return server_response
    
    def DeleteItem(self, request, context):

        #retrieve info from the delete item request
        req_item_id = request.item_id
        seller_uuid = request.seller_address

        server_response = all_pb2.DeleteItemResponse()

        #search for item in the products list, validate credentials and delete
        for item in self.products:
            if (item.item_id == req_item_id and item.seller_address == seller_uuid):
                self.products.remove(item)
                server_response.message = f"DELETED ITEM W/ ITEM ID:{req_item_id} SUCCESSFULLY"

                #debug
                print(self.registered_sellers)
                print(self.products)
                return server_response
            
        #debug
        print(self.registered_sellers)
        print(self.products)
            
        #failure to delete the requested item either because item not found in the products list or credentials not verified
        server_response.message = "FAILURE"
        return server_response
    
    def DisplaySellerItemsResponse(self, request, context):
        #retrieve uuid of the seller
        seller_uuid = request.seller_id
        user_search_response=[]
        for i in self.products:
            if (i.seller_address == seller_uuid):
                item=seller_pb2.Item()
                item.name=i.name
                item.category=i.category
                item.item_price=i.item_price
                item.quantity=i.quantity
                item.description=i.description
                item.seller_address=i.seller_address
                item.item_id=i.item_id
                item.rating = i.rating
                user_search_response.append(item)
                
        response=all_pb2.DisplaySellerItemResponse()
        response.items.extend(user_search_response)
        return response
    
   
    def SearchItem(self, request,context):
        item_name=request.item_name
        item_category=request.category_name
        user_search_response=[]
        for i in self.products:
            if ((i.category==item_category) or item_category=="ANY") and i.name==item_name:
                item=seller_pb2.Item()
                item.name=i.name
                item.category=i.category
                item.item_price=i.item_price
                item.quantity=i.quantity
                item.description=i.description
                item.seller_address=i.seller_address
                item.item_id=i.item_id
                item.rating = i.rating
                user_search_response.append(item)
        response=all_pb2.SearchItemResponse()
        response.items.extend(user_search_response)
        return response
        
    def BuyItem(self, request, context):
        item_id=request.item_id
        item_quantity=request.item_quantity
        flag =False

        for i in self.products:
            if item_id==i.item_id and item_quantity>=i.quantity and i.quantity>0:
                i.quantity-=item_quantity
                flag=True
                break
        response=all_pb2.BuyItemResponse()
        if(not flag):
            response.status="Failure"
        else:
            response.status="Success"
        return response

    def AddToWishList(self, request, context):
        
        return None

    def RateItem(self, request, context):
        item_name=request.item_id
        item_rating=request.rating
        server_response = all_pb2.RateItemResponse()
        for i in self.products:
            if (i.item_id==item_name):
                i.rating=item_rating
                server_response.status=f"UPDATED RATING OF ITEM W/ ITEM ID:{item_name} SUCCESSFULLY"
                return server_response
        server_response.status = "FAILURE"
        return server_response
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    all_pb2_grpc.add_AllServicesServicer_to_server(
        AllServicesServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()