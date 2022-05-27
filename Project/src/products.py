class Products:
    def __init__(self,name: str,price: float, is_vegan: bool):
        self.name = name
        self.is_vegan = is_vegan
        self.price = price
    
    def print_self(self):
        print(self.name,':',self.price)
    
    def rename(self,new_name : str):
        self.name = new_name
    
    def update_price(self,new_price : float):
        self.price = new_price

