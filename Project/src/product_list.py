import my_functions # <-- i wrote all the functions in here
from getpass import getpass
import json
#from logins import logins
exit = False
order_list = {}
product_list = [['sandwich','burrito','burger'], ['cola','coffee','tea','lemonade'],["banana","apple","crisps"]]# the menu

list_name = 'order_history.json'
try:
    with open(list_name) as file:
        order_list = json.load(file)
except:
    print(list_name,'not found, new file will be created')

# try:
#     with open('products.json') as file:
#         prod_dict = json.load(file)
        
# except:
#     prod_dict = {
#         'food':[],'drinks':[],'snacks':[]
#     }
#     print('products.json not found')

# for key,value in prod_dict.items():
#     product_list.append(key[value]) 
#     print(product_list)
    

while exit == False:
    my_functions.clear_term()
    print('\nWelcome to the pop-up caf-app')
    print('Menu\n 1 - Product List\n 2 - Food Menu\n 3 - Drinks Menu\n 4 - Order Menu\n 0 - Exit Program')
    option = input('what option would you like? ')
    
    if option.strip().isdigit():
        option = int(option)
        
        if option == 0: #exits the program
            my_functions.clear_term()            
            print('Goodbye!')
            
            #exports my ordr list to .json
            with open(list_name,'w') as file:
                new = json.dumps(order_list,indent='    ')
                file.write(new)
            
            #convert my list into appropriate dict format for exporting
            prod_dict = {
                'food' : product_list[0], 'drinks' : product_list[1], 'snacks' : product_list[2]
            }
            with open('products.json','w') as file:
                new = json.dumps(prod_dict,indent= '    ')
                file.write(new)
            
            quit()
            
        elif option == 1: #prints the product list
            my_functions.print_list(product_list)
            input("press Enter to return to the menu ")
        
        elif option == 2: #enters food menu
            food = False
           
            while food == False:
                my_functions.clear_term()
                print('Food\n 1 - Product List\n 2 - Create Product\n 3 - Update Product\n 4 - Delete Product\n 0 - Return To Menu')
                sec_option = input('What option would you like? ')

                if sec_option.strip().isdigit():
                    sec_option = int(sec_option)
                    
                    if sec_option == 0: #return to main menu
                        food = True
                        continue
                    
                    elif sec_option == 1:
                        my_functions.print_list(product_list[0])
                        input('press Enter to return to the menu')
                    
                    elif sec_option == 2:#add food item to list
                        list_append = input('please enter the name of your new Food item ')
                        
                        if list_append in product_list[0] or list_append in product_list[1]:
                            input('item already on menu, press enter to continue')
                        else:    
                            product_list[0].append(list_append)
                    
                    elif sec_option == 3:#update entry
                        list_id = my_functions.option_3(product_list[0])#takes input and checks it is in correct format, returns index
                        
                        if list_id is None: #if an invalid entry was given, return to menu
                            continue
                        
                        else: #enter amendment at previously returned index
                            list_ammend = input('enter you ammendment here please ')
                            product_list[0,list_id] = list_ammend

                    elif sec_option == 4: #removing item from list
                        list_id = my_functions.option_4(product_list[0])
                        
                        if list_id is None: #if invalid entry was given, return to main menu
                            continue
                        
                        else:
                            product_list[0].remove(list_id) #remove item at returned index
                
                else:            
                    continue   
                
        elif option == 3:#enters drink menu
            drinks = False
            
            while drinks == False:
                my_functions.clear_term()
                print('Drinks\n 1 - Product List\n 2 - Create Product\n 3 - Update Product\n 4 - Delete Product\n 0 - Return To Menu')
                sec_option = input('What option would you like? ') #prints menu options and takes input

                if sec_option.strip().isdigit():
                    sec_option = int(sec_option)
                    
                    if sec_option == 0: #return to main menu
                        drinks = True
                        continue
                    
                    elif sec_option == 1:
                        my_functions.print_list(product_list[1])
                        input('press Enter to return to the menu')
                    
                    elif sec_option == 2:#add drinks item to list
                        list_append = input('please enter the name of your new Drink item ')
                        if list_append in product_list[0] or list_append in product_list[1]: #makes sure you cannot add duplicate items
                            input('item already on menu, press enter to continue')
                        else:
                            product_list[1].append(list_append)

                    elif sec_option == 3:#update entry
                        list_id = my_functions.option_3(product_list[1])#takes input and checks it is in correct format, returns index
                        
                        if list_id is None: #if an invalid entry was given, return to menu
                            continue
                        
                        else: #enter amendment at previously returned index
                            list_ammend = input('enter you ammendment here please ')
                            product_list[1,list_id] = list_ammend

                    elif sec_option == 4: #removing item from list
                        list_id = my_functions.option_4(product_list[1])
                        
                        if list_id is None: #if invalid entry was given, return to main menu
                            continue
                        
                        else:
                            product_list[1].remove(list_id) #remove item at returned index
                
                else:            
                    continue   

        elif option == 4: #enters orders menu
            orders = False
            
            while orders == False:
                my_functions.clear_term()
                print('Welcome to the order menu\nMenu\n 1 - Print active orders\n 2 - Create new order\n 3 - Update Order Status\n 4 - Ammend Order Information\n 5 - Delete Order\n 0 - Return to Menu')
                order_option = input()
                my_functions.clear_term()

                if order_option == '0': # return to main menu
                    orders = True
                    continue
                
                elif order_option == '1': #prints the current list of orders
                    for key in order_list:
                        print(order_list[key])
                    input('press enter to return to menu : ')
                
                elif order_option == '2': #create new order
                    order_number = input('please enter the order number : ')
                    
                    if order_number in order_list: #cannot make new order under previously used order id
                        input('\norder number already exists. press enter to continue\n')
                        continue
                    
                    else:
                        order_info = my_functions.create_order(product_list) #user fills in order information. returns dictionary
                        order_list[order_number] = order_info # adds the order to the order list
                        input('order added to order history.\nenter to continue : ') 
                
                elif order_option == '3': #update order status
                    order_number = input('please enter your order number : ') 
                    if order_number in order_list:
                        new_value = my_functions.order_status()
                        order_list[order_number]['user_data']['order_status'] = new_value
                    else:
                        input('unknown order number.\nEnter to continue : ')


                elif order_option =='4': #amend order
                    order_number = input('please enter your order number : ') 
                    amendment = my_functions.order_amend(order_list[order_number],product_list) #function runs you through quick multiple choice menu to update the selected order's information
                    order_list[order_number] = amendment #returned dictionary, each key is either the same or updated and will overrite the original.
                    
                elif order_option == '5' : #delete order
                    order_number = input('please enter your order number : ')
                    check = input(f'are you sure you would like to delete order {order_number}? \ny/n : ')
                    if check == 'y':
                        order_list.pop(order_number)
                    else:
                        continue

    else:
        input("\nincorrect input, please try again.\n")