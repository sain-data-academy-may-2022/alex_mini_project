import os

print("why are you running my_functions.py ? it dont do nuffin'")

def print_list(my_list): #prints a list with indexes
    clear_term()
    index = 0
    for x in my_list:
        print(index, x)
        index += 1

def clear_term(): #clears the terminal
    os.system('clear')

def option_3(product_list):
    print_list(product_list)#prints product list, along with index ids
    entry = input('please enter the id or name of the item you wish to update ')
    list_id = list_int_check(product_list,entry)
    return list_id

def option_4(product_list):
    print_list(product_list) #prints product list along with index ids
    entry = input("please enter the id or name of the item you wish to delete ")
    list_id = list_str_check(product_list, entry) #function allows both text and numbers to be accepted, returns appropriate index (different text output)
    return list_id

def list_int_check(product_list,list_id):#returns an int
    if list_id.strip().isdigit(): #if input is a number convert to int
        list_id = int(list_id)
        
        if list_id<len(product_list):
            return list_id

        else:
            input("\nno product at index\n")
            return None 
    
    elif list_id in product_list:
        list_id = int(product_list.index(list_id)) #if it is a string, check the index location if it has one and store it           
        return list_id    
    
    else:
        input("\nno such entry exists\n")
        return None

def list_str_check(product_list,list_id): #returns a string
    #list_id = input("please enter the id or name of the item you wish to delete ")
    if list_id.strip().isdigit():
        list_id = int(list_id)
        
        if list_id<len(product_list):
            return product_list[list_id]

        else:
            input('\nno product at index\n')
            return None
    
    elif list_id in product_list:
        return list_id
    
    else:
        input("\nno such entry exists, sorry\n")
        return None

def order_status():
    new_value = ''
    print('d = delivered\nt = in-transit\np = pending\nc = cooking')
    update = input('please enter the new status : ')
    while True:
        if update == 'c' or update == 'cooking': #if characters match, update to appropriate order status
            new_value = 'cooking'
            return new_value
        
        elif update == 't' or update == 'in-transit':
            new_value = 'in-transit'
            return new_value
        
        elif update == 'd' or update == 'delivered':
            new_value = 'delivered'
            return new_value
        
        elif update == 'p' or update == 'pending':
            new_value = 'pending'
            return new_value
        
        else:
            print('invalid entry')

def order_amend(order,product_list):
    data = input('ammending user data y/n? : ')
    if data == 'y' or data =='Y': #accepts both capitals and text
        
        for key,value in order['user_data'].items(): #runs through each item in the dictionary
            if key == 'order_status': #skips the order status as that needs to be changed separately
                    continue
            
            print(key,value,'enter ammendment or enter to skip : ')
            change = input()
            
            if change == '':#if they just use enter, they do not update the entry
                continue
            else:
                order['user_data'][key] = change #updates entry in passed dictionary
    
    items = input('ammending food and drink y/n : ')
    if items == 'y' or items == 'Y':
        index = 0
        for key,value in order['items'].items():
            while True: #loop used to make sure they can only enter items on the menu
                print(product_list[index])
                print(key,value,'enter ammendment or enter to skip : ')
                change = input()
                if change == '':
                    index +=1
                    continue
                else:
                    if change in product_list[index]: #if item is in the menu then great!, else try again
                        order['items'][key] = change
                        index +=1
                        break
                    else:
                        input('item not on menu, enter to try again : ')
                        continue
            
    return order #returns the dictionary passed in, but updated with new info

def old_order_amend(product_list): #old and messy. no need to use!
    key_dex =[['0','user_data'],['1','items']]
    key = ''
    subkey_dex = [[['0','1','2','3'],['name','address','post_code','phone_number']],[['0','1'],['food','drink']]]
    subkey = ''
    change = ''
        
    while True:
        print('0 - user_data\n1 - items')
        key = input('what are you changing? : ')
        
        if key in key_dex[0] :
            if key == '0':
                key = key_dex[0][1] 
            
            while True:
                print('0 - name\n1 - address\n2 - post_code\n3 - phone_number')
                subkey = input('what are you changing? : ')
                
                if subkey in subkey_dex[0][0] or subkey in subkey_dex[0][1]:
                    if subkey in subkey_dex[0][0]:
                        subkey = str(subkey_dex[0][1][int(subkey.strip())])
                    
                    change = input('please input your change : ')
                    return_list = [key,subkey,change]
                    return return_list
                
                else:
                    input('invalid entry, try again.\n enter to continue : ')
                    continue

        elif key in key_dex[1]:
            if key == '1':
                key = key_dex[1][1]

            while True:
                print('0 - food\n1 - drink')
                subkey = input('what are you changing? : ')

                if subkey in subkey_dex[1][0] or subkey in subkey_dex[1][1]:
                    if subkey in subkey_dex[1][0]:
                        subkey = str(subkey_dex[1][1][int(subkey.strip())])
                    
                    while True:
                        change = input('please input your change : ')
                        
                        if subkey == 'food' and change in product_list[0]:
                            break
                        
                        elif subkey == 'drink' and change in product_list[1]:
                            break
                        
                        else:
                            input('item not on menu, please enter again. enter to continue : ')
                    return_list = [key,subkey,change]
                    return return_list
                
                else:
                    input('invalid entry, try again.\n enter to continue : ')

        else:
            input('invalid entry, try again.\n enter to continue : ')
            continue

def get_product_choice(list): #lindas
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

def remove_item(list): #lindas
    num = get_product_choice(list)
    del list[num]

def create_order(product_list):
    #order form is used as a template to itterate through when adding the info
    order_form = { 
    'user_data': { 
        'name' : 'None', 'address' : 'None', 'post_code' : 'None', 
        'phone_number' : 'None' , 'order_status' : 'None' },
    'items' : { 
        'food' : 'None', 'drink' : 'None'}
    }  
    for key in order_form['user_data'].keys(): #loops through all of the keys in the info part of the dictionary
                            
        if key == 'order_status': #sets status to pending for uniformality 
            order_form['user_data'][key] = 'pending' 
            continue
        
        order_form['user_data'][key] = input(f'please enter User {key} : ') #user can enter all info manually for dictionary values

    for index in product_list:
        print_list(product_list) #prints the product lists

    index = 0                        
    for key in order_form['items'].keys(): #loops through all keys in the items part of the dictionary
        correct = False
        
        while correct == False:
            meal = input(f'please enter customers {key} item : ')
            if meal in product_list[index]:
                order_form['items'][key] = meal
                index +=1
                correct = True
            else:
                input('please enter a valid input. enter to continue : ')


    return order_form