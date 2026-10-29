'''
Design and create an online Store for Products (name, price).
Track total products being created.
Create a static method to calculate discount on each product based on a percent parameter.
'''

class Product:
    count = 0
        
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
        
    @classmethod
    def get_count(cls):
        print(f"No of products are {cls.count}")
        
    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price is {price - (price * discount / 100)}")
        
        
s1 = Product("Iphone 17 pro max", 1_50_000)
s2 = Product("Samsung galaxy S26 Ultra", 1_50_000)

Product.get_count()
s1.calc_discount(s1.price, 30)