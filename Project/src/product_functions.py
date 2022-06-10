import my_functions
import json
import traceback
import products
from db import db

# returns the contents of my-products.json as a nested list
def pull_produtcts(): 
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

def master_pull():
    connect = db.establish()
    prods = []
    
    prods.append(new_pull_products(connect,"food"))
    prods.append(new_pull_products(connect,'drinks'))
    prods.append(new_pull_products(connect,'snack'))
    
    db.shut_down(connect)
    return prods

def new_pull_products(connect,table):
    sql = f'SELECT * FROM {table}'
    val = (table)
    cursor = connect.cursor()
    cursor.execute(sql)
    desc = cursor.description
    col_names = [col[0] for col in desc]
    orders = [dict(zip(col_names, row)) 
        for row in cursor.fetchall()]
    return orders

def new_push_products(food,drinks,snacks):
    pass

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

# prints all entrys in list (includes index for all nested lists also. needs formatting for easier reading!!!!)
def print_products(products: list):
    x = 0
    for ind in products:
        if type(ind) == list:
            print_products(ind)
        else:
            print(x,ind)
            x+=1

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
    my_functions.print_list(product_list)  # prints product list, along with index ids
    entry = input(
        'please enter the id or name of the item you wish to update ')
    list_id = prod_input_to_index(product_list, entry)
    return list_id

# the menu part of the food/drinks/snacks delete item option
def option_4(product_list):
    my_functions.print_list(product_list)  # prints product list along with index ids
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

