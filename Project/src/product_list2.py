import my_functions # <-- i wrote all the functions in here
exit = False
product_list = [['sandwich','burrito','burger'], ['cola','coffee','tea']]# the menu

while exit == False:
    my_functions.clear_term()
    print('\nWelcome to the pop-up caf-app')
    print('Menu\n 1 - Product List\n 2 - Food Menu\n 3 - Drinks Menu\n 0 - Exit Program')
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

    else:
        input("\nincorrect input, please try again.\n")