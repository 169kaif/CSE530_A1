import grpc
import all_pb2
import all_pb2_grpc
import uuid


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = all_pb2_grpc.AllServicesStub(channel)
        print("Registering Buyer!!!!")
        buyerr_uuid=str(uuid.uuid1())
        buyer_server_ip="localhost"
        buyer_server_port="12345"
        buyer_request=all_pb2.RegisterBuyerRequest(message=buyerr_uuid,notif_server_ip=buyer_server_ip,notif_server_port=buyer_server_port)
        buyer_response=stub.RegisterBuyer(buyer_request)
        print(buyer_response.message)

        while True:
            print("1. Search_Item")
            print("2. Buy_Item")
            print("3. Add_To_WishList")
            print("4. Rate_Item")
            print("5. Exit")
            rpc_call = input("Enter option: ")

            if rpc_call == "1":
                name=input("Enter name of item to search(leave empty to display all): ")
                category=input("Enter category of item to search(type ANY to display all): ")
                search_request = all_pb2.SearchItemRequest(item_name=name, category_name=category)
                search_reply = stub.SearchItem(search_request)
                if search_reply.items:
                    print("Items found:")
                    for item in search_reply.items:
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

            elif rpc_call == "2":
                item_id = int(input("Enter the item id to buy: "))
                quantity = int(input("Enter the quantity to buy: "))
                buy_request = all_pb2.BuyItemRequest(item_id=item_id, item_quantity=quantity,buyer_uuid=buyerr_uuid)
                buy_reply = stub.BuyItem(buy_request)
                print(buy_reply.status)
            elif rpc_call == "3":
                item_id = int(input("Enter the item id to add to wishlist: "))
                add_to_wishlist_request = all_pb2.AddToWishListRequest(item_id=item_id,buyer_uuid=buyerr_uuid)
                add_to_wishlist_reply = stub.AddToWishList(add_to_wishlist_request)
                print(add_to_wishlist_reply.status)
            elif rpc_call == "4":
                item_id = int(input("Enter the item id to rate: "))
                rating = int(input("Enter the rating: "))
                rate_item_request = all_pb2.RateItemRequest(item_id=item_id, rating=rating,seller_uuid=buyerr_uuid)
                rate_item_reply = stub.RateItem(rate_item_request)
                print(rate_item_reply.status)
            elif rpc_call == "5":
                break

if __name__ == "__main__":
    run()