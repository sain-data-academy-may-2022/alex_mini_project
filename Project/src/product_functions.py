from pickle import TRUE
from turtle import pu
import my_functions as mf
import json
from decimal import Decimal
import traceback
from prettytable import from_db_cursor

from db import db

#
def pull_product_name_plus_id(table):
    names = []

    sql = table_checker(table,name=True)
    # check for bad table name
    if sql == None:
        return None

    values = db.execute_and_return_all(sql)
    
    for row in values:
        val = []
        val.append(row[0])
        val.append(row[1])
        names.append(val)

    return names

#
def pull_product_name(table):
    names = []

    sql = table_checker(table,name=True)
    # check for bad table name
    if sql == None:
        return None

    values = db.execute_and_return_all(sql)
    
    for row in values:
        names.append(row[0])

    return names

def deactivate_product(table,product):
    sql = table_checker(table,delete=True)
    # update food set active = %s where food_id =%s
    if sql == None:
        return 'no table - error'

    val = (0,product['product_id'])
        
    try:
        db.connect_execute_close_with_val(sql,val)
    except:
        print('sql error')
        input

#
def pull_product_names():
    prods = []
    
    prods.append(pull_product_name_plus_id('food'))
    prods.append(pull_product_name_plus_id('drinks'))
    prods.append(pull_product_name_plus_id('snack'))
    
    return prods

#
def create_product(name:str):
    prod_form = {'name':'None','price': None,'vegan':None}

    prod_form['name'] = name
    
    is_dec = True
    while is_dec:
        mf.clear_term()
        try:
            prod_form['price'] = Decimal(input('enter product price in 0.00 format : '))
            is_dec = False
        except Exception as e:
            print(f'error occured {e}, please try again : ')
            input()

    vegan_in = ''
    while vegan_in != 'y' and vegan_in != 'n':
        mf.clear_term()
        vegan_in = input('is product vegan y/n? : ') 
    
    if vegan_in == 'y':
        prod_form['vegan'] = 1
    else:
        prod_form['vegan'] = 0

    return prod_form

#
def master_pull():
    connect = db.establish()
    prods = []
    
    prods.append(new_pull_products(connect,"food"))
    prods.append(new_pull_products(connect,'drinks'))
    prods.append(new_pull_products(connect,'snack'))
    
    db.shut_down(connect)
    return prods

#
def table_checker(table:str, push=False, name=False, update=False, delete=False):
    if delete == True:
        if table == 'food':
            sql = "update food set active = %s where food_id = %s"
            return sql
        elif table == 'drinks':
            sql = "update drinks set active = %s where drinks_id = %s"
            return sql
        elif table == 'snack':
            sql = "update snack set active = %s where snack_id = %s"
            return sql
        else: 
            return None
    
    if update == True:
        if table == 'food':
            sql = "update food set name = %s, price = %s, vegan = %s where food_id = %s"
            return sql
        elif table == 'drinks':
            sql = "update drinks set name = %s, price = %s, vegan = %s where drinks_id = %s"
            return sql
        elif table == 'snack':
            sql = "update snack set name = %s, price = %s, vegan = %s where snack_id = %s"
            return sql
        else: 
            return None
    
    if name == True:
        if table == 'food':
            sql = 'SELECT name, food_id FROM food WHERE active = 1;'
            return sql
        elif table == 'drinks':
            sql = 'SELECT name, drinks_id FROM drinks WHERE active = 1'
            return sql
        elif table == 'snack':
            sql = 'SELECT name, snack_id FROM snack WHERE active = 1'
            return sql
        else:
            return None        

    if push == True:
        if table == 'food':
            sql = "insert into food (name,price,vegan) VALUES (%s,%s,%s)"
            return sql
        elif table == 'drinks':
            sql = "insert into drinks (name,price,vegan) VALUES (%s,%s,%s)"
            return sql
        elif table == 'snack':
            sql = "insert into snack (name,price,vegan) VALUES (%s,%s,%s)"
            return sql
        else: 
            return None  
    
    else:
        if table == 'food':
            sql = 'SELECT * FROM food'
            return sql
        elif table == 'drinks':
            sql = 'SELECT * FROM drinks'
            return sql
        elif table == 'snack':
            sql = 'SELECT * FROM snack'
            return sql
        else: 
            return None

#
def new_pull_products(connect,table):
    # handles each variation of the products menu
    sql = table_checker(table)
    if sql == None:
        return None

    #gets cursor and description
    cursor = connect.cursor()
    cursor.execute(sql)
    desc = cursor.description

    col_names = [col[0] for col in desc]
    products = [dict(zip(col_names, row)) for row in cursor.fetchall()]

    cursor.close()

    return products

#
def pull_product_by_name(table:str,name:str):
    
    sql = table_checker(table)
    sql +=' WHERE name = %s'
    val = (name)

    prod = db.execute_and_return_one(sql,val=val)

    ret = {'product_id':prod[0],'name':prod[1],'price':prod[2],'vegan':prod[3]}
    return ret

#
def update_product(table:str,prod:dict):
    confirm = input(f"are you sure you want to update {prod['name']}? \ny/n : ")
    print(prod)
    copy = {'product_id':prod['product_id'],
            'name': prod['name'],
            'price': prod['price'],
            'vegan': prod['vegan']}
            
    
    if confirm == 'y' or confirm == 'Y':
        n_name = input('input new name or ENTER to skip : ')
        
        if n_name != '':
            copy['name'] = n_name
            print(copy)
        n_price = input('input new price or ENTER to skip : ')
        
        if n_price != '':
            try:
                n_price = Decimal(n_price)
                copy['price'] = n_price
            except:
                input('incorrect price format. ENTER to continue : ')
        
        n_vegan = input('input new vegan status or ENTER to skip : ')
        if n_vegan != '':
            if n_vegan == '0' or n_vegan == '1':
                copy['vegan'] = int(n_vegan)

    return copy

#
def push_product(table:str,prod:dict):
    sql = table_checker(table,push=True)
    val = (prod['name'],prod['price'],prod['vegan'])
    try:
        db.connect_execute_close_with_val(sql,val)
    except Exception as e:
        input(f'error occured{e}, enter to continue')

#
def push_updated_product(table:str,prod:dict):

    sql = table_checker(table,update=True)
    print(sql)
    val = (prod['name'],prod['price'],prod['vegan'],prod['product_id'])
    try:
        db.connect_execute_close_with_val(sql,val)
    except Exception as e:
        input(f'error updating table - {e}. \nENTER to continue')

#
def print_products(table:str):
    #handle each product menu
    sql = table_checker(table)
    if sql == None:
        return
    sql += " WHERE active = %s"
    val = (1)
    
    #create connection
    connect = db.establish()
    cursor = connect.cursor()
    
    #make and print table
    cursor.execute(sql,val)
    mytable = from_db_cursor(cursor)
    print(mytable)
    
    #close connection
    cursor.close()
    db.shut_down(connect)

# checks all list values (including nested) for duplicates
def duplicate_check(my_list,check):
    for ind in my_list:
        if type(ind) == list:
            if duplicate_check(my_list[my_list.index(ind)],check) == True:
                return True   
    if check in my_list:
        return True
    else:
        return False

# the menu part of the food/drinks/snacks update item option
def option_3(product_list,table):
    print_products(table)  # prints product list, along with index ids
    entry = input(
        'please enter the id or name of the item you wish to update ')
    list_id = new_list_str_check(product_list, entry)
    return list_id

# the menu part of the food/drinks/snacks delete item option
def option_4(product_list,table):
    print_products(table)  # prints product list along with index ids
    entry = input("please enter the id or name of the item you wish to delete ")
    # function allows both text and numbers to be accepted, returns appropriate index (different text output)
    list_id = new_list_str_check(product_list, entry)
    return list_id

def prod_input_to_index(product_list:list, list_id:str):
    if list_id.strip().isdigit():  # if input is a number convert to int
        list_id = int(list_id)
        
        for ind in product_list:
            index = product_list.index(ind)
            
            if list_id in product_list[index]:
                return list_id
        
        input("\nno product at index\n")
        return None

    else: 
        # if it is a string, check the index location if it has one and store it
        
        for ind in product_list:
            index = product_list.index(ind)
            if list_id in product_list[index][0]:
                return product_list[index][1]
            else:
                continue

   
        input("\nno such entry exists\n")
        return None

#returns the in index from a list, takes both string and int as input
def old_prod_input_to_index(product_list, list_id):
    if list_id.strip().isdigit():  # if input is a number convert to int
        list_id = int(list_id)

        if list_id < len(product_list):
            return list_id

        else:
            input("\nno product at index\n")
            return None

    elif list_id in product_list:
        # if it is a string, check the index location if it has one and store it
        list_id = int(product_list.index(list_id))
        return list_id

    else:
        input("\nno such entry exists\n")
        return None

def new_list_str_check(product_list:list, list_id:str):
    if list_id == '':
        return None

    if list_id.strip().isdigit():  # if input is a number convert to int
        list_id = int(list_id)
        
        for ind in product_list:
            index = product_list.index(ind)
            
            if list_id in product_list[index]:
                return product_list[index][0]
        
        input("\nno product at index\n")
        return None

    else: # if it is a string, check the index location if it has one and store it
        
        for ind in product_list:
            index = product_list.index(ind)
            if list_id in product_list[index][0]:
                return list_id
            else:
                continue
   
        input("\nno such entry exists\n")
        return None

#returns the string value from a list, accepts both string and int values as input


#def old_code_dont_run_please
    '''
    def list_str_check(product_list, list_id):
    #list_id = input("please enter the id or name of the item you wish to delete ")
    if list_id.strip().isdigit():
        list_id = int(list_id)

        if list_id < len(product_list):
            return product_list[list_id-1]

        else:
            input('\nno product at index\n')
            return None

    elif list_id in product_list:
        return list_id

    else:
        input("\nno such entry exists, sorry\n")
        return None

    # updates the my-products.json file with a provided set of datapoints
    def push_products(food,drinks,snacks):
        prod_dict = {'food': food, 'drinks': drinks,'snacks':snacks}
        file_name = 'my-products.json'
        try:
            with open(file_name, 'w') as file:
                new = json.dumps(prod_dict, indent='    ')
                file.write(new)
        except Exception as e:
            print('unable to create / find', file_name)
            print(traceback.print_exc(),e)
    
    # returns the contents of my-products.json as a nested list
    def pull_products(): 
        products = []
        file_name = 'my-products.json'
        try:
            with open(file_name) as file:
                prod_dict = json.load(file)
                #print(prod_dict)
                for key,value in prod_dict.items():
                    products.append(value)
        except Exception as e:
            print(file_name, 'not found, new file will be created', e)
            print(traceback.print_exc())
            for x in range(0,3):
                products.append([])
        #my_functions.print_list(products)
        return products

    def print_products(products: list):
        x = 0
        for ind in products:
            if type(ind) == list:
                print_products(ind)
            else:
                print(x,ind)
                x+=1
    '''