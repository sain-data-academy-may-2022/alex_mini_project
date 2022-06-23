from unittest.mock import Mock,patch
from decimal import Decimal
import product_functions as pf
import json

#TOTEST








#------------pull_product_by_name-------------
@patch('db.db.execute_and_return_one', side_effect=[(1,'orange',0.50,1)])
def test_pull_product_by_name(mock_ex_and_return):
    expected = {'product_id':1,'name':'orange','price':0.50,'vegan':1}
    result = pf.pull_product_by_name('food','orange')  
    assert expected == result  

#------------create_product-------------------
@patch('builtins.input',side_effect=[1.99,'y'])
def test_create_product(mock_input):
    expected = {'name':'tofu','price': 1.99,'vegan':1}
    result = pf.create_product('tofu')

    assert expected == result

#-----------pull_product_names----------------
@patch('product_functions.pull_product_name_plus_id',side_effect=[['egg',0],['tea',1],['toast',2]])
def test_pull_product_names(mock_pull_product_name):
    expected = [['egg',0],['tea',1],['toast',2]]
    result = pf.pull_product_names()

    assert expected == result

#-----------deactivate_product----------------
@patch('db.db.connect_execute_close_with_val')
def test_deactivate_product(mock_connect_execute_close_with_val: Mock):
    prod = {'product_id':3}
    pf.deactivate_product('food',prod)
    expected = 'update food set active = %s where food_id = %s'
    mock_connect_execute_close_with_val.assert_called_once_with(expected,(0,3))

def test_deactivate_product_none():
    prod = {'product_id':3}
    
    expected = 'no table - error'
    result = pf.deactivate_product('foods',prod)

    assert expected ==  result    

#--------------pull_product_name--------------

@patch('db.db.execute_and_return_all', side_effect=[(('egg',),('tuna',),('salad',))])
def test_pull_product_name_bad_str(mock_execute_and_return):
    table = 'foods'
    
    expected = None
    result = pf.pull_product_name(table)

    assert expected == result

@patch('db.db.execute_and_return_all', side_effect=[(('egg',),('tuna',),('salad',))])
def test_pull_product_name(mock_execute_and_return):
    table = 'food'
    
    expected = ['egg','tuna','salad']
    result = pf.pull_product_name(table)

    assert expected == result

@patch('db.db.execute_and_return_all', side_effect=[(('egg',),('tuna',),('salad',))])
def test_pull_product_name_typeError(mock_execute_and_return):
    table = 1
    
    expected = None
    result = pf.pull_product_name(table)

    assert expected == result

#--------------Table_checker------------------
def test_table_checker_default():
    table = 'drinks'
    
    expected = 'SELECT * FROM drinks'
    result = pf.table_checker(table)

    assert expected == result

def test_table_checker_delete():
    table = 'snack'
    
    expected = "update snack set active = %s where snack_id = %s"
    result = pf.table_checker(table,delete=True)

    assert expected == result

def test_table_checker_update():
    table = 'food'
    
    expected = "update food set name = %s, price = %s, vegan = %s where food_id = %s"
    result = pf.table_checker(table,update=True)

    assert expected == result

def test_table_checker_name():
    table = 'snack'
    
    expected = 'SELECT name, snack_id FROM snack WHERE active = 1'
    result = pf.table_checker(table,name=True)

    assert expected == result

def test_table_checker_push():
    table = 'snack'
    
    expected = "insert into snack (name,price,vegan) VALUES (%s,%s,%s)"
    result = pf.table_checker(table,push=True)

    assert expected == result

def test_table_checker_bad_string():
    table = 'dranks'
    
    expected = None
    result = pf.table_checker(table)

    assert expected == result

def test_table_checker_bad_type():
    table = 1
    
    expected = None
    result = pf.table_checker(table)

    assert expected == result

def test_table_checker_bad_string_optional():
    table = 'dranks'
    
    expected = None
    result = pf.table_checker(table,name=True)

    assert expected == result

def test_table_checker_bad_type_optional():
    table = 1
    
    expected = None
    result = pf.table_checker(table,delete=True)

    assert expected == result

#---------------duplicate_check-----------------
def test_dupe_check_corner_true():
    m_list = [1,5,7]
    expected = True
    result = pf.duplicate_check(m_list,7)
    assert expected == result
def test_dupe_check_corner_false():
    m_list = [1,5,7]

    expected = False
    result = pf.duplicate_check(m_list,6)

    assert expected == result

def test_dupe_check_corner_nested_true():
    m_list = [[1,5,7],[2,4,6]]

    expected = True
    result = pf.duplicate_check(m_list,6)

    assert expected == result

def test_dupe_check_corner_nested_false():
    m_list = [[1,5,7],[2,4,6]]

    expected = False
    result = pf.duplicate_check(m_list,3)

    assert expected == result

#-----------------list_str_check-------------

@patch('builtins.input', side_effect=[''])
def test_list_str_edge_str(mock_input):
    expected = None
    prods = [['egg',0],['toast',1]]
    result = pf.new_list_str_check(prods,'bark')

    assert expected == result

@patch('builtins.input', side_effect=[''])
def test_list_str_edge_int(mock_input):
    expected = None
    prods = [['egg',0],['toast',1]]

    result = pf.new_list_str_check(prods,'7')

    assert expected == result

def teest_list_str_corner_int():
    prods = [['egg',0],['toast',1]]

    expected = 'egg'
    result = pf.new_list_str_check(prods,'0')

    assert expected == result

def test_list_str_corner_str():
    prods = [['egg',0],['toast',1]]

    expected = 'toast'
    result = pf.new_list_str_check(prods,'toast')

    assert expected == result

def test_list_str_corner_blank():
    prods = [['egg',0],['toast',1]]

    expected = None
    result = pf.new_list_str_check(prods,'')

    assert expected == result

#-----------prod_input_to_index------------------

@patch('builtins.input', side_effect=[''])
def test_list_int_edge_str(mock_input):
    expected = None
    prods = ['egg','toast']
    result = pf.prod_input_to_index(prods,'bark')

    assert expected == result

@patch('builtins.input', side_effect=[''])
def test_list_int_edge_int(mock_input):
    expected = None
    prods = [['egg',0],['toast',1]]
    result = pf.prod_input_to_index(prods,'7')

    assert expected == result

def test_list_int_corner_int():
    prods = [['egg',0],['toast',1]]

    expected = 0
    result = pf.prod_input_to_index(prods,'0')

    assert expected == result

def test_list_int_corner_str():
    prods = [['egg',0],['toast',1]]

    expected = 1
    result = pf.prod_input_to_index(prods,'toast')

    assert expected == result


#---------update_product-----------
@patch('builtins.input',side_effect=['y','','0.99',''])
def test_update_product(mock_input):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':1.99,'vegan':0}
    price = round(Decimal(0.99),2)

    expected = {'product_id':1,'name':'egg','price':price,'vegan':0}
    result = pf.update_product(table,prod)

    assert expected == result

@patch('builtins.input',side_effect=['n'])
def test_update_product_cancel(mock_input):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':1.99,'vegan':0}
    
    expected = {'product_id':1,'name':'egg','price':1.99,'vegan':0}
    result = pf.update_product(table,prod)

    assert expected == result

@patch('builtins.input',side_effect=['y','','0',''])
def test_update_product_whole_price(mock_input):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':1.99,'vegan':0}
    price = round(Decimal(0))

    expected = {'product_id':1,'name':'egg','price':price,'vegan':0}
    result = pf.update_product(table,prod)

    assert expected == result

@patch('builtins.input',side_effect=['y','','',''])
def test_update_product_no_inputs(mock_input):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':1.99,'vegan':0}

    expected = {'product_id':1,'name':'egg','price':1.99,'vegan':0}
    result = pf.update_product(table,prod)

    assert expected == result

@patch('builtins.input',side_effect=['y','chicken','egg','','egg'])
def test_update_product_wrong_types(mock_input):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':1.99,'vegan':0}

    expected = {'product_id':1,'name':'chicken','price':1.99,'vegan':0}
    result = pf.update_product(table,prod)

    assert expected == result

@patch('builtins.input',side_effect=['y','','','1'])
def test_update_product_vegan(mock_input):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':1.99,'vegan':0}

    expected = {'product_id':1,'name':'egg','price':1.99,'vegan':1}
    result = pf.update_product(table,prod)

    assert expected == result

@patch('builtins.input',side_effect=['y','','','5'])
def test_update_product_big_vegan(mock_input):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':1.99,'vegan':0}

    expected = {'product_id':1,'name':'egg','price':1.99,'vegan':0}
    result = pf.update_product(table,prod)

    assert expected == result

#----------print_products-----------------
# not sure yet. has baked in db calls. hmmmmmmm

#-------------option3--------------------------

@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['egg'])
def test_option3(mock_input:Mock,mock_print_products:Mock,mock_new_list_str_check:Mock):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    expected = 'egg'
    result = pf.option_3(prod_list,table)

    assert expected == result

@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['0'])
def test_option3_int(mock_input,mock_print_prod,mock_list_str):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    expected = 'egg'
    result = pf.option_3(prod_list,table)

    assert expected == result

@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['0'])
def test_option3_input_check(mock_input:Mock,mock_print_prod:Mock,mock_list_str:Mock):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    pf.option_3(prod_list,table)
    mock_input.assert_called_once()

@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['0'])
def test_option3_input_print_check(mock_input:Mock,mock_print_prod:Mock,mock_list_str:Mock):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    pf.option_3(prod_list,table)
    mock_print_prod.assert_called_once_with(table)

@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['0'])
def test_option3_input_list_str_check(mock_input:Mock,mock_print_prod:Mock,mock_list_str:Mock):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    pf.option_3(prod_list,table)
    mock_list_str.assert_called_once_with(prod_list,'0')

#-------------option4--------------------------
    
@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['egg'])
def test_option4(mock_input:Mock,mock_print_products:Mock,mock_new_list_str_check:Mock):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    expected = 'egg'
    result = pf.option_4(prod_list,table)

    assert expected == result

@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['0'])
def test_option4_int(mock_input,mock_print_prod,mock_list_str):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    expected = 'egg'
    result = pf.option_4(prod_list,table)

    assert expected == result

@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['0'])
def test_option4_input_check(mock_input:Mock,mock_print_prod:Mock,mock_list_str:Mock):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    pf.option_4(prod_list,table)
    mock_input.assert_called_once()

@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['0'])
def test_option4_input_print_check(mock_input:Mock,mock_print_prod:Mock,mock_list_str:Mock):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    pf.option_4(prod_list,table)
    mock_print_prod.assert_called_once_with(table)

@patch('product_functions.new_list_str_check',side_effect=['egg'])
@patch('product_functions.print_products')
@patch('builtins.input',side_effect=['0'])
def test_option4_input_list_str_check(mock_input:Mock,mock_print_prod:Mock,mock_list_str:Mock):
    prod_list = [['egg',0],['toast',1]]
    table = 'food'

    pf.option_4(prod_list,table)
    mock_list_str.assert_called_once_with(prod_list,'0')

#----------push_product-----------------
@patch('product_functions.table_checker',side_effect=['insert into food (name,price,vegan) VALUES (%s,%s,%s)'])
@patch('db.db.connect_execute_close_with_val')
def test_push_product(mock_execute:Mock,mock_checker:Mock):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':0.99,'vegan':0}

    sql = 'insert into food (name,price,vegan) VALUES (%s,%s,%s)'
    expected = [sql,('egg',0.99,0)]
    pf.push_product(table,prod)

    mock_execute.assert_called_once_with(expected[0],expected[1])


@patch('builtins.input',side_effect=[''])
@patch('product_functions.table_checker',side_effect=['insert into food (name,price,vegan) VALUES (%s,%s,%s)'])
@patch('db.db.connect_execute_close_with_val' ,side_effect=[TypeError])
def test_push_product_error_check(mock_execute:Mock,mock_checker:Mock,mock_input:Mock):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':'0a9','vegan':0}

    pf.push_product(table,prod)

    mock_input.assert_called_once()

#-----------push_updated_product------------
@patch('product_functions.table_checker',side_effect=['update food set name = %s, price = %s, vegan = %s where food_id = %s'])
@patch('db.db.connect_execute_close_with_val')
def test_push_updated_product(mock_connect:Mock,mock_chekcer:Mock):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':0.99,'vegan':0}

    sql = 'update food set name = %s, price = %s, vegan = %s where food_id = %s'
    pf.push_updated_product(table,prod)
    
    mock_connect.assert_called_once_with(sql,('egg',0.99,0,1))

@patch('builtins.input',side_effect=[''])
@patch('product_functions.table_checker',side_effect=['update food set name = %s, price = %s, vegan = %s where food_id = %s'])
@patch('db.db.connect_execute_close_with_val',side_effect=[TypeError])
def test_push_updated_product_type_error(mock_connect:Mock,mock_chekcer,mock_input:Mock):
    table = 'food'
    prod = {'product_id':1,'name':'egg','price':'cheese','vegan':0}

    pf.push_updated_product(table,prod)
    
    mock_input.assert_called_once()



