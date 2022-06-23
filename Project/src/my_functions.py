import os
import product_functions
import order_functions
import couriers_fun


def orders_menu_select(order_option):
    if order_option == '0':  # return to main menu
        return False

    elif order_option == '1':  # prints the current dictionary of orders
        order_functions.print_orders()
        input()
        return True

    elif order_option == '2':  # create new order
        order_functions.create_order()
        return True

    elif order_option == '3':  # update order status
        order_functions.order_menu_update()
        return True

    elif order_option == '4':  # amend order
        order_functions.order_menu_amend()
        return True

    elif order_option == '5':  # delete order
        order_functions.order_menu_delete()
        return True

# the order menu. options to add, update and delete can be accessed here
def orders_menu():
    #product_list = product_functions.pull_produtcts()
    orders = True

    while orders == True:
        clear_term()
        print('Welcome to the order menu\nMenu\n 1 - Print active orders\n 2 - Create new order\n 3 - Update Order Status\n 4 - Ammend Order Information\n 5 - Delete Order\n 0 - Return to Menu')
        order_option = input()
        clear_term()
        orders = orders_menu_select(order_option)
    
def print_list(my_list):  # prints a list with indexes
    #clear_term()
    index = 0
    for x in my_list:
        print(index, x)
        index += 1

def clear_term():  # clears the terminal
    os.system('clear')

#the interactive menu for each of the different product menus. options to add, update and delete can be accessed here
def product_menu(product_type,index):
    menu = True
    product_list = product_functions.pull_product_names()
    while menu == True:
        clear_term()
        print(
            'Food\n 1 - Product List\n 2 - Create Product\n 3 - Update Product\n 4 - Delete Product\n 0 - Return To Menu')
        sec_option = input('What option would you like? ')
        menu = product_menu_input(sec_option,product_type,product_list,index)

def product_menu_input(sec_option,version,product_list,index):
    clear_term()
    if sec_option.strip().isdigit():
        sec_option = int(sec_option)

        if sec_option == 0:  # return to main menu
            return False

        elif sec_option == 1:
            product_functions.print_products(version)
            input('press Enter to return to the menu : ')
            return True

        elif sec_option == 2:  # add item to list
            list_append = input(
                'please enter the name of your new item ')

            if product_functions.duplicate_check(product_list,list_append):
                input('item already on menu, press enter to continue : ')

            else:
                prod = product_functions.create_product(list_append)
                product_functions.push_product(version,prod)

        elif sec_option == 3:  # update entry
            # takes input and checks it is in correct format, returns index
            list_id = product_functions.option_3(product_list[index],version)
            
            if list_id is None:  # if an invalid entry was given, return to menu
                return True

            else:  # enter amendment at previously returned index
                #list_id -=1
                product = product_functions.pull_product_by_name(version,list_id)
                fresh_prod = product_functions.update_product(version,product)
                
                if product != fresh_prod:
                    product_functions.push_updated_product(version,fresh_prod)

        elif sec_option == 4:  # removing item from availability
            list_id = product_functions.option_4(product_list[index],version)

            if list_id is None:  # if invalid entry was given, return to main menu
                return True

            else:
                # remove item at returned index
                print(version)
                print(list_id)
                input()
                product = product_functions.pull_product_by_name(version,list_id)
                product_functions.deactivate_product(version,product)
                
    else:
        return True
        
#the interactive menu for the couriers. options to add, delete and print couriers
def courier_menu():
    couriers = True
    
    while couriers == True:
        clear_term()
        print('Welcome to the couriers menu.')
        courier_entry = input('1 - see all couriers\n2 - add new courier\n3 - update courier\n4 - remove courier (inactive)\n0 - return to menu : ')
        couriers = courier_menu_option(courier_entry)

def courier_menu_option(courier_entry):
    #exit
    if courier_entry == '0':
        return False 
    
    #print couriers
    elif courier_entry == '1':
        clear_term()
        couriers_fun.print_couriers()
        input()
        return True

    #add courier
    elif courier_entry == '2':
        new_hire = (couriers_fun.hire_courier())
        couriers_fun.add_a_courier(new_hire)
        return True

    #update courier
    elif courier_entry == '3':
        clear_term()
        couriers_fun.print_couriers()
        
        courier_dict = couriers_fun.get_couriers_dict()
        try:
            id = int(input('Enter id number : '))
        except:
            input('enter a number please')
            return True
            
        for x in courier_dict:
            if id == x['id']:
                index = courier_dict.index(x)
                changes = couriers_fun.update_courier(courier_dict[index])
                couriers_fun.push_a_courier(changes)
                return True
        else:
            input('invalid id, enter to continue : ')
            return True

    #delete courier
    # elif courier_entry == '4':
    #     clear_term()
    #     couriers_fun.print_couriers()

    #     to_del = input('Enter id number : ')
    #     if to_del in courier_dict:
    #         del courier_dict[to_del]
    #         couriers_fun.push_couriers(courier_dict)
    #         return True

    #     else:
    #         input('invalid id, enter to continue : ')
    #         return True
