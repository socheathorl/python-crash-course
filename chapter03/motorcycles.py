motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modifying element
motorcycles[0] = 'ducati'
print(motorcycles)

# adding element
motorcycles.append('toyota')
print(motorcycles)

# insert element
motorcycles.insert(0, 'hyundai')
print(motorcycles)

# remove element
del motorcycles[2]
print(motorcycles)

# remove element using pop

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# remove item by value
motorcycles.remove('ducati')
print(motorcycles)