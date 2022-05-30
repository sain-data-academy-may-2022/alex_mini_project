import order_functions
import json

def test_pull_orders_output():
    with open('order_history.json') as file:
        expected = json.load(file)

    result = order_functions.pull_orders()

    assert expected == result
