cars = ['bmw', 'audi', 'toyota', 'subaru']

# sorting a list permanently
cars.sort()
print(cars)

# sorting a list in reverse alphabetocal order permanently
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)
