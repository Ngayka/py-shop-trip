import math


class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to(self, location):
        """count distance between customer and location"""
        return math.sqrt((self.location[0] - location[0]) ** 2 +
                         (self.location[1] - location[1]) ** 2)

    def count_total_trip_cost(self, shop, fuel_price):
        """count total trip cost"""
        distance = self.distance_to(shop.location)
        trip_cost = 2 * self.car.calculate_fuel_cost(distance, fuel_price)
        product_cost = shop.calculate_products_cost(self.product_cart)
        if product_cost is None:
            return None
        return trip_cost + product_cost

    def buy_products(self, shop):
        return shop.print_receipt(self)
