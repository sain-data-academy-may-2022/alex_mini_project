#imports
import json
from db import db
from prettytable import from_db_cursor
import random


#
def add_a_courier(courier):
    sql = 'INSERT into couriers (name, phone) Values (%s,%s)'
    val = (courier['name'],courier['phone'])
    try:
        db.connect_execute_close_with_val(sql,val)
    except:
        print('sql error') 

#
def print_couriers():
    connection = db.establish()
    cursor = connection.cursor()
    
    cursor.execute("select * from couriers")
    
    mytable = from_db_cursor(cursor)
    print(mytable)
    cursor.close()
    db.shut_down(connection)

#
def new_pull_couriers():
    connect = db.establish()
    cursor = connect.cursor()
    sql = ('SELECT * FROM couriers')
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close
    db.shut_down(connect)
    return data

#
def get_couriers_dict():
    couriers = []

    data = new_pull_couriers()
    for x in data:
        temp = {'id': x[0],'name':x[1], 'phone': x[2], 'orders': x[3]}
        couriers.append(temp)

    return(couriers)

def push_a_courier(courier):
    sql = 'UPDATE couriers SET name = %s, phone = %s WHERE courier_id = %s'
    val = (courier['name'],courier['phone'],courier['id'])
    db.connect_execute_close_with_val(sql,val)

#creates and returns a new courier dictionary
def hire_courier():
    courier = {}
    courier['name'] = input('enter courier name : ')
    courier['phone'] = input('enter courier phone number : ')
    print(courier)
    return courier

# loops through the courier info and allows you to update. returns an updated ditctoinary
def update_courier(courier):
    copy = {'name': courier['name'],
            'phone': courier['phone'],
            'id': courier['id']}

    for key, value in copy.items():
        if key == 'id': # dont want to go changing the id now, do we
            continue

        print(key, value,'enter ammendment or enter to skip : ')
        change = input()

        if change == '':# if nothing was entered
            continue
        else:
            copy[key] = change

    return copy

#
def increment_orders(courier):
    courier['orders'] +=1
    
    sql = 'UPDATE couriers SET orders = %s WHERE courier_id = %s'
    val = (courier['orders'],courier['id'])
    
    try:
        db.connect_execute_close_with_val(sql,val)
    except:
        input('sql error')
    
    return

def random_courier():
    couriers = get_couriers_dict()
    my_random = random.randrange(len(couriers))

    increment_orders(couriers[my_random])
    return couriers[my_random]['id']
    


#===========================================================================================================================
#=====================================================old===================================================================
#===========================================================================================================================







# returns the name of the courier with the least orders
def assign_order(couriers):
    name = ''
    lowest = 0
    for courier,orders in couriers:
        if name == "" or orders < lowest:
            name = courier
            lowest = orders
        else:
            continue
    return name



#=========================
#======replaced===========
#=========================

#populates a dictionary with the contents of couriers.json
# def pull_couriers():
#     file_name = 'couriers.json'
#     try:
#         with open(file_name) as file:
#             couriers = json.load(file)
#     except:
#         print(file_name, 'not found, new file will be created')
#     return couriers

#prints the contents of the provided dictionary somewhat neatly
# def print_couriers(couriers):
#     for key, value in couriers.items():
#         if type(value) == dict:
#             print(key)
#             print_couriers(value)
#         else:
#             print(key,' : ',value)

#updates the couriers.json file with the provided dictionary
# def push_couriers(couriers):
#     file_name = 'couriers.json'
#     try:
#         with open(file_name, 'w') as file:
#             new = json.dumps(couriers, indent='    ')
#             file.write(new)
#     except:
#         print('unable to create / find', file_name)
#         input('enter to continue : ')