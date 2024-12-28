motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = popped_motorcycle
print("The last motorcycles I owned was a " + last_owned.title() + ".")