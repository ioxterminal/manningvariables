class Price:
    def __init__(self, part_number, price):
        self.price = price
        self.part_number = part_number

    def get_price(self):
        return  self.price

Cola = Price(815,15)
print(Cola.get_price())
print(type(Cola))

def func__init__(self, part_number, price):
    self.price = price
    self.part_number = part_number
    
def func_get_price(self):
    return  self.price