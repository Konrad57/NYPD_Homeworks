# Hello World exercise
import math

print("Hello World!")

# Greeting exercise
print("The greeting program v. 1.0")
name = input("Enter your name: ")
print("Hi " + name + "!")

# Quadratic equation exercise
print("The quadratic equation solver (ver. 1.0).")
a = int(input("Enter the quadratic coefficient: "))
b = int(input("Enter the linear coefficient: "))
c = int(input("Enter the free term: "))

delta = b**2 - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"The equation has two roots: {x1}, {x2}")

elif delta == 0:
    x0 = -b / (2 * a)
    print(f"The equation has one root: {x0}")

elif delta < 0:
    print("The equation has no roots")

# Pizza order exercise
print("Pizzarino Ltd. The best pizza deliveries in this century and galaxy!")

# Below first try, I wanted to do it somehow faster and shorter with usage of list and dict but couldn't make it work
'''
prices = {"sauce": 3, "onion": 4, "mushrooms": 5, "jalapenos": 6, "corns": 7, "olives": 8}

sauce = input("Do you want the (T)omato or (M)ayonnaise sauce? ")
onion = input("Do you want onion (Y/N)? ")
mushrooms = input("Do you want mushrooms (Y/N)? ")
jalapenos = input("Do you want jalapenos (Y/N)? ")
corn = input("Do you want corns (Y/N)? ")
olives = input("Do you want olives (Y/N)? ")


ingredients = [sauce, onion, mushrooms, jalapenos, corn, olives]
order = []
price = 0
for ingredient in ingredients:
    if ingredient == "Y" or ingredient == "T" or ingredient == "M":
        order.append(ingredient)
        price += prices[ingredient]

print(f"You have ordered a pizza with: {order}. The price is ${price}")
'''
# This one is working though feels a bit too long and cumbersome

tomato_sauce_price = 1.5
mayonnaise_sauce_price = 2.0

onion_price = 1.0
mushrooms_price = 1.5
jalapenos_price = 2.0
corn_price = 1.0
black_olive_price = 1.0

sauce_choice = input("Do you want the (T)omato or (M)ayonnaise sauce? ")
if sauce_choice.upper() == 'T':
    sauce = "tomato sauce"
    sauce_price = tomato_sauce_price
else:
    sauce = "mayonnaise sauce"
    sauce_price = mayonnaise_sauce_price

onion = input("Do you want onion (Y/N)? ")
mushrooms = input("Do you want mushrooms (Y/N)? ")
jalapenos = input("Do you want jalapenos (Y/N)? ")
corn = input("Do you want corn (Y/N)? ")
black_olive = input("Do you want black olive (Y/N)? ")

total_price = sauce_price
topping_list = []

if onion.upper() == 'Y':
    topping_list.append("onion")
    total_price += onion_price
if mushrooms.upper() == 'Y':
    topping_list.append("mushrooms")
    total_price += mushrooms_price
if jalapenos.upper() == 'Y':
    topping_list.append("jalapenos")
    total_price += jalapenos_price
if corn.upper() == 'Y':
    topping_list.append("corn")
    total_price += corn_price
if black_olive.upper() == 'Y':
    topping_list.append("black olive")
    total_price += black_olive_price

topping_description = ', '.join(topping_list)
print(f"You have ordered a pizza with: {sauce}, {topping_description}. The price is ${total_price}.")