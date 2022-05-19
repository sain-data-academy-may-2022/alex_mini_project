# # import my_functions
# # product_list1 = [['sandwich','burrito','burger'], ['cola','coffee','tea']] # potential other options
# # product_list2 = {
# #     'food': {
# #         'hot':{1:'burger',2:'burrito'},
# #         'cold':{1:'sandwich',2:'burrito'}},
# #     'drinks':{
# #         'hot':{1:'coffee',2:'tea'},
# #         'cold':{1:'cola'}}}

# # def time_to_add(a,b,c):
# #     d = a+b+c
# #     return d

# # my_functions.print_list(product_list1)
# # #print(my_functions.list_int_check(product_list1[0],'1'))
# subkey = '1'
# subkey_dex = [[['1','2','3','4'],'name','address','post_code','phone_number'],[['1','2'],'food','drink']]
# print(subkey_dex)
# print(subkey_dex[0])
# print(subkey_dex[0][0])
# if subkey in subkey_dex[0][0] or subkey in subkey_dex[0][1]:
#     if subkey in subkey_dex[0[0]]:
#         subkey = subkey_dex[0[0[subkey_dex[0[0].index(subkey)]]]]
# print(subkey)

import json

# order_list = {'1' : { 
#     'user_data': { 
#         'name' : 'Tim Esting', 'address' : 'holborn', 'post_code' : 'me2', 
#         'phone_number' : '07788221133' , 'order_status' : 'delivered' },
#     'items' : { 
#         'food' : 'None', 'drink' : 'None'}
#     }   }

export = 'order_history.json'


example = 'order_history.json'
my_d = {}

with open(example) as file:
    my_d = json.load(file)

print(my_d)