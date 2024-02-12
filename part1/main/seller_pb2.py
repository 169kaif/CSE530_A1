# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: seller.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cseller.proto\")\n\x06Seller\x12\x11\n\tseller_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x8a\x01\n\x04Item\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nitem_price\x18\x03 \x01(\x02\x12\x10\n\x08quantity\x18\x04 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x16\n\x0eseller_address\x18\x07 \x01(\t\"(\n\x15RegisterSellerRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\")\n\x16RegisterSellerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"J\n\x0fSellItemRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x04item\x18\x02 \x01(\x0b\x32\x05.Item\x12\x11\n\tseller_id\x18\x03 \x01(\x05\"#\n\x10SellItemResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x81\x01\n\x11UpdateItemRequest\x12\x11\n\tseller_id\x18\x01 \x01(\x05\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\x12\x16\n\x0enew_item_price\x18\x03 \x01(\x02\x12\x14\n\x0cnew_quantity\x18\x04 \x01(\x05\x12\x1a\n\x12new_seller_address\x18\x05 \x01(\t\"%\n\x12UpdateItemResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"O\n\x11\x44\x65leteItemRequest\x12\x11\n\tseller_id\x18\x01 \x01(\x05\x12\x16\n\x0eseller_address\x18\x02 \x01(\t\x12\x0f\n\x07item_id\x18\x03 \x01(\x05\"%\n\x12\x44\x65leteItemResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\".\n\x19\x44isplaySellerItemsRequest\x12\x11\n\tseller_id\x18\x01 \x01(\x05\"2\n\x1a\x44isplaySellerItemsResponse\x12\x14\n\x05items\x18\x01 \x03(\x0b\x32\x05.Item2\xc0\x02\n\rSellerService\x12\x41\n\x0eRegisterSeller\x12\x16.RegisterSellerRequest\x1a\x17.RegisterSellerResponse\x12/\n\x08SellItem\x12\x10.SellItemRequest\x1a\x11.SellItemResponse\x12\x35\n\nUpdateItem\x12\x12.UpdateItemRequest\x1a\x13.UpdateItemResponse\x12\x35\n\nDeleteItem\x12\x12.DeleteItemRequest\x1a\x13.DeleteItemResponse\x12M\n\x12\x44isplaySellerItems\x12\x1a.DisplaySellerItemsRequest\x1a\x1b.DisplaySellerItemsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'seller_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SELLER']._serialized_start=16
  _globals['_SELLER']._serialized_end=57
  _globals['_ITEM']._serialized_start=60
  _globals['_ITEM']._serialized_end=198
  _globals['_REGISTERSELLERREQUEST']._serialized_start=200
  _globals['_REGISTERSELLERREQUEST']._serialized_end=240
  _globals['_REGISTERSELLERRESPONSE']._serialized_start=242
  _globals['_REGISTERSELLERRESPONSE']._serialized_end=283
  _globals['_SELLITEMREQUEST']._serialized_start=285
  _globals['_SELLITEMREQUEST']._serialized_end=359
  _globals['_SELLITEMRESPONSE']._serialized_start=361
  _globals['_SELLITEMRESPONSE']._serialized_end=396
  _globals['_UPDATEITEMREQUEST']._serialized_start=399
  _globals['_UPDATEITEMREQUEST']._serialized_end=528
  _globals['_UPDATEITEMRESPONSE']._serialized_start=530
  _globals['_UPDATEITEMRESPONSE']._serialized_end=567
  _globals['_DELETEITEMREQUEST']._serialized_start=569
  _globals['_DELETEITEMREQUEST']._serialized_end=648
  _globals['_DELETEITEMRESPONSE']._serialized_start=650
  _globals['_DELETEITEMRESPONSE']._serialized_end=687
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_start=689
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_end=735
  _globals['_DISPLAYSELLERITEMSRESPONSE']._serialized_start=737
  _globals['_DISPLAYSELLERITEMSRESPONSE']._serialized_end=787
  _globals['_SELLERSERVICE']._serialized_start=790
  _globals['_SELLERSERVICE']._serialized_end=1110
# @@protoc_insertion_point(module_scope)