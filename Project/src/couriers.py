class Courier:
    def __init__(self,name: str,drivers: int):
        self.name = name
        self.drivers = drivers
    
    def get_name(self):
        return self.name

class Driver:
    def __init__(self,name,wage):
        self.name = name
        self.wage = wage

