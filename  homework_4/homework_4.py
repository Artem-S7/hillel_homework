class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

class Order:
    def __init__(self):
        self.products = []
        self.total = 0

    def add_product(self, product):
        self.products.append(product)
    def calculate_total(self):
        self.total = 0
        for product in self.products:
            self.total += product.price
            return self.total

class Inventory:
    def __init__(self):
         self.stock = {}
    def add_product(self, product, quantity):
        self.stock[product.name] = quantity
    def change_quantity(self, product, new_quantity):
        self.stock[product.name] = new_quantity
inventory = Inventory()
customers = []

shop = open('shopstore.txt', encoding='utf-8').read().splitlines()

for line in shop:
    data = line.split(';')

    if data[0] == 'PRODUCT':
        product = Product(data[1], data[2], int(data[3]))
        inventory.add_product(product, int(data[4]))

    elif data[0] == 'CUSTOMER':
        customer = Customer(data[1], data[2])
        customers.append(customer)

print(inventory.stock)
for customer in customers:
    print(customer.name, customer.email)
order = Order()
order.add_product(product)
customer.add_order(order)
print('Сума замовлення:', order.calculate_total())