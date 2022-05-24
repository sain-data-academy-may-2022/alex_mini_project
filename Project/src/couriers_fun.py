#imports
import json

#creates and returns a new courier dictionary
def hire_courier():
    courier = {}
    courier['name'] = input('enter courier name: ')
    courier['open_orders'] = 0
    print(courier)
    return courier

#updates the couriers.json file with the provided dictionary
def push_couriers(couriers):
    file_name = 'couriers.json'
    try:
        with open(file_name, 'w') as file:
            new = json.dumps(couriers, indent='    ')
            file.write(new)
    except:
        print('unable to create / find', file_name)
        input('enter to continue : ')

#populates a dictionary with the contents of couriers.json
def pull_couriers():
    file_name = 'couriers.json'
    try:
        with open(file_name) as file:
            couriers = json.load(file)
    except:
        print(file_name, 'not found, new file will be created')
    return couriers

# returns the name of the courier with the least orders
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

#prints the contents of the provided dictionary somewhat neatly
def print_couriers(couriers):
    for key, value in couriers.items():
        if type(value) == dict:
            print(key)
            print_couriers(value)
        else:
            print(key,' : ',value)