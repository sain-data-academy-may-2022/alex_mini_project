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