bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accesing Elements in a list
print(bicycles[0])
print(bicycles[0].title())

# Index Position Start at 0, Not 1
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)