motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

# Modifing elements in a list
motocycles[0] = 'ducati'
print(motocycles)

# Appending elements to the end of list
motocycles.append('honda')
print(motocycles)

# Inserting elements into a list
motocycles.insert(0, 'sym')
print(motocycles)

# Removing an item from list by its index
del motocycles[0]
print(motocycles)

# Removing an item from the end of a list and reusing the value
popped_motocycle = motocycles.pop()
print(motocycles)
print(popped_motocycle)
