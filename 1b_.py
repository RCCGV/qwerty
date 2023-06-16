class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        
    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other
    
    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            self.price - other
            
    def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, int):
            self.price * other

    def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, int):
            self.price * other
            
    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.price / other.price
        elif isinstance(other, int):
            self.price / other

item1 = Item('i7 9900k', 10000, 0.12)
item2 = Item('DDR4 3600MHZ KINGSTONE', 8000, 0.15)

print(f'Сумма {item1 + item2}')
print(f'Разность {item1 - item2}')
print(f'Умножение {item1 * item2}')
print(f'Деление {item1 / item2}')



# class MathOperations: 
#     def __init__(self, x, y): 
#         self.x = x 
#         self.y = y 
 
#     def __add__(self, other): 
#         return self.x + other.y 
 
#     def __sub__(self, other): 
#         return self.x - other.y 
 
#     def __mul__(self, other): 
#         return self.x * other.y 
 
#     def __truediv__(self, other):  
#         return self.x / other.y 
 
# # Example usage 
# a = MathOperations(10, 5) 
# b = MathOperations(5, 2) 
 
# print(a + b) 
# print(a - b) 
# print(a * b) 
# print(a / b)