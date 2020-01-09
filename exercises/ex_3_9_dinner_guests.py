guests = ['David', 'Jeff', 'Mary']

for guest in guests:
	print(f"Hi {guest}, I would like to invite you to dinner.")

print(f"{guests[0]} cannot make the dinner.")

guests[0] = 'Carrie'

for guest in guests:
	print(f"Hi {guest}, I would like to invite you to dinner.")
	
print('I found a bigger table.')

guests.insert(0, 'Tzuyu')
guests.insert(2, 'Irene')
guests.append('Jennie')

for guest in guests:
	print(f"Hi {guest}, I would like to invite you to dinner.")

print(f"There will be {len(guests)} at the dinner.")
