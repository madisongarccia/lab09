class Product:

    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    def discount_price(self, discount_percent):
        new_price = self.product_price * (1- 0.01*discount_percent)
        return round(new_price, 2)
    
    def change_price(self, new):
        self.product_price = new

item = Product(1223, "milk", 2.7)
item.change_price(6)
print(item.product_price)
print(item.discount_price(35))
