# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#   print("Hold the anchovies!")

# requested_toppins = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppins:
#   print("Adding mushrooms.")
# if 'pepperoni' in requested_toppins:
#   print("Adding peperoni.")
# if 'extra cheese' in requested_toppins:
#   print("Adding extra cheese.")

# print("\nFinished marking your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
  if requested_topping == 'green peppers':
    print("Sorry, we are out of green peppers right now.")
  else:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")