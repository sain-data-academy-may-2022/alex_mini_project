import my_functions # <-- i wrote all the functions in here
exit = False
product_list = ["sandwich", "cola", "burrito", "coffee",'burger','tea']# the menu

while exit == False:
    my_functions.clear_term()
    print('\nWelcome to the pop-up caf-app')
    print('Menu\n 1 - Product List\n 2 - Create Product\n 3 - Update Product\n 4 - Delete Product\n 0 - Exit Program')
    option = input('what option would you like? ')
    
    if option.strip().isdigit():
        option = int(option)
        
        if option == 0: #exits the program
            my_functions.clear_term()            
            print('Goodbye!')
            quit()
            
        elif option == 1: #prints the product list
            my_functions.print_list(product_list)
            input("press any Enter to return to the menu ")

        elif option == 2: #add an item to the product list
            list_append = input("please enter the name of your product ")
            product_list.append(list_append)

        elif option == 3: #update entry
            my_functions.print_list(product_list) #prints product list, along with index ids
            entry = input("please enter the id or name of the item you wish to update ")
            list_id = my_functions.list_int_check(product_list,entry) #function allows both text and numbers to be accepted, returns appropriate index
            
            if list_id is None: #if an invalid entry was given, return to main menu
                continue

            else: #enter amendment at previously returned index
                list_ammend = input("enter your ammendment here please ")
                product_list[list_id] = list_ammend

        elif option == 4: #removing item from list
            my_functions.print_list(product_list) #prints product list along with index ids
            entry = input("please enter the id or name of the item you wish to delete ")
            list_id = my_functions.list_str_check(product_list, entry) #function allows both text and numbers to be accepted, returns appropriate index (different text output)
            
            if list_id is None: #if invalid entry was given, return to main menu
                continue
            
            else:
                product_list.remove(list_id) #remove item at returned index

    else:
        input("\nincorrect input, please try again.\n")