import math
from datetime import datetime

from app import shop


class Customer:
    def __init__(self, name, products_to_buy, location, money, car):
        self.name = name
        self.products_to_buy = products_to_buy
        self.location = location
        self.money = money
        self.car = car

    def distance_to(self, shop_location):
        """count distance between customer and location"""
        return math.sqrt((shop_location[0] - shop_location[0] ** 2) +
                         (shop_location[1] - shop_location[1] ** 2))

    def count_total_trip_cost(self, shop, fuel_price):
        """count total trip cost"""
        distance = self.distance_to(shop.location)
        trip_cost = 2 * self.car.calculate_fuel_cost(fuel_price, distance)
        product_cost = shop.calculate_products_cost(self.product_cart)
        return trip_cost + product_cost

    def buy_products(self):
        return shop.print_recept(self)
