# goods = [
#     {
#         'name': 'Iphone 7',
#         'brand': 'Apple',
#         'price': 100,
#     },
#     {
#         'name': 'Ipad',
#         'brand': 'Apple',
#         'price': 50,
#     },
#     {
#         'name': 'Windows XP',
#         'brand': 'Microsoft',
#         'price': 150,
#     }
# ]


# if __name__ == "__main__":
#     def on_price(item):
#         return item['price']


#     print(sorted(goods, key=lambda item: item['price']))

#     filtered_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
#     print(filtered_list)

#     numbers = ['1', '2', '3', '4', '5']
#     print(numbers)
#     result = list(map(int, numbers))
#     print(result)

#     names_list = ['Igor', 'Артем', 'Аня', 'Ксюша', 'Елена']
#     surnames = ['Иванов', 'Петрович', 'Максимовна', 'Андреевна']

#     persons = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames))
#     print(persons)

#     new_goods = []

#     for index, item in enumerate(goods):
#         print(index)
#         new_goods.append({index: item})

#     print(new_goods)

#     names_list = ['Igor', 'Артем', 'Аня', 'Ксюша', 'Елена']
#     surnames = ['Иванов', 'Петрович', 'Максимовна', 'Андреевна']

#     for name, surname in zip(names_list, surnames):
#         print(name, surname)
# else:
#     print("Скрипт запустился извне")










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

new_list = (filter(lambda item: Item('brand') == 'Apple', item_list))
new_list = list(new_list)
print(new_list)

