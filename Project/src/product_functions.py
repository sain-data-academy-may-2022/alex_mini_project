import my_functions

def duplicate_check(my_list,check):
    for ind in my_list:
        if type(ind) == list:
            if duplicate_check(my_list[my_list.index(ind)],check) == True:
                return True   
    if check in my_list:
        return True
    else:
        return False

def option_3(product_list):
    my_functions.print_list(product_list)  # prints product list, along with index ids
    entry = input(
        'please enter the id or name of the item you wish to update ')
    list_id = list_int_check(product_list, entry)
    return list_id


def option_4(product_list):
    my_functions.print_list(product_list)  # prints product list along with index ids
    entry = input("please enter the id or name of the item you wish to delete ")
    # function allows both text and numbers to be accepted, returns appropriate index (different text output)
    list_id = list_str_check(product_list, entry)
    return list_id

#returns the in index from a list, takes both string and int as input
def list_int_check(product_list, list_id):
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

