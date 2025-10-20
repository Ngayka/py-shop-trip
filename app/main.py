import json
from customer import Customer
from car import Car
from shop import Shop


def shop_trip():
    with open('shop.json', 'r', encoding="utf-8") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    shops = [Shop(shop["products"], shop["location"], shop["name"])
            for shop in data["shops"]]

    customers = []
    for c in data["customers"]:
        car = Car(c["car"]["brand"], c["car"]["fuel_consumption"])
        customer = Customer(c["name"], c["product_cart"], c["location"], c["money"], car)
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            total_cost = customer.count_total_trip_cost(shop, fuel_price)
            print(f"{customer.name}`s trip to the {shop.name} costs {total_cost:.2f}")

        cheapest_shop = None
        cheapest_cost = None

        for shop in shops:
            total_cost = customer.calculate_fuel_cost(shop, fuel_price)
            if total_cost is None:
                continue

            if cheapest_cost is None or total_cost < cheapest_cost:
                cheapest_shop = shop
                cheapest_cost = total_cost

        if cheapest_shop and customer.money >= cheapest_cost:

            print(f"{customer.name} rides to the {cheapest_shop.name}")
            customer.buy_products(cheapest_shop)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
