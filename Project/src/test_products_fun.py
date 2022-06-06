from unittest.mock import Mock,patch
import product_functions
import json

@patch('builtins.print')
def test_print_products(mock_print: Mock):
    test_list = [1,3,4,5]
    product_functions.print_products(test_list)

    mock_print.assert_any_call(0,1)
    mock_print.assert_any_call(1,3)
    mock_print.assert_any_call(2,4)
    mock_print.assert_any_call(3,5)
#---------------duplicate_check-----------------
def test_dupe_check_corner_true():
    m_list = [1,5,7]
    expected = True
    result = product_functions.duplicate_check(m_list,7)
    assert expected == result
def test_dupe_check_corner_false():
    m_list = [1,5,7]

    expected = False
    result = product_functions.duplicate_check(m_list,6)

    assert expected == result

def test_dupe_check_corner_nested_true():
    m_list = [[1,5,7],[2,4,6]]

    expected = True
    result = product_functions.duplicate_check(m_list,6)

    assert expected == result

def test_dupe_check_corner_nested_false():
    m_list = [[1,5,7],[2,4,6]]

    expected = False
    result = product_functions.duplicate_check(m_list,3)

    assert expected == result

#-----------------list_str_check-------------

@patch('builtins.input', side_effect=[''])
def test_list_str_edge_str(mock_input):
    expected = None
    prods = ['egg','toast']
    result = product_functions.list_str_check(prods,'bark')

    assert expected == result

@patch('builtins.input', side_effect=[''])
def test_list_str_edge_int(mock_input):
    expected = None
    prods = ['egg','toast']
    result = product_functions.list_str_check(prods,'7')

    assert expected == result

def test_list_str_corner_int():
    prods = ['egg','toast']

    expected = 'egg'
    result = product_functions.list_str_check(prods,'0')

    assert expected == result

def test_list_str_corner_str():
    prods = ['egg','toast']

    expected = 'toast'
    result = product_functions.list_str_check(prods,'toast')

    assert expected == result

#-----------list_int_check------------------

@patch('builtins.input', side_effect=[''])
def test_list_int_edge_str(mock_input):
    expected = None
    prods = ['egg','toast']
    result = product_functions.prod_input_to_index(prods,'bark')

    assert expected == result

@patch('builtins.input', side_effect=[''])
def test_list_int_edge_int(mock_input):
    expected = None
    prods = ['egg','toast']
    result = product_functions.prod_input_to_index(prods,'7')

    assert expected == result

def test_list_int_corner_int():
    prods = ['egg','toast']

    expected = 0
    result = product_functions.prod_input_to_index(prods,'0')

    assert expected == result

def test_list_int_corner_str():
    prods = ['egg','toast']

    expected = 1
    result = product_functions.prod_input_to_index(prods,'toast')

    assert expected == result