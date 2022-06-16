#import my_functions as mf
#import traceback
#import random
#impoort json
#import os
import product_functions as pf
#import order_functions as of
from decimal import Decimal
#import couriers_fun as cf
from db import db
#import orders
#import couriers


# how to create a view !!!!! - sql = 'create view orders_by_status as SELECT first_name, last_name, courier, status FROM orders ORDER BY status;'

#connect = db.establish()
# price = Decimal(1)
# id = 'food'
# mdict = {'name': 'eggs','price': price,'vegan': 0,'food_id':6}
# pf.push_updated_product(id,mdict)
#print(output)

prod = pf.pull_product_by_name('food','burger')
print(prod)
pf.push_updated_product('food',prod)


input()
#db.shut_down(connect)