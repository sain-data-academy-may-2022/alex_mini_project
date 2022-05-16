import os

print("why are you running my_functions.py ? it dont do nuffin'")
print("git test")
def print_list(my_list):
    clear_term()
    index = 0
    for x in my_list:
        print(index, x)
        index += 1

def clear_term():
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