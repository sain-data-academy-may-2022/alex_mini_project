from pickle import TRUE
from turtle import pu
import my_functions as mf
import json
from decimal import Decimal
import traceback
from prettytable import from_db_cursor

from db import db



def pull_product_name(connect,table):
    names = []

    sql = table_checker(table,name=True)
    if sql == None:
        return None


    cursor = connect.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()

    for row in values:
        names.append(row[0])

    cursor.close()
    return names

def pull_product_names():
    prods = []
    connect = db.establish()
    prods.append(pull_product_name(connect,'food'))
    prods.append(pull_product_name(connect,'drinks'))
    prods.append(pull_product_name(connect,'snack'))
    db.shut_down(connect)
    return prods

def create_product(name):
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

def master_pull():
    connect = db.establish()
    prods = []
    
    prods.append(new_pull_products(connect,"food"))
    prods.append(new_pull_products(connect,'drinks'))
    prods.append(new_pull_products(connect,'snack'))
    
    db.shut_down(connect)
    return prods



def table_checker(table:str, push=False, name=False, update=False):
    if update == True:
        if table == 'food':
            sql = "update food set (name,price,vegan) where food_id = %s VALUES (%s,%s,%s)"
            return sql
        elif table == 'drinks':
            sql = "update drinks set (name,price,vegan) where (drinks_id) VALUES (%s,%s,%s,%s)"
            return sql
        elif table == 'snack':
            sql = "update snack set (name,price,vegan) where (snack_id) VALUES (%s,%s,%s,%s)"
            return sql
        else: 
            return None
    
    if name == True:
        if table == 'food':
            sql = 'SELECT name FROM food;'
            return sql
        elif table == 'drinks':
            sql = 'SELECT name FROM drinks'
            return sql
        elif table == 'snack':
            sql = 'SELECT name FROM snack'
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

def pull_product_by_name(table:str,name:str):
    connect = db.establish()
    cursor = connect.cursor()
    sql = table_checker(table)
    sql +=' WHERE name = %s'
    print(sql)
    val = (name)

    cursor.execute(sql,val)
    prod = cursor.fetchone()
    print(prod)
    ret = {'product_id':prod[0],'name':prod[1],'price':prod[2],'vegan':prod[3]}
    return ret

def update_product(table:str,prod:dict):
    confirm = input(f"are you sure you want to update {prod['name']}? \ny/n : ")
    print(prod)
    copy = prod
    
    if confirm == 'y' or confirm == 'Y':
        n_name = input('input new name or ENTER to skip : ')
        
        if n_name != '':
            copy['name'] = n_name
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
                copy['vegan'] = n_vegan

    return copy

def push_product(table:str,prod:dict):
    sql = table_checker(table,push=True)
    val = (prod['name'],prod['price'],prod['vegan'])
    try:
        db.connect_execute_close_with_val(sql,val)
    except Exception as e:
        input(f'error occured{e}, enter to continue')



def push_updated_product(table:str,prod:dict):

    sql = table_checker(table,update=True)
    val = (prod['product_id'],prod['name'],prod['price'],prod['vegan'])
    try:
        db.connect_execute_close_with_val(sql,val)
    except Exception as e:
        input(f'error updating table - {e}. \nENTER to continue')



def print_products(table:str):
    #handle each product menu
    sql = table_checker(table)
    if sql == None:
        return
    
    #create connection
    connect = db.establish()
    cursor = connect.cursor()
    
    #make and print table
    cursor.execute(sql)
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
def option_3(product_list):
    mf.print_list(product_list)  # prints product list, along with index ids
    entry = input(
        'please enter the id or name of the item you wish to update ')
    list_id = prod_input_to_index(product_list, entry)
    return list_id

# the menu part of the food/drinks/snacks delete item option
def option_4(product_list):
    mf.print_list(product_list)  # prints product list along with index ids
    entry = input("please enter the id or name of the item you wish to delete ")
    # function allows both text and numbers to be accepted, returns appropriate index (different text output)
    list_id = list_str_check(product_list, entry)
    return list_id

#returns the in index from a list, takes both string and int as input
def prod_input_to_index(product_list, list_id):
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

#returns the string value from a list, accepts both string and int values as input
def list_str_check(product_list, list_id):
    #list_id = input("please enter the id or name of the item you wish to delete ")
    if list_id.strip().isdigit():
        list_id = int(list_id)

        if list_id < len(product_list):
            return product_list[list_id]

        else:
            input('\nno product at index\n')
            return None

    elif list_id in product_list:
        return list_id

    else:
        input("\nno such entry exists, sorry\n")
        return None

def old_code_dont_run_please():
    '''
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
    pass