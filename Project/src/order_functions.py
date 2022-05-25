#imports
import my_functions
import traceback
#import product_functions
import json

def create_order(product_list):
    # order form is used as a template to itterate through when adding the info
    order_form = {
        'user_data': {
            'name': 'None', 'address': 'None', 'post_code': 'None',
            'phone_number': 'None','courier' : "None", 'order_status': 'None'},
        'items': {
            'food': 'None', 'drink': 'None'}
    }
    # loops through all of the keys in the info part of the dictionary
    for key in order_form['user_data'].keys():

        if key == 'order_status':  # sets status to pending for uniformality
            order_form['user_data'][key] = 'pending'
            continue

        # user can enter all info manually for dictionary values
        order_form['user_data'][key] = input(f'please enter User {key} : ')

    for index in product_list:
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


def order_status():
    new_value = ''
    print('d = delivered\nt = in-transit\np = pending\nc = cooking')
    update = input('please enter the new status : ')
    while True:
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


def order_amend(order, product_list):
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
                order['user_data'][key] = change

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
                        order['items'][key] = change
                        index += 1
                        break
                    else:
                        input('item not on menu, enter to try again : ')
                        continue

    return order  # returns the dictionary passed in, but updated with new info

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

def push_orders(order_list):
    file_name = 'order_history.json'
    try:
        with open(file_name,'w') as file:
            new = json.dumps(order_list, indent='   ')
            file.write(new)
    except Exception as e:
        print('unable to update / create',file_name)
        print(traceback.print_exc(),e)