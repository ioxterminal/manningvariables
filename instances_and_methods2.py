class Price:
    def __init__(self, part_number, price):
        self.price = price
        self.part_number = part_number

    def get_price(self):
        return  self.price

item_price = Price

print(dir(Price))
print(Price.__dict__ )

def set_discount(item_price, percent_off):
    item_price.percent_off = percent_off


def get_discount_price(item_price):
    return item_price.price - (item_price.price * item_price.percent_off)