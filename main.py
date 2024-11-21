#1. define your function
def pizza_price():
  
  #2. Ask customer what they want
  requested_topping = input("""
  Write your customer prompt here
  """)
  requested_topping = requested toppings.upper()
  print("You requested: {requested_topping}")

base_price = 15
topping_price = 0
caculated_toppings = []

for topping in requested_toppings:

  # Skip toppings we've already caculated
  if topping in caculated_toppings:
    continue

  if topping == "T":
    topping_price += 1.5
    
  if topping == "O":
    topping_price += 1.25

  if topping == "P":
    topping_price += 3.5

  if topping == "M":
    topping_price += 3.75

  if topping == "A":
    topping_price += .40

  # Add topping to caculated list
  caculated_toppings += topping

 total_price = base_price + topping_price

 if total_price > 20:
   total_price = total_price * .95

 total_price = round(total_price, 2)

 print(total_price)

pizza_price()

