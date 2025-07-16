
print("Welcome to Python Pizza Delivery")
size = input("What size of pizza you would like to order; S,M or L ")
topping = input("Would you like some toppings? y or n :")
extra_cheese = input(" Do you want extra cheese? y or n :")

Pizza_prize = 0

if size == "S" or size== "s":
    Pizza_prize += 15
elif size == "M" or size== "m":
    Pizza_prize += 20
elif size == "L" or size== "l":
    Pizza_prize += 25

if topping == "Y" or topping == "y":
    topping_size = input(print("What size of topping you would like to order; S,M or L"))
    if topping_size == "S" or topping_size== "s":
        Pizza_prize += 1
    elif topping_size == "M" or topping_size== "m":
        Pizza_prize += 3
    elif topping_size == "L" or topping_size== "l":
        Pizza_prize += 3

if extra_cheese== "Y" or extra_cheese=="y":
    Pizza_prize += 1

print(Pizza_prize)
