import couriers


class Order:
    def __init__(self, order: dict) -> None:
        self.name = order['user_data']['name']
        self.address = order['user_data']['address']
        self.post_code = order['user_data']['post_code']
        self.phone_number = order['user_data']['phone_number']
        self.status = order['user_data']['order_status']
        self.courier = order['user_data']['courier']
        self.items: dict = order['items']

    def update_order():
        pass

    def print_order(self):
        print('\nname         :', self.name,'\naddress      : ', self.address,'\npost code    : ', self.post_code,
              '\nphone number : ', self.phone_number,'\ncourier      : ', self.courier,'\nstatus       : ', self.status)
        print('\nfood         : ', self.items['food'],'\ndrink        : ',self.items['drink'], 
              '\nsnack        : ', self.items['snack'])
        pass

    def convert_to_dict(self) -> dict:
        user = {'name': self.name, 'address': self.address, 'post_code': self.post_code,
                'phone_number': self.phone_number, 'courier': self.courier, 'order_status': self.status}
        my_order = {'user_data': user, 'items': self.items}
        print(my_order)
        return my_order
