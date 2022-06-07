from pickle import FALSE
import order_functions
import json
from unittest.mock import Mock, patch

#--------pull_orders-----------------
def test_pull_orders_output():
    with open('order_history.json') as file:
        expected = json.load(file)

    result = order_functions.pull_orders()

    assert expected == result

#-------create_order-------------------
@patch('couriers_fun.push_couriers')
@patch('couriers_fun.pull_couriers',side_effect=[{'2':{'open_orders':1}}])
@patch('builtins.input',side_effect=['james','bournemouth','bh8','07939265209','burger','cola','crisps'])
def test_create_order_corner(mock_input,mock_pull,mock_push):

    expected = {
        'user_data': {
            'name': 'james', 'address': 'bournemouth', 'post_code': 'bh8',
            'phone_number': '07939265209','courier' : "2", 'order_status': 'pending'},
        'items': {
            'food': 'burger', 'drink': 'cola', 'snack':'crisps'}
    }
    result = order_functions.create_order()

    assert expected == result

#--------------order_menu_create--------
@patch('builtins.input',side_effect=['',''])
def test_order_menu_create_edge_none(mock_input):
    expected = False 
    result = order_functions.order_menu_create()

    assert expected == result

@patch('builtins.input',side_effect=['egg',''])
def test_order_menu_create_edge_word(mock_input):
    expected = False
    result = order_functions.order_menu_create()

    assert expected == result

#--------order_menu_delete-------
@patch('builtins.input',side_effect=['cola','y',''])
def test_order_menu_delete_edge_product(mock_input):
    expect = False
    result = order_functions.order_menu_delete()

    assert expect == result

#-------order_menu_amend-----------
@patch('builtins.input',side_effect=['soda',''])
def test_order_menu_amend_invalid(mock_input):
    expected = False
    result = order_functions.order_menu_amend()

    assert expected == result

#----------order_nenu_update--------

#--------order_status---------------
@patch('builtins.input',side_effect=['','z','Delivered','t'])
def test_order_status_various(mock_input):
    expected = 'in-transit'
    result = order_functions.order_status()

    assert expected == result

