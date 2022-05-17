import my_functions # <-- i wrote all the functions in here
from getpass import getpass
from logins import logins
exit = False
order_list = {}
product_list = [['sandwich','burrito','burger'], ['cola','coffee','tea']]# the menu
order_form = { 
    'user_data': { 
        'name' : 'None', 'address' : 'None', 'post_code' : 'None', 
        'phone_number' : 'None' , 'order_status' : 'None' },
    'items' : { 
        'item_1' : 'None', 'item_2' : 'None'}
}

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
                sec_option = input('What option would you like? ')

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
                        if list_append in product_list[0] or list_append in product_list[1]:
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

        elif option == 4:#enters orders menu
            orders = False
            
            while orders == False:
                print('Welcome to the order menu\nMenu\n 1 - Print Current Order\n 2 - Create new order\n 3 - Update Order Status\n 4 - Ammend Order Information\n 5 - Delete Order\n 0 - Return to Menu')
                order_option = input()

                if order_option == '0': # return to main menu
                    orders = True
                    continue
                
                elif order_option == '1': #prints the current list of orders
                    print(order_list)
                
                elif order_option == '2': #create new order
                    order_number = input('please enter the order number : ')
                    
                    if order_list.__contains__(order_number): # checks if order number already exists
                        print('\norder number already exists.\n')
                        continue
                    
                    for key in order_form['user_data'].keys(): #loops through all of the keys in the info part of the dictionary
                        
                        if key == 'order_status': #sets status to pending for uniformality 
                            order_form['user_data'][key] = 'pending' 
                            continue
                        
                        order_form['user_data'][key] = input(f'please enter User {key} : ') #user can enter all info manually for dictionary values
                    
                    for index in product_list:
                        my_functions.print_list(product_list[index]) #prints the product lists
                    
                    for key in order_form['items'].keys(): #loops through all keys in the items part of the dictionary
                        order_form['items'][key] = input(f'please enter customers {key} item')

                    order_list[order_number] = order_form # adds the order to the order list
                    print(order_list) #to be commented out

    else:
        input("\nincorrect input, please try again.\n")