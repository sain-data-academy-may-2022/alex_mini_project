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
