#imports
import my_functions
import product_functions 
import traceback
import couriers_fun
import random
import json

# returns a dictonary with the format of the provided 'order form' dictionary
def create_order():
    product_list = product_functions.pull_produtcts()
    couriers = couriers_fun.pull_couriers()
    # order form is used as a template to itterate through when adding the info
    order_form = {
        'user_data': {
            'name': 'None', 'address': 'None', 'post_code': 'None',
            'phone_number': 'None','courier' : "None", 'order_status': 'None'},
        'items': {
            'food': 'None', 'drink': 'None', 'snack':'None'}
    }
    # loops through all of the keys in the info part of the dictionary
    for key in order_form['user_data'].keys():

        if key == 'order_status':  # sets status to pending for uniformality
            order_form['user_data'][key] = 'pending'
            continue
        if key == 'courier':
            print(couriers.keys())
            my_random = random.choice(list(couriers.keys()))
            order_form['user_data'][key] = my_random
            couriers[my_random]['open_orders'] +=1
            couriers_fun.push_couriers(couriers)
            continue

        # user can enter all info manually for dictionary values
        order_form['user_data'][key] = input(f'please enter User {key} : ')

    
    my_functions.print_list(product_list)  # prints the product lists

    index = 0
    # loops through all keys in the items part of the dictionary
    for key in order_form['items'].keys():
        correct = False

        while correct == False:
            meal = input(f'please enter customers {key} item : ')
            if meal in product_list[index]:
                order_form['items'][key] = meal
                index += 1
                correct = True
            else:
                input('please enter a valid input. enter to continue : ')

    return order_form

def order_menu_amend():
    order_number = input('please enter your order number : ')
    order_list = pull_orders()
    if order_number in order_list.keys():
        # function runs you through quick multiple choice menu to update the selected order's information
        amendment = order_amend(order_list[order_number])
        # returned dictionary, each key is either the same or updated and will overrite the original.
        order_list[order_number] = amendment
        push_orders(order_list)
        return True
    else:
        input('order not in list\nenter to continue : ')
        return False

def order_menu_create():
    order_list = pull_orders()
    order_number = input('please enter the order number : ')
    if order_number in order_list:  # cannot make new order under previously used order id
        input('\norder number already exists. press enter to continue\n')
        return False
    elif order_number == '' or  not order_number.strip().isdigit():
        input('\nplease enter a valid input\n enter to continue : ')
        return False
    else:
        # user fills in order information. returns dictionary
        order_info = create_order()
        # adds the order to the order list
        order_list[order_number] = order_info
        push_orders(order_list)
        input('order added to order history.\nenter to continue : ')
        return True

def order_menu_delete():
    order_number = input('please enter your order number : ')
    check = input(f'are you sure you would like to delete order {order_number}? \ny/n : ')
    order_list = pull_orders()

    if check == 'y' or check == 'Y':
        if order_number in order_list.keys():
            order_list.pop(order_number)
            push_orders(order_list)
            return True
        
        else:
            input('order not found\nenter to continue : ')
            return False

    else:
        return False

def order_menu_update():
    order_number = input('please enter your order number : ')
    order_list = pull_orders()        
    # if entry in dict, call update function, assign value and then update source file. else return to menu
    if order_number in order_list.keys():
        new_value = order_status()
        order_list[order_number]['user_data']['order_status'] = new_value
        push_orders(order_list)
        return True
    
    else:
        input('unknown order number.\nEnter to continue : ')
        return False

def print_orders():
    order_list = pull_orders()
    print('-----------------------------------------')
    for key in order_list:
        
        print('\nname         : ', order_list[key]['user_data']['name'],'\naddress      : ', order_list[key]['user_data']['address'],
              '\npost code    : ', order_list[key]['user_data']['post_code'],'\nphone number : ', order_list[key]['user_data']['phone_number'],
              '\ncourier      : ', order_list[key]['user_data']['courier'],'\nstatus       : ', order_list[key]['user_data']['order_status'])
        print('\nfood         : ', order_list[key]['items']['food'],'\ndrink        : ',order_list[key]['items']['drink'], 
              '\nsnack        : ', order_list[key]['items']['snack'])
        print('-----------------------------------------')

# used for updating the order status key in an order dictonary, returns the new value
def order_status():
    new_value = ''
    while True:
        print('d = delivered\nt = in-transit\np = pending\nc = cooking')
        update = input('please enter the new status : ')
        if update == 'c' or update == 'cooking':  # if characters match, update to appropriate order status
            new_value = 'cooking'
            return new_value

        elif update == 't' or update == 'in-transit':
            new_value = 'in-transit'
            return new_value

        elif update == 'd' or update == 'delivered':
            new_value = 'delivered'
            return new_value

        elif update == 'p' or update == 'pending':
            new_value = 'pending'
            return new_value

        else:
            print('invalid entry')

# creates copy of passed order, loops through keys and returns copy so original can be updated
def order_amend(order):
    copy = order
    product_list = product_functions.pull_produtcts
    data = input('ammending user data y/n? : ')
    if data == 'y' or data == 'Y':  # accepts both capitals and text
        # runs through each item in the dictionary
        for key, value in order['user_data'].items():
            if key == 'order_status':  # skips the order status as that needs to be changed separately
                continue

            print(key, value, 'enter ammendment or enter to skip : ')
            change = input()

            if change == '':  # if they just use enter, they do not update the entry
                continue
            else:
                # updates entry in passed dictionary
                copy['user_data'][key] = change

    items = input('ammending food and drink y/n : ')
    if items == 'y' or items == 'Y':
        index = 0
        for key, value in order['items'].items():
            while True:  # loop used to make sure they can only enter items on the menu
                print(product_list[index])
                print(key, value, 'enter ammendment or enter to skip : ')
                change = input()
                if change == '':
                    index += 1
                    continue
                else:
                    # if item is in the menu then great!, else try again
                    if change in product_list[index]:
                        copy['items'][key] = change
                        index += 1
                        break
                    else:
                        input('item not on menu, enter to try again : ')
                        continue

    return copy  # returns the dictionary passed in, but updated with new info

#imports from file
def pull_orders():
    file_name = 'order_history.json'
    try:
        with open(file_name) as file:
            orders = json.load(file)
    except Exception as e:
        print(file_name,'not found, new file will be created',e)
        orders = {}
        print(traceback.print_exc())
    return orders

#exports to file
def push_orders(order_list):
    file_name = 'order_history.json'
    try:
        with open(file_name,'w') as file:
            new = json.dumps(order_list, indent='   ')
            file.write(new)
    except Exception as e:
        print('unable to update / create',file_name)
        print(traceback.print_exc(),e)