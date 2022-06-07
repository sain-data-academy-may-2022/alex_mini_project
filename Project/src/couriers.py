class Courier:
    def __init__(self,name: str,drivers: int,contact: int):
        self.name = name
        self.drivers = drivers
        self.contact = contact #447860251308
    
    def get_name(self):
        return self.name

class Driver:
    def __init__(self,name,wage,phone):
        self.name = name
        self.wage = wage
        self.phone = phone

