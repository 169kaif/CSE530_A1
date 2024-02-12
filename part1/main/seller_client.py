from unicodedata import category
import grpc
import grpc_tools
import seller_pb2
import seller_pb2_grpc
import buyer_pb2
import buyer_pb2_grpc
import all_pb2
import all_pb2_grpc

def display_requests():
    print("SellItem:1")
    print("UpdateItem:2")
    print("DeleteItem:3")
    print("DisplaySellerItems:4")
    print("Exit:5")
def sellitem():
    Item_ID=int(input("Enter Item ID: "))
    category=input("Enter Category Name: ")
    Item_name=input("Enter Item Name: ")
    Item_Price=float(input("Enter Item Price: "))
    quantity=int(input("Enter Quantity: "))
    description=input("Enter Description: ")
    return Item_ID,Item_name,Item_Price,quantity,category,description
def updateitem():
    Item_ID=int(input("Enter Item ID: "))
    Item_Price=float(input("Enter Item Price: "))
    quantity=int(input("Enter Quantity: "))
    return Item_ID,Item_Price,quantity
def deleteItem():
    Item_ID=int(input("Enter Item ID: "))
    return Item_ID



    
def Run():
    print("Hello Welcome")
    print("Register yourself")
    #connecting to the server(Market)
    #connection initiated
    #displaying the result
    with grpc.insecure_channel('localhost:50051') as channel:
        stub=all_pb2_grpc.AllServicesStub(channel)
        seller_id="abc"
        while(True):
            display_requests()
            rpc_input=int(input("Enter the request you want to use: "))
            if rpc_input==1:
                
                Item_ID,Item_name,Item_Price,quantity,category,description=sellitem()
                sellerItem=all_pb2.Item(item_id=Item_ID,name=Item_name,item_price=Item_Price,quantity=quantity,category=category,description=description,seller_address="")
                sellitem_request=all_pb2.SellItemRequest(message="",item=sellerItem,seller_id=seller_id)
                sellitem_response=stub.SellItem(sellitem_request)
                print(sellitem_response.message)



            elif rpc_input==2:
                Item_ID,Item_Price,quantity=updateitem()
                updateitemm=all_pb2.UpdateItemRequest(seller_id=seller_id,item_id=Item_ID,new_item_price=Item_Price,new_quantity=quantity,new_seller_address="")
                updateitem_response=stub.UpdateItem(updateitemm)
                print(updateitem_response.message)
                
            elif rpc_input==3:
                Item_ID=deleteItem()
                deleteItem=all_pb2.DeleteItemRequesr(seller_id=seller_id,seller_address="",item_id=Item_ID)
                deleteItem_response=stub.DeleteItem(deleteItem)
                print(deleteItem_response.message)
            elif rpc_input==4:
                show_item=all_pb2.DisplaySellerItemsRequest(seller_id=seller_id)
                show_item_response=stub.DisplaySellerItems(show_item)
                if show_item_response.items:
                    for item in show_item_response.items:
                            print(f"Item ID: {item.item_id}")
                            print(f"Name: {item.name}")
                            print(f"Price: ${item.item_price}")
                            print(f"Quantity: {item.quantity}")
                            print(f"Category: {item.category}")
                            print(f"Description: {item.description}")
                            print(f"Seller Address: {item.seller_address}")
                            print("-" * 30)  
                else:
                    print("No items found.")


            elif rpc_input==5:
                break
            else:
                print("Invalid Input")

if __name__ == "__main__":
    Run()