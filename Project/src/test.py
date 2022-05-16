import my_functions
product_list1 = [['sandwich','burrito','burger'], ['cola','coffee','tea']] # potential other options
product_list2 = {
    'food': {
        'hot':{1:'burger',2:'burrito'},
        'cold':{1:'sandwich',2:'burrito'}},
    'drinks':{
        'hot':{1:'coffee',2:'tea'},
        'cold':{1:'cola'}}}


my_functions.print_list(product_list1)
#print(my_functions.list_int_check(product_list1[0],'1'))
