import os
import product_functions
import order_functions
import couriers_fun

print("why are you running my_functions.py ? it dont do nuffin'")


def print_list(my_list):  # prints a list with indexes
    #clear_term()
    index = 0
    for x in my_list:
        print(index, x)
        index += 1

def clear_term():  # clears the terminal
    os.system('clear')

def product_menu(product_type):
    if product_type == 'food':
        version = 0
    elif product_type == 'drinks':
        version = 1
    elif product_type == 'snacks':
        version = 2
    else:
        return False
    menu = False
    product_list = product_functions.pull_produtcts()
    while menu == False:
        clear_term()
        print(
            'Food\n 1 - Product List\n 2 - Create Product\n 3 - Update Product\n 4 - Delete Product\n 0 - Return To Menu')
        sec_option = input('What option would you like? ')

        if sec_option.strip().isdigit():
            sec_option = int(sec_option)

            if sec_option == 0:  # return to main menu
                menu = True
                product_functions.push_products(product_list[0],product_list[1],product_list[2])
                continue

            elif sec_option == 1:
                print_list(product_list[version])
                input('press Enter to return to the menu')

            elif sec_option == 2:  # add item to list
                list_append = input(
                    'please enter the name of your new item ')

                if product_functions.duplicate_check(product_list,list_append):
                    input('item already on menu, press enter to continue')
                else:
                    product_list[version].append(list_append)

            elif sec_option == 3:  # update entry
                # takes input and checks it is in correct format, returns index
                list_id = product_functions.option_3(product_list[version])

                if list_id is None:  # if an invalid entry was given, return to menu
                    continue

                else:  # enter amendment at previously returned index
                    list_ammend = input('enter you ammendment here please ')
                    if product_functions.duplicate_check(product_list,list_ammend):
                        input('entry already exists. enter to continue : ')
                    else:
                        product_list[version][list_id] = list_ammend

            elif sec_option == 4:  # removing item from list
                list_id = product_functions.option_4(product_list[version])

                if list_id is None:  # if invalid entry was given, return to main menu
                    continue

                else:
                    # remove item at returned index
                    product_list[version].remove(list_id)

        else:
            continue

