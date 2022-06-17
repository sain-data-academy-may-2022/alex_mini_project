from unittest.mock import Mock,patch
from product_functions import *
import json









#------------pull_product_by_name-------------
@patch('db.db.execute_and_return_one', side_effect=[(1,'orange',0.50,1)])
def test_pull_product_by_name(mock_ex_and_return):
    expected = {'product_id':1,'name':'orange','price':0.50,'vegan':1}
    result = pull_product_by_name('food','orange')  
    assert expected == result  

#------------create_product-------------------
@patch('builtins.input',side_effect=[1.99,'y'])
def test_create_product(mock_input):
    expected = {'name':'tofu','price': 1.99,'vegan':1}
    result = create_product('tofu')

    assert expected == result

#-----------pull_product_names----------------
@patch('product_functions.pull_product_name',side_effect=[['egg'],['tea'],['toast']])
def test_pull_product_names(mock_pull_product_name):
    expected = [['egg'],['tea'],['toast']]
    result = pull_product_names()

    assert expected == result

#-----------deactivate_product----------------
@patch('db.db.connect_execute_close_with_val')
def test_deactivate_product(mock_connect_execute_close_with_val: Mock):
    prod = {'product_id':3}
    deactivate_product('food',prod)
    expected = 'update food set active = %s where food_id = %s'
    mock_connect_execute_close_with_val.assert_called_once_with(expected,(0,3))

def test_deactivate_product_none():
    prod = {'product_id':3}
    
    expected = 'no table - error'
    result = deactivate_product('foods',prod)

    assert expected ==  result    

#--------------pull_product_name--------------

@patch('db.db.execute_and_return_all', side_effect=[(('egg',),('tuna',),('salad',))])
def test_pull_product_name_bad_str(mock_execute_and_return):
    table = 'foods'
    
    expected = None
    result = pull_product_name(table)

    assert expected == result

@patch('db.db.execute_and_return_all', side_effect=[(('egg',),('tuna',),('salad',))])
def test_pull_product_name(mock_execute_and_return):
    table = 'food'
    
    expected = ['egg','tuna','salad']
    result = pull_product_name(table)

    assert expected == result

@patch('db.db.execute_and_return_all', side_effect=[(('egg',),('tuna',),('salad',))])
def test_pull_product_name_typeError(mock_execute_and_return):
    table = 1
    
    expected = None
    result = pull_product_name(table)

    assert expected == result

#--------------Table_checker------------------
def test_table_checker_default():
    table = 'drinks'
    
    expected = 'SELECT * FROM drinks'
    result = table_checker(table)

    assert expected == result

def test_table_checker_delete():
    table = 'snack'
    
    expected = "update snack set active = %s where snack_id = %s"
    result = table_checker(table,delete=True)

    assert expected == result

def test_table_checker_update():
    table = 'food'
    
    expected = "update food set name = %s, price = %s, vegan = %s where food_id = %s"
    result = table_checker(table,update=True)

    assert expected == result

def test_table_checker_name():
    table = 'snack'
    
    expected = 'SELECT name FROM snack WHERE active = 1'
    result = table_checker(table,name=True)

    assert expected == result

def test_table_checker_push():
    table = 'snack'
    
    expected = "insert into snack (name,price,vegan) VALUES (%s,%s,%s)"
    result = table_checker(table,push=True)

    assert expected == result

def test_table_checker_bad_string():
    table = 'dranks'
    
    expected = None
    result = table_checker(table)

    assert expected == result

def test_table_checker_bad_type():
    table = 1
    
    expected = None
    result = table_checker(table)

    assert expected == result

def test_table_checker_bad_string_optional():
    table = 'dranks'
    
    expected = None
    result = table_checker(table,name=True)

    assert expected == result

def test_table_checker_bad_type_optional():
    table = 1
    
    expected = None
    result = table_checker(table,delete=True)

    assert expected == result

#---------------old-print_products-----------------------------------
@patch('builtins.print')
def teest_print_products(mock_print: Mock):
    test_list = [1,3,4,5]
    print_products(test_list)

    mock_print.assert_any_call(0,1)
    mock_print.assert_any_call(1,3)
    mock_print.assert_any_call(2,4)
    mock_print.assert_any_call(3,5)
#---------------duplicate_check-----------------
def test_dupe_check_corner_true():
    m_list = [1,5,7]
    expected = True
    result = duplicate_check(m_list,7)
    assert expected == result
def test_dupe_check_corner_false():
    m_list = [1,5,7]

    expected = False
    result = duplicate_check(m_list,6)

    assert expected == result

def test_dupe_check_corner_nested_true():
    m_list = [[1,5,7],[2,4,6]]

    expected = True
    result = duplicate_check(m_list,6)

    assert expected == result

def test_dupe_check_corner_nested_false():
    m_list = [[1,5,7],[2,4,6]]

    expected = False
    result = duplicate_check(m_list,3)

    assert expected == result

#-----------------list_str_check-------------

@patch('builtins.input', side_effect=[''])
def test_list_str_edge_str(mock_input):
    expected = None
    prods = ['egg','toast']
    result = list_str_check(prods,'bark')

    assert expected == result

@patch('builtins.input', side_effect=[''])
def test_list_str_edge_int(mock_input):
    expected = None
    prods = ['egg','toast']
    result = list_str_check(prods,'7')

    assert expected == result

def teest_list_str_corner_int():
    prods = ['egg','toast']

    expected = 'egg'
    result = list_str_check(prods,'0')

    assert expected == result

def test_list_str_corner_str():
    prods = ['egg','toast']

    expected = 'toast'
    result = list_str_check(prods,'toast')

    assert expected == result

#-----------list_int_check------------------

@patch('builtins.input', side_effect=[''])
def test_list_int_edge_str(mock_input):
    expected = None
    prods = ['egg','toast']
    result = prod_input_to_index(prods,'bark')

    assert expected == result

@patch('builtins.input', side_effect=[''])
def test_list_int_edge_int(mock_input):
    expected = None
    prods = ['egg','toast']
    result = prod_input_to_index(prods,'7')

    assert expected == result

def test_list_int_corner_int():
    prods = ['egg','toast']

    expected = 0
    result = prod_input_to_index(prods,'0')

    assert expected == result

def test_list_int_corner_str():
    prods = ['egg','toast']

    expected = 1
    result = prod_input_to_index(prods,'toast')

    assert expected == result