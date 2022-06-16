#imports
import my_functions 
#from getpass import getpass
#from logins import logins
exit = False
while exit == False:
    my_functions.clear_term()
    print('\nWelcome to the pop-up caf-app')
    print('Menu\n 1 - Food Menu\n 2 - Drinks Menu\n 3 - Snacks menu\n 4 - Order Menu\n 5 - couriers\n 0 - Exit Program')
    option = input('what option would you like? ')

    if option.strip().isdigit():
        option = int(option)

        if option == 0:  # exits the program
            my_functions.clear_term()
            print('Goodbye!')
            quit()

        elif option == 1:  # enters food menu
            my_functions.product_menu('food')            

        elif option == 2:  # enters drink menu
            my_functions.product_menu('drinks')

        elif option == 3: # enters snacks menu
            my_functions.product_menu('snack') #can make return bool (true) if list updated to improve performance ?)

        elif option == 4:  # enters orders menu
            my_functions.orders_menu()

        elif option == 5: # enters couriers menu
            my_functions.courier_menu()
    else:
        input("\nincorrect input, please try again.\n")
