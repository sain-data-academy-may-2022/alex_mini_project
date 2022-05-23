import os

print("why are you running my_functions.py ? it dont do nuffin'")


def print_list(my_list):  # prints a list with indexes
    clear_term()
    index = 0
    for x in my_list:
        print(index, x)
        index += 1


def clear_term():  # clears the terminal
    os.system('clear')


def get_product_choice(list):  # lindas
    print_list(list)
    while True:
        try:
            which_item = int(input('Please select item: '))
            if which_item < 0 or which_item >= len(list):
                print('Please select a valid number')
            else:
                return which_item
        except ValueError:
            print('Please write a number')


def remove_item(list):  # lindas
    num = get_product_choice(list)
    del list[num]
