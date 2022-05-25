import os
import product_functions
import order_functions
import couriers_fun

# the order menu. options to add, update and delete can be accessed here
def orders_menu():
    order_list = order_functions.pull_orders()
    #product_list = product_functions.pull_produtcts()
    orders = False

    while orders == False:
        clear_term()
        print('Welcome to the order menu\nMenu\n 1 - Print active orders\n 2 - Create new order\n 3 - Update Order Status\n 4 - Ammend Order Information\n 5 - Delete Order\n 0 - Return to Menu')
        order_option = input()
        clear_term()

        if order_option == '0':  # return to main menu
            orders = True
            continue

        elif order_option == '1':  # prints the current dictionary of orders
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
                order_info = order_functions.create_order()
                # adds the order to the order list
                order_list[order_number] = order_info
                order_functions.push_orders(order_list)
                input('order added to order history.\nenter to continue : ')

        elif order_option == '3':  # update order status
            order_number = input('please enter your order number : ')
            if order_number in order_list:
                new_value = order_functions.order_status()
                order_list[order_number]['user_data']['order_status'] = new_value
                order_functions.push_orders(order_list)
            else:
                input('unknown order number.\nEnter to continue : ')

        elif order_option == '4':  # amend order
            order_number = input('please enter your order number : ')
            # function runs you through quick multiple choice menu to update the selected order's information
            amendment = order_functions.order_amend(order_list[order_number])
            # returned dictionary, each key is either the same or updated and will overrite the original.
            order_list[order_number] = amendment
            order_functions.push_orders(order_list)

        elif order_option == '5':  # delete order
            order_number = input('please enter your order number : ')
            check = input(f'are you sure you would like to delete order {order_number}? \ny/n : ')
            
            if check == 'y':
                order_list.pop(order_number)
                order_functions.push_orders(order_list)
            else:
                continue

def print_list(my_list):  # prints a list with indexes
    #clear_term()
    index = 0
    for x in my_list:
        print(index, x)
        index += 1

def clear_term():  # clears the terminal
    os.system('clear')

#the interactive menu for each of the different product menus. options to add, update and delete can be accessed here
def product_menu(product_type):
    if product_type == 'food':
        version = 0
    elif product_type == 'drinks':
        version = 1
    elif product_type == 'snacks':
        version = 2
    else:
        return False
    menu = False
    product_list = product_functions.pull_produtcts()
    while menu == False:
        clear_term()
        print(
            'Food\n 1 - Product List\n 2 - Create Product\n 3 - Update Product\n 4 - Delete Product\n 0 - Return To Menu')
        sec_option = input('What option would you like? ')

        if sec_option.strip().isdigit():
            sec_option = int(sec_option)

            if sec_option == 0:  # return to main menu
                menu = True
                product_functions.push_products(product_list[0],product_list[1],product_list[2])
                continue

            elif sec_option == 1:
                print_list(product_list[version])
                input('press Enter to return to the menu')

            elif sec_option == 2:  # add item to list
                list_append = input(
                    'please enter the name of your new item ')

                if product_functions.duplicate_check(product_list,list_append):
                    input('item already on menu, press enter to continue')
                else:
                    product_list[version].append(list_append)

            elif sec_option == 3:  # update entry
                # takes input and checks it is in correct format, returns index
                list_id = product_functions.option_3(product_list[version])

                if list_id is None:  # if an invalid entry was given, return to menu
                    continue

                else:  # enter amendment at previously returned index
                    list_ammend = input('enter you ammendment here please ')
                    if product_functions.duplicate_check(product_list,list_ammend):
                        input('entry already exists. enter to continue : ')
                    else:
                        product_list[version][list_id] = list_ammend

            elif sec_option == 4:  # removing item from list
                list_id = product_functions.option_4(product_list[version])

                if list_id is None:  # if invalid entry was given, return to main menu
                    continue

                else:
                    # remove item at returned index
                    product_list[version].remove(list_id)

        else:
            continue

#the interactive menu for the couriers. options to add, delete and print couriers
def courier_menu():
    courier_dict = couriers_fun.pull_couriers()    
    couriers = False
    while couriers == False:
        clear_term()
        print('Welcome to the couriers menu.')
        courier_entry = input('1 - see all couriers\n2 - add new courier\n3 - update courier\n4 - remove courier\n0 - return to menu : ')
        
        #exit
        if courier_entry == '0':
            couriers = True 
            continue
        
        #print couriers
        elif courier_entry == '1':
            couriers_fun.print_couriers(courier_dict)
            input()

        #add courier
        elif courier_entry == '2':
            id = input('enter courier id')
            if id in courier_dict or id == '' or id is None:
                input('id already exists/invalid')
                continue
            else:
                courier_dict[id] = couriers_fun.hire_courier()
                couriers_fun.push_couriers(courier_dict)

        #update courier
        elif courier_entry == '3':
            print(courier_dict)
            to_edit = input('Enter id number : ')
            if to_edit in courier_dict:
                courier_dict[to_edit] = couriers_fun.update_courier(courier_dict[to_edit])
                couriers_fun.push_couriers(courier_dict)
            else:
                input('invalid id, enter to continue : ')

        #delete courier
        elif courier_entry == '4':
            print(courier_dict)
            to_del = input('Enter id number : ')
            if to_del in courier_dict:
                del courier_dict[to_del]
                couriers_fun.push_couriers(courier_dict)
            else:
                input('invalid id, enter to continue : ')
