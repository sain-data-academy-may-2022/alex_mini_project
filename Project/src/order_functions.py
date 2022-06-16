#imports
import my_functions as mf
import product_functions as pf 
import traceback
import couriers_fun as cf
import random
import json
#import pymysql
from db import db
from prettytable import from_db_cursor

def print_orders():
    connection = db.establish()
    cursor = connection.cursor()
    
    cursor.execute("select * from orders")
    
    mytable = from_db_cursor(cursor)
    print(mytable)
    cursor.close()
    db.shut_down(connection)

def print_an_order(id):

    sql = 'select * from orders where order_number = %s'
    val = (id)
    
    connection = db.establish()
    cursor = connection.cursor()
    cursor.execute(sql,val)
    
    my_table = from_db_cursor(cursor)
    print(my_table)

    cursor.close()
    db.shut_down(connection)

def get_specific_order(number):
    connect = db.establish()
    sql = f'select * from orders where order_number = {number}'
    
    cursor = connect.cursor()
    cursor.execute(sql)
    desc = cursor.description
    
    col_names = [col[0] for col in desc]
    orders = dict(zip(col_names, cursor.fetchone()))
    
    return orders
    
def update_order_sql(order):
    #print(order)
    #input()
    num = order['order_number']
    sql = "UPDATE orders SET first_name = %s,last_name = %s,address = %s,phone = %s,courier = %s,status = %s,food = %s,drink = %s,snack = %s WHERE order_number = %s "
    val = (order['first_name'],
            order['last_name'],
            order['address'],
            order['phone'],
            order['courier'],
            order['status'],
            order['food'],
            order['drink'],
            order['snack'],
            num)
    db.connect_execute_close_with_val(sql,val)


def download_orders():
    connect = db.establish()
    sql = 'select * from orders'
    cursor = connect.cursor()
    cursor.execute(sql)
    desc = cursor.description
    col_names = [col[0] for col in desc]
    orders = [dict(zip(col_names, row)) 
        for row in cursor.fetchall()]
    db.shut_down(connect)
    return orders

def upload_all_orders(orders: list):
    connect = db.establish()
    sql = "insert into orders (first_name,last_name,address,phone,courier,status,food,drink,snack) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor = connect.cursor()
    for x in orders:
        val = (x['first_name'],
                x['last_name'],
                x['address'],
                x['phone_number'],
                x['courier'],
                x['status'],
                x['food'],
                x['drink'],
                x['snack'])
        cursor.execute(sql,val)

    connect.commit()
    cursor.close()
    db.shut_down(connect)

def upload_order(order):
    connect = db.establish()
    sql = "insert into orders (first_name,last_name,address,phone,courier,status,food,drink,snack) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor = connect.cursor()
    val = (order['first_name'],
            order['last_name'],
            order['address'],
            order['phone_number'],
            order['courier'],
            order['status'],
            order['food'],
            order['drink'],
            order['snack'])
    cursor.execute(sql,val)

    connect.commit()
    cursor.close()
    db.shut_down(connect)

def get_order_nums():
    connect = db.establish()
    sql = 'select order_number from orders order by order_number asc'
    
    cursor = connect.cursor()
    cursor.execute(sql)
    #gets list of rows (in this case only one row)
    nums = [i[0] for i in cursor.fetchall()]
    return nums
    
# returns a dictonary with the format of the provided 'order form' dictionary
def create_order():
    product_list = pf.pull_product_names()
    #couriers = cf.new_pull_couriers()
    # order form is used as a template to itterate through when adding the info
    order_form = {
        'first_name': 'None','last_name': 'None', 'address': 'None', 
        'phone_number': 'None','courier' : "None", 'status': 'None',
        'food': 'None', 'drink': 'None', 'snack':'None'}
    
    # loops through all of the keys in the info part of the dictionary
    for key in order_form.keys():

        if key == 'status':  # sets status to pending for uniformality
            order_form[key] = 'pending'
            continue
        
        if key == 'courier':
            order_form[key] = cf.random_courier()
            # print(couriers.keys())
            # my_random = random.choice(list(couriers.keys()))
            # order_form[key] = my_random
            # couriers[my_random]['open_orders'] +=1
            # cf.push_couriers(couriers)
            continue
        
        if key =='food' or key == 'drink' or key == 'snack':
            correct = False
            
            if key == 'food':
                index = 0
            if key == 'drink':
                index = 1
            if key == 'snack':
                index = 2
            
            # prints the product lists
            

            while correct == False:
                mf.clear_term()
                mf.print_list(product_list[index])
                meal = input(f'please enter customers {key} item : ')
                if meal in product_list[index]:
                    id = product_list[index].index(meal)+1
                    order_form[key] = id
                    correct = True
                    
                else:
                    input('please enter a valid input. enter to continue : ')
            continue

        # user can enter all info manually for dictionary values
        order_form[key] = input(f'please enter User {key} : ')
    upload_order(order_form)

def order_menu_amend():
    order_number = int(input('please enter your order number : '))
    order_list = get_order_nums()
    if order_number in order_list:
        order = get_specific_order(order_number)
        # function runs you through quick multiple choice menu to update the selected order's information
        amendment = order_amend(order)
        # returned dictionary, each key is either the same or updated and will overrite the original.
        if order != None:
            order = amendment
            update_order_sql(order)
            return True
        
    else:
        input('order not in list\nenter to continue : ')
        return False

def order_delete_from_db(order_number):
    sql = "DELETE FROM orders WHERE order_number = %s"
    val = (order_number)
    try:
        db.connect_execute_close_with_val(sql,val)
        return True
    except Exception as e:
        input(f'error occured : {e}, enter to continue')


def order_menu_delete():
    order_number = int(input('please enter your order number : '))
    print_an_order(order_number)
    check = input(f'are you sure you would like to delete order {order_number}? \ny/n : ')
    order_list = get_order_nums()

    if check == 'y' or check == 'Y':
        if order_number in order_list:
            order_delete_from_db(order_number)
            return True
        
        else:
            input('order not found\nenter to continue : ')
            return False

    else:
        return False

def order_menu_update():
    order_number = int(input('please enter your order number : '))
    order_list = get_order_nums()        
    # if entry in dict, call update function, assign value and then update source file. else return to menu
    if order_number in order_list:
        new_value = order_status()
        order = get_specific_order(order_number)
        order['status'] = new_value
        update_order_sql(order)
        return True
    
    else:
        input('unknown order number.\nEnter to continue : ')
        return False

# used for updating the order status key in an order dictonary, returns the new value
def order_status():
    new_value = ''
    running = True
    while running:
        new_value,running = order_status_while(new_value,running)
        
def order_status_while(new_value: str,running: bool):
    
    print('d = delivered\nt = in-transit\np = pending\nc = cooking')
    update = input('please enter the new status : ')
    if update == 'c' or update == 'cooking':  # if characters match, update to appropriate order status
        new_value = 'cooking'
        running = False
        return new_value,running

    elif update == 't' or update == 'in-transit':
        new_value = 'in-transit'
        running = False
        return new_value,running

    elif update == 'd' or update == 'delivered':
        new_value = 'delivered'
        running = False
        return new_value,running

    elif update == 'p' or update == 'pending':
        new_value = 'pending'
        running = False
        return new_value,running

    else:
        print('invalid entry')
        return new_value, running

# creates copy of passed order, loops through keys and returns copy so original can be updated
def order_amend(order):
    copy = order
    product_list = pf.pull_product_names()
    print_an_order(order['order_number'])
    data = input('ammending order data y/n? : ')
    if data == 'y' or data == 'Y':  # accepts both capitals and text
        # runs through each item in the dictionary
        for key, value in order.items():
            mf.clear_term()
            if key == 'status' or key =='order_number':  # skips the order status as that needs to be changed separately
                continue
            
            elif key in ['food','drink','snack']:
                correct = True
                if key == 'food':
                    index = 0
                elif key == 'drink':
                    index = 1
                elif key == 'snack':
                    index = 2
                
                while correct:  # loop used to make sure they can only enter items on the menu
                    mf.clear_term()
                    print(product_list[index])
                    print(key,' : ', value, 'enter ammendment or enter to skip : ')
                    change = input()
                    if change == '':
                        correct  = False
                        break
                    else:
                        # if item is in the menu then great!, else try again
                        if change in product_list[index]:
                            change = int(product_list[index].index(change)+1)
                            print(change)
                            input()
                            correct = False
                            break
                        else:
                            input('item not on menu, enter to try again : ')
                            continue
            else:
                print(key,' : ', value, 'enter ammendment or enter to skip : ')
                change = input()

            if change == '':  # if they just use enter, they do not update the entry
                continue
            else:
                # updates entry in passed dictionary
                copy[key] = change
            
        print(copy)
        return copy  # returns the dictionary passed in, but updated with new info
    else:
        return None

#imports from json file
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

def temp_pull_orders():
    file_name = 'order_history copy.json'
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