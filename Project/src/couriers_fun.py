#imports


#creates and returns a new courier dictionary
def hire_courier():
    courier = {}
    courier['name'] = input('enter courier name: ')
    courier['open_orders'] = 0
    print(courier)
    return courier

def assign_order(couriers):
    name = ''
    lowest = 0
    for courier,orders in couriers:
        if name == "" or orders < lowest:
            name = courier
            lowest = orders
        else:
            continue
    return name