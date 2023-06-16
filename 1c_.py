class Item:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def _repr__(self):
        return self.brand

item_list = [
    Item(1000, 'Apple'),
    Item(1200, 'Apple'),
    Item(900, 'Samsung'),
    Item(700, 'Samsung'),
    Item(660, 'Xiaomi'),
]

new_list = list(filter(lambda item: item('brand') == 'Apple', item_list))
print(new_list)