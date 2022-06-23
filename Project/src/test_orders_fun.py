import order_functions
import json
from unittest.mock import Mock, patch, call

dummy_order = {
        'first_name': 'Alex','last_name': 'Parham', 'address': 'BH8 8LW', 
        'phone_number': '07860251308','courier' : 2, 'status': 'pending',
        'food': 0, 'drink': 1, 'snack':2}

#--------order_menu_delete-------
@patch('builtins.input',side_effect=['cola','y',''])
def tesst_order_menu_delete_edge_product(mock_input):
    expect = False
    result = order_functions.order_menu_delete()

    assert expect == result

#-------order_menu_amend-----------
@patch('order_functions.update_order_sql')
@patch('order_functions.get_specific_order',side_effect=[dummy_order])
@patch('order_functions.order_amend',side_effect=[dummy_order])
@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4]])
@patch('builtins.input',side_effect=['2'])
def test_order_menu_amend(mock_input:Mock,mock_nums:Mock,mock_ammend:Mock,mock_order:Mock,mock_sql:Mock):
    expected = True
    result = order_functions.order_menu_amend()

    mock_order.assert_called_once_with(2)
    mock_nums.assert_called_once()
    mock_input.assert_called_once()
    mock_ammend.assert_called_once_with(dummy_order)
    mock_sql.assert_called_once_with(dummy_order)
    assert expected == result

@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4]])
@patch('builtins.input',side_effect=['9',''])
def test_order_menu_amend_invalid(mock_input,mock_nums):
    expected = False
    result = order_functions.order_menu_amend()

    assert expected == result

@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4]])
@patch('builtins.input',side_effect=['salad',''])
def test_order_menu_amend_invalid_str(mock_input,mock_nums):
    expected = False
    result = order_functions.order_menu_amend()

    assert expected == result

@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4]])
@patch('builtins.input',side_effect=['1.1',''])
def test_order_menu_amend_invalid_float(mock_input,mock_nums):
    expected = False
    result = order_functions.order_menu_amend()

    assert expected == result

@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4]])
@patch('builtins.input',side_effect=['-1',''])
def test_order_menu_amend_invalid_negative(mock_input,mock_nums):
    expected = False
    result = order_functions.order_menu_amend()

    assert expected == result

@patch('order_functions.get_specific_order',side_effect=[dummy_order])
@patch('order_functions.order_amend',side_effect=[None])
@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4]])
@patch('builtins.input',side_effect=['2'])
def test_order_menu_amend_none_returned(mock_input:Mock,mock_nums:Mock,mock_ammend:Mock,mock_order:Mock):
    expected = False
    result = order_functions.order_menu_amend()

    mock_order.assert_called_once_with(2)
    mock_nums.assert_called_once()
    mock_input.assert_called_once()
    mock_ammend.assert_called_once_with(dummy_order)
    assert expected == result

#--------order_status---------------
@patch('order_functions.order_status_while',side_effect=[('cooking',False)])
def test_order_status(mock_while:Mock):
    expected = 'cooking'
    result = order_functions.order_status()

    mock_while.assert_called_once_with('',True)
    assert expected == result

@patch('order_functions.order_status_while',side_effect=[("",True),("cooking",False)])
def test_order_status_multiple(mock_while:Mock):
    expected = 'cooking'
    result = order_functions.order_status()
    calls = [call('',True),call('',True)]

    mock_while.assert_has_calls(calls)
    assert expected == result

#--------order_status_while-------
@patch('builtins.input',side_effect=['t'])
@patch('builtins.print')
def test_order_status_while_letter(mock_print:Mock,mock_input:Mock):
    val = ''
    run = True
    expected = ('in-transit',False)
    print_val = 'd = delivered\nt = in-transit\np = pending\nc = cooking'
    result = order_functions.order_status_while(val,run)

    mock_print.assert_called_once_with(print_val)
    assert expected == result

@patch('builtins.input',side_effect=['delivered'])
@patch('builtins.print')
def test_order_status_while_word(mock_print:Mock,mock_input:Mock):
    val = ''
    run = True
    expected = ('delivered',False)
    print_val = 'd = delivered\nt = in-transit\np = pending\nc = cooking'
    result = order_functions.order_status_while(val,run)

    mock_print.assert_called_once_with(print_val)
    assert expected == result

@patch('builtins.input',side_effect=['deleevered'])
@patch('builtins.print')
def test_order_status_while_mistake(mock_print:Mock,mock_input:Mock):
    val = ''
    run = True
    expected = ('',True)
    print_val = 'd = delivered\nt = in-transit\np = pending\nc = cooking'
    calls = [call(print_val),call('invalid entry')]
    result = order_functions.order_status_while(val,run)

    mock_print.assert_has_calls(calls)
    assert expected == result

@patch('builtins.input',side_effect=['z'])
@patch('builtins.print')
def test_order_status_while_mistake_letter(mock_print:Mock,mock_input:Mock):
    val = ''
    run = True
    expected = ('',True)
    print_val = 'd = delivered\nt = in-transit\np = pending\nc = cooking'
    calls = [call(print_val),call('invalid entry')]
    result = order_functions.order_status_while(val,run)

    mock_print.assert_has_calls(calls)
    assert expected == result

#------upload_order-------------
@patch('db.db.connect_execute_close_with_val')
def test_upload_order(mock_con_ex:Mock):
    sql = "insert into orders (first_name,last_name,address,phone,courier,status,food,drink,snack) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (dummy_order['first_name'],
            dummy_order['last_name'],
            dummy_order['address'],
            dummy_order['phone_number'],
            dummy_order['courier'],
            dummy_order['status'],
            dummy_order['food'],
            dummy_order['drink'],
            dummy_order['snack'])

    order_functions.upload_order(dummy_order)

    mock_con_ex.assert_called_once_with(sql,val)

@patch('builtins.input',side_effect=[''])
@patch('db.db.connect_execute_close_with_val',side_effect=[TypeError])
def test_upload_order_except(mock_con_ex:Mock,mock_input:Mock):
    sql = "insert into orders (first_name,last_name,address,phone,courier,status,food,drink,snack) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (dummy_order['first_name'],
            dummy_order['last_name'],
            dummy_order['address'],
            dummy_order['phone_number'],
            dummy_order['courier'],
            dummy_order['status'],
            dummy_order['food'],
            dummy_order['drink'],
            dummy_order['snack'])

    order_functions.upload_order(dummy_order)

    mock_con_ex.assert_called_once_with(sql,val)
    mock_input.assert_called_once()

#--------create_order-------------
@patch('product_functions.print_products')
@patch('my_functions.clear_term')
@patch('couriers_fun.random_courier',side_effect=[2])
@patch('builtins.input',side_effect=['Alex','Parham','BH8 8LW','07860251308','0','1','2'])
@patch('product_functions.pull_product_names',side_effect=[[[['egg',0],['toast',1]],[['cola',0],['tea',1]],[['granola',0],['apple',1],['orange',2]]]])
@patch('order_functions.upload_order')
def test_create_order(mock_upload:Mock,mock_names:Mock,mock_input:Mock,mock_courier:Mock,mock_clear:Mock,mock_l_print:Mock):    
    calls = [call('please enter User first_name : '),   call('please enter User last_name : '),
        call('please enter User address : '),           call('please enter User phone_number : '),
        call('please enter customers food item : '),    call('please enter customers drink item : '),   
        call('please enter customers snack item : '),]

    order_functions.create_order()
    
    mock_upload.assert_called_once_with(dummy_order)
    mock_names.assert_called_once()
    mock_input.assert_has_calls(calls)
    mock_courier.assert_called_once()
    mock_clear.assert_called()
    mock_l_print.assert_called()

@patch('product_functions.print_products')
@patch('my_functions.clear_term')
@patch('couriers_fun.random_courier',side_effect=[2])
@patch('builtins.input',side_effect=['Alex','Parham','BH8 8LW','07860251308','egg','tea','orange'])
@patch('product_functions.pull_product_names',side_effect=[[[['egg',0],['toast',1]],[['cola',0],['tea',1]],[['granola',0],['apple',1],['orange',2]]]])
@patch('order_functions.upload_order')
def test_create_order_names(mock_upload:Mock,mock_names:Mock,mock_input:Mock,mock_courier:Mock,mock_clear:Mock,mock_l_print:Mock):    
    calls = [call('please enter User first_name : '),   call('please enter User last_name : '),
        call('please enter User address : '),           call('please enter User phone_number : '),
        call('please enter customers food item : '),    call('please enter customers drink item : '),   
        call('please enter customers snack item : '),]

    order_functions.create_order()
    
    mock_upload.assert_called_once_with(dummy_order)
    mock_names.assert_called_once()
    mock_input.assert_has_calls(calls)
    mock_courier.assert_called_once()
    mock_clear.assert_called()
    mock_l_print.assert_called()

@patch('product_functions.print_products')
@patch('my_functions.clear_term')
@patch('couriers_fun.random_courier',side_effect=[2])
@patch('builtins.input',side_effect=['Alex','Parham','BH8 8LW','07860251308','5','','0','5','','1','5','','2'])
@patch('product_functions.pull_product_names',side_effect=[[[['egg',0],['toast',1]],[['cola',0],['tea',1]],[['granola',0],['apple',1],['orange',2]]]])
@patch('order_functions.upload_order')
def test_create_order_loop_check(mock_upload:Mock,mock_names:Mock,mock_input:Mock,mock_courier:Mock,mock_clear:Mock,mock_l_print:Mock):    
    calls = [call('please enter User first_name : '),               call('please enter User last_name : '),
        call('please enter User address : '),                       call('please enter User phone_number : '),
        call('please enter customers food item : '),                call('please enter a valid input. enter to continue : '),    
        call('please enter customers food item : '),                call('please enter customers drink item : '),
        call('please enter a valid input. enter to continue : '),   call('please enter customers drink item : '), 
        call('please enter customers snack item : '),               call('please enter a valid input. enter to continue : '),
        call('please enter customers snack item : ')]

    order_functions.create_order()
    
    mock_upload.assert_called_once_with(dummy_order)
    mock_names.assert_called_once()
    mock_input.assert_has_calls(calls)
    mock_courier.assert_called_once()
    mock_clear.assert_called()
    mock_l_print.assert_called()

@patch('product_functions.print_products')
@patch('my_functions.clear_term')
@patch('couriers_fun.random_courier',side_effect=[2])
@patch('builtins.input',side_effect=['Alex','Parham','BH8 8LW','07860251308','5','','0','1.1','','1','soup','','2'])
@patch('product_functions.pull_product_names',side_effect=[[[['egg',0],['toast',1]],[['cola',0],['tea',1]],[['granola',0],['apple',1],['orange',2]]]])
@patch('order_functions.upload_order')
def test_create_order_loop_check_bad_vars(mock_upload:Mock,mock_names:Mock,mock_input:Mock,mock_courier:Mock,mock_clear:Mock,mock_l_print:Mock):    
    calls = [call('please enter User first_name : '),               call('please enter User last_name : '),
        call('please enter User address : '),                       call('please enter User phone_number : '),
        call('please enter customers food item : '),                call('please enter a valid input. enter to continue : '),    
        call('please enter customers food item : '),                call('please enter customers drink item : '),
        call('please enter a valid input. enter to continue : '),   call('please enter customers drink item : '), 
        call('please enter customers snack item : '),               call('please enter a valid input. enter to continue : '),
        call('please enter customers snack item : ')]
    
    order_functions.create_order()
    
    mock_upload.assert_called_once_with(dummy_order)
    mock_names.assert_called_once()
    mock_input.assert_has_calls(calls)
    mock_courier.assert_called_once()
    mock_clear.assert_called()
    mock_l_print.assert_called()

#------------order_delete_from_db-----------
@patch('db.db.connect_execute_close_with_val')
def test_order_delete_from_db(mock_connect:Mock):
    num = 5
    expected = True
    result = order_functions.order_delete_from_db(num)

    assert expected == result
    mock_connect.assert_called_once_with("DELETE FROM orders WHERE order_number = %s",(num))

@patch('builtins.input',side_effect=[''])
@patch('db.db.connect_execute_close_with_val',side_effect=[TypeError])
def test_order_delete_from_db(mock_connect:Mock,mock_input:Mock):
    num = 'five'
    expected = False
    result = order_functions.order_delete_from_db(num)

    assert expected == result
    mock_connect.assert_called_once_with("DELETE FROM orders WHERE order_number = %s",(num))
    mock_input.assert_called_once()

#------order_menu_delete-----------
@patch('order_functions.order_delete_from_db')
@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4,5]])
@patch('order_functions.print_an_order')
@patch('builtins.input',side_effect=['5','y'])
def test_order_menu_delete(mock_input:Mock,mock_print_o:Mock,mock_nums:Mock,mock_delete:Mock):
    expected = True
    result = order_functions.order_menu_delete()

    assert expected == result
    mock_input.assert_called()
    mock_print_o.assert_called_once_with(5)
    mock_nums.assert_called_once()
    mock_delete.assert_called_once_with(5)

@patch('order_functions.order_delete_from_db')
@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4,5]])
@patch('order_functions.print_an_order')
@patch('builtins.input',side_effect=['5','Y'])
def test_order_menu_delete_cap(mock_input:Mock,mock_print_o:Mock,mock_nums:Mock,mock_delete:Mock):
    expected = True
    result = order_functions.order_menu_delete()

    assert expected == result
    mock_input.assert_called()
    mock_print_o.assert_called_once_with(5)
    mock_nums.assert_called_once()
    mock_delete.assert_called_once_with(5)

@patch('order_functions.order_delete_from_db')
@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4,5]])
@patch('order_functions.print_an_order')
@patch('builtins.input',side_effect=['5','n',''])
def test_order_menu_delete_no(mock_input:Mock,mock_print_o:Mock,mock_nums:Mock,mock_delete:Mock):
    expected = False
    result = order_functions.order_menu_delete()

    assert expected == result
    mock_input.assert_called()
    mock_print_o.assert_called_once_with(5)
    mock_nums.assert_called_once()

@patch('order_functions.order_delete_from_db')
@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4,5]])
@patch('order_functions.print_an_order')
@patch('builtins.input',side_effect=['7','Y',''])
def test_order_menu_delete_bad_order(mock_input:Mock,mock_print_o:Mock,mock_nums:Mock,mock_delete:Mock):
    expected = False
    result = order_functions.order_menu_delete()

    assert expected == result
    mock_input.assert_called()
    mock_print_o.assert_called_once_with(7)
    mock_nums.assert_called_once()

@patch('order_functions.order_delete_from_db')
@patch('order_functions.get_order_nums',side_effect=[[1,2,3,4,5]])
@patch('order_functions.print_an_order')
@patch('builtins.input',side_effect=['seven',''])
def test_order_menu_delete_bad_input(mock_input:Mock,mock_print_o:Mock,mock_nums:Mock,mock_delete:Mock):
    expected = False
    result = order_functions.order_menu_delete()

    assert expected == result
    mock_input.assert_called()