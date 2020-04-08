class Product:
    # Class or static attributes
    taxrate = 18

    @staticmethod
    def change_taxrate(newtaxrate):
        Product.taxrate = newtaxrate

    @classmethod
    def dummy(cls):
        return cls(0, "", 0)

    def __init__(self, id, name, price):
        # Object attributes
        self.id = id
        self.name = name
        if price < 0:
            raise ValueError('Invalid Price ' + str(price))

        self.price = price

    def __str__(self):
        return f"{self.id} - {self.name} - {self.price}"

    def net_price(self):
        return self.price + self.price * Product.taxrate / 100

    def change_price(self, price):
        if price >= 0:
            self.price = price
        else:
            print("Invalid Price")


p1 = Product(1, "Abc", -1000)

p = Product.dummy()
print(p)

Product.change_taxrate(20)  # Call static method

p1 = Product(1, "Abc", 30000)
p1.change_price(10000)
print(p1)
print("Net price : ", p1.net_price())
