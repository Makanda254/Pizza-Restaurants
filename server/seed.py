from app import app, db
from models import Restaurant, Pizza, RestaurantPizza
import random

with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    print("🍕 Seeding restaurants...")

    restaurants_data = [
        {"name": "Pizza Palace", "address": "123 Main St, Cityville"},
        {"name": "Mamma Mia Pizzeria", "address": "456 Oak St, Townsville"},
        {"name": "Cheesy Bites", "address": "789 Pine St, Villagetown"},
        {"name": "Slice Haven", "address": "101 Elm St, Hamletville"},
        {"name": "Crust Kingdom", "address": "202 Maple St, Boroughburg"},
        {"name": "Pizzarino", "address": "303 Cedar St, Village Springs"},
        {"name": "Pepperoni Paradise", "address": "404 Birch St, Orchard City"},
        {"name": "Dough Delight", "address": "505 Pine St, Town Haven"},
        {"name": "Tomato Topia", "address": "606 Oak St, Groveburg"},
        {"name": "Kempinski Villa Rosa", "address":"402 Waiyaki Way, Nairobi"}
    ]

    for data in restaurants_data:
        restaurant = Restaurant(**data)
        db.session.add(restaurant)

    db.session.commit()

    print("🍕 Seeding pizzas...")

    pizzas_data = [
        {"name": "Margherita", "ingredients": "Tomato Sauce, Mozzarella, Basil"},
        {"name": "Pepperoni", "ingredients": "Tomato Sauce, Mozzarella, Pepperoni"},
        {"name": "Vegetarian", "ingredients": "Tomato Sauce, Mozzarella, Bell Peppers, Mushrooms, Onions"},
        {"name": "Hawaiian", "ingredients": "Tomato Sauce, Mozzarella, Ham, Pineapple"},
        {"name": "BBQ Chicken", "ingredients": "BBQ Sauce, Mozzarella, Grilled Chicken, Red Onion"},
    ]

    for data in pizzas_data:
        pizza = Pizza(**data)
        db.session.add(pizza)

    db.session.commit()

    print("🍕 Adding pizzas to restaurants...")

    prices = [10, 12, 14, 16, 24, 13, 5, 16, 3, 20]

    restaurants = Restaurant.query.all()
    pizzas = Pizza.query.all()

    for restaurant in restaurants:
          for _ in range(random.randint(1, 4)):
            pizza = random.choice(pizzas)
            price = random.choice(prices)

            restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza.id, restaurant_id=restaurant.id)
            db.session.add(restaurant_pizza)
            

    db.session.commit()

    print("🍕 Done seeding!")
