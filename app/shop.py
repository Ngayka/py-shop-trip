from datetime import datetime

from app import customer


class Shop:
    def __init__(self, products, name, location):
        self.products = products
        self.name = name
        self.location = location


    def calculate_products_cost(self, product_cart):
        total = 0
        for product, quantity in product_cart.items():
            if product not in self.products:
                return None
            total += quantity * self.products[product]
        return total

    def print_recept(self):
        print(f"\nDate: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks {customer.name} for your purchase!")
        print(f"You have bought:")
        total = 0
        for product, quantity in self.products.items():
            price = self.products[product]
            cost = price * quantity
            total += cost
        print(f"{quantity} {product}s cost {cost} dollars")
        print(f"Total cost is {total} dollars")
        print("\nSee you again!")
