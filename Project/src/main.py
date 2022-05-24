import my_functions  # <-- i wrote all the functions in here
import order_functions
import product_functions
import couriers_fun
#from getpass import getpass
import json
#from logins import logins
exit = False

product_list = product_functions.pull_produtcts()
courier_dict = couriers_fun.pull_couriers()
order_list = order_functions.pull_orders()

while exit == False:
    my_functions.clear_term()
    print('\nWelcome to the pop-up caf-app')
    print('Menu\n 1 - Product List\n 2 - Food Menu\n 3 - Drinks Menu\n 4 - Order Menu\n 5 - couriers\n 0 - Exit Program')
    option = input('what option would you like? ')

    if option.strip().isdigit():
        option = int(option)

        if option == 0:  # exits the program
            my_functions.clear_term()
            print('Goodbye!')

            # exports my ordr list to .json
            order_functions.push_orders(order_list)
            #updates couriers file with the current version of the dictionary
            couriers_fun.push_couriers(courier_dict)
            # convert my list into appropriate dict format for exporting, then exports them
            product_functions.push_products(product_list[0],product_list[1],product_list[2])

            quit()

        elif option == 1:  # prints the product list
            my_functions.print_list(product_list)
            input("press Enter to return to the menu ")

        elif option == 2:  # enters food menu
            food = False

            while food == False:
                my_functions.clear_term()
                print(
                    'Food\n 1 - Product List\n 2 - Create Product\n 3 - Update Product\n 4 - Delete Product\n 0 - Return To Menu')
                sec_option = input('What option would you like? ')

                if sec_option.strip().isdigit():
                    sec_option = int(sec_option)

                    if sec_option == 0:  # return to main menu
                        food = True
                        continue

                    elif sec_option == 1:
                        my_functions.print_list(product_list[0])
                        input('press Enter to return to the menu')

                    elif sec_option == 2:  # add food item to list
                        list_append = input(
                            'please enter the name of your new Food item ')

                        if product_functions.duplicate_check(product_list,list_append):
                            input('item already on menu, press enter to continue')
                        else:
                            product_list[0].append(list_append)

                    elif sec_option == 3:  # update entry
                        # takes input and checks it is in correct format, returns index
                        list_id = product_functions.option_3(product_list[0])

                        if list_id is None:  # if an invalid entry was given, return to menu
                            continue

                        else:  # enter amendment at previously returned index
                            list_ammend = input('enter you ammendment here please ')
                            if product_functions.duplicate_check(product_list,list_ammend):
                                input('entry already exists. enter to continue : ')
                            else:
                                product_list[0][list_id] = list_ammend

                    elif sec_option == 4:  # removing item from list
                        list_id = product_functions.option_4(product_list[0])

                        if list_id is None:  # if invalid entry was given, return to main menu
                            continue

                        else:
                            # remove item at returned index
                            product_list[0].remove(list_id)

                else:
                    continue

        elif option == 3:  # enters drink menu
            drinks = False

            while drinks == False:
                my_functions.clear_term()
                print(
                    'Drinks\n 1 - Product List\n 2 - Create Product\n 3 - Update Product\n 4 - Delete Product\n 0 - Return To Menu')
                # prints menu options and takes input
                sec_option = input('What option would you like? ')

                if sec_option.strip().isdigit():
                    sec_option = int(sec_option)

                    if sec_option == 0:  # return to main menu
                        drinks = True
                        continue

                    elif sec_option == 1:
                        my_functions.print_list(product_list[1])
                        input('press Enter to return to the menu')

                    elif sec_option == 2:  # add drinks item to list
                        list_append = input(
                            'please enter the name of your new Drink item ')
                        # makes sure you cannot add duplicate items
                        if list_append in product_list[0] or list_append in product_list[1]:
                            input('item already on menu, press enter to continue')
                        else:
                            product_list[1].append(list_append)

                    elif sec_option == 3:  # update entry
                        # takes input and checks it is in correct format, returns index
                        list_id = product_functions.option_3(product_list[1])

                        if list_id is None:  # if an invalid entry was given, return to menu
                            continue

                        else:  # enter amendment at previously returned index
                            list_ammend = input(
                                'enter you ammendment here please ')
                            product_list[1][list_id] = list_ammend

                    elif sec_option == 4:  # removing item from list
                        list_id = product_functions.option_4(product_list[1])

                        if list_id is None:  # if invalid entry was given, return to main menu
                            continue

                        else:
                            # remove item at returned index
                            product_list[1].remove(list_id)

                else:
                    continue

        elif option == 4:  # enters orders menu
            orders = False

            while orders == False:
                my_functions.clear_term()
                print('Welcome to the order menu\nMenu\n 1 - Print active orders\n 2 - Create new order\n 3 - Update Order Status\n 4 - Ammend Order Information\n 5 - Delete Order\n 0 - Return to Menu')
                order_option = input()
                my_functions.clear_term()

                if order_option == '0':  # return to main menu
                    orders = True
                    continue

                elif order_option == '1':  # prints the current list of orders
                    for key in order_list:
                        print(order_list[key])
                    input('press enter to return to menu : ')

                elif order_option == '2':  # create new order
                    order_number = input('please enter the order number : ')

                    if order_number in order_list:  # cannot make new order under previously used order id
                        input('\norder number already exists. press enter to continue\n')
                        continue

                    else:
                        # user fills in order information. returns dictionary
                        order_info = order_functions.create_order(product_list)
                        # adds the order to the order list
                        order_list[order_number] = order_info
                        input('order added to order history.\nenter to continue : ')

                elif order_option == '3':  # update order status
                    order_number = input('please enter your order number : ')
                    if order_number in order_list:
                        new_value = order_functions.order_status()
                        order_list[order_number]['user_data']['order_status'] = new_value
                    else:
                        input('unknown order number.\nEnter to continue : ')

                elif order_option == '4':  # amend order
                    order_number = input('please enter your order number : ')
                    # function runs you through quick multiple choice menu to update the selected order's information
                    amendment = order_functions.order_amend(order_list[order_number], product_list)
                    # returned dictionary, each key is either the same or updated and will overrite the original.
                    order_list[order_number] = amendment

                elif order_option == '5':  # delete order
                    order_number = input('please enter your order number : ')
                    check = input(f'are you sure you would like to delete order {order_number}? \ny/n : ')
                    
                    if check == 'y':
                        order_list.pop(order_number)
                    else:
                        continue

        elif option == 5:
            couriers = False
            while couriers == False:
                my_functions.clear_term()
                #couriers_fun.print_couriers(courier_dict)
                print('Welcome to the couriers menu.')
                courier_entry = input('1 - see all couriers\n2 - add new courier\n3 - remove courier\n0 - return to menu ')

                if courier_entry == '0':
                    couriers = True 
                    continue

                elif courier_entry == '1':
                    couriers_fun.print_couriers(courier_dict)
                    input()

                elif courier_entry == '2':
                    id = input('enter courier id')
                    if id in courier_dict or id == '' or id is None:
                        input('id already exists/invalid')
                        continue
                    else:
                        courier_dict[id] = couriers_fun.hire_courier()

                elif courier_entry == '3':
                    print(courier_dict)
                    to_del = input('Enter id number : ')
                    if to_del in courier_dict:
                        del courier_dict[to_del]
                    else:
                        input('invalid id, enter to continue : ')

    else:
        input("\nincorrect input, please try again.\n")
