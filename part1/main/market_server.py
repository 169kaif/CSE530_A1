#import grpc
import grpc

#import seller classes generated by grpc
import seller_pb2
import seller_pb2_grpc

#import buyer classes generated by grpc
import buyer_pb2
import buyer_pb2_grpc

#import market classes generated by grpc
import market_pb2
import market_pb2_grpc

class ProductDetails:
    def __init__(self, name,item_id, item_price, quantity, category, description, seller_address):
        self.name = name
        self.item_id = item_id
        self.item_price = item_price
        self.quantity = quantity
        self.category = category
        self.description = description
        self.seller_address = seller_address

class MarketServiceServicer(market_pb2_grpc.MarketServiceServicer):
    """ Add methods to implement functionality of the services required by the seller"""

    def __init__(self):
        self.registered_sellers = {}
        self.products=[]

    def RegisterSeller(self, request, context):
        #extract uuid and add key to dictionary
        curr_seller_uuid = request.message
        server_response=seller_pb2.RegisterSellerResponse()
        #validate user
        if (curr_seller_uuid in self.registered_sellers.keys()):
            server_response.message= "FAILURE: USER ALREADY EXISTS"
        else:
            self.registered_sellers = []
            server_response.message= "SUCCESS: USER ADDED"
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

        #retrieve seller id
        curr_seller_id = request.seller_id

        #retrieve uuid
        curr_seller_uuid = request.message

        new_prod = ProductDetails(curr_item_name,
                                  curr_item_id, 
                                  curr_item_price,
                                  curr_item_quantity,
                                  curr_item_category,
                                  curr_item_description,
                                  curr_item_selleraddress)
        
        server_response = seller_pb2.SellItemResponse()

        #add products to product list if it doesn't already exist
        for product in self.products:
            if (product.item_id == curr_item_id): #product already exists, return failure
                server_response.message = "FAILURE, ITEM ALREADY EXISTS"
                return server_response
            
        #product doesn't exist
        self.products.append(new_prod)
        server_response.message = "SUCCESS, ITEM ADDED SUCCESSFULLY"
        return server_response
    
    def UpdateItem(self, request, context):

        #retrieve info from the update item request
        seller_uuid = request.message #this is the seller uuid that the product originally has
        req_item_id = request.item_id
        new_item_price = request.new_item_price
        new_item_quantity = request.new_quantity

        #new seller uuid not needed but too lazy to change and recompile the proto files

        server_response = seller_pb2.UpdateItemResponse()

        #search for item in the products list, validate seller credentials and update
        for item in self.products:
            if (item.item_id == req_item_id and item.seller_address == seller_uuid):
                item.item_price = new_item_price
                item.quantity = new_item_quantity
                server_response.message = "SUCCESS"
                return server_response
        
        #failed either because no item match found or invalid credentials
        server_response.message = "FAILURE"
        return server_response
    
    def DeleteItem(self, request, context):

        #retrieve info from the delete item request
        req_item_id = request.item_id
        seller_uuid = request.seller_address

        server_response = seller_pb2.DeleteItemResponse()

        #search for item in the products list, validate credentials and delete
        for item in self.products:
            if (item.item_id == req_item_id and item.seller_address == seller_uuid):
                self.products.remove(item)
                server_response.message = f"DELETED ITEM W/ ITEM ID:{req_item_id} SUCCESSFULLY"
                return server_response
            
        #failure to delete the requested item either because item not found in the products list or credentials not verified
        server_response.message = "FAILURE"
        return server_response
    
    

    
    def SearchItem(self, request,context):
        item_name=request.item_name
        item_category=request.category_name
        
        
    
    def BuyItem(self, request, context):

    def AddToWishList(self, request, context):

    def RateItem(self, request, context):
