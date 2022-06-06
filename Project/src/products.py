class Products:
    def __init__(self,name: str,price: float, is_vegan: bool):
        self.name = name
        self.is_vegan = is_vegan
        self.price = price
    
    def print_self(self):
        if self.is_vegan:
            print(self.name,':',self.price,'Vegan')
        else:
            print(self.name,':',self.price)

    def get_self(self):
        return{'name':self.name,'price':self.price,'vegan':self.is_vegan}
    
    def rename(self,new_name : str):
        self.name = new_name
    
    def update_price(self,new_price : float):
        self.price = new_price

