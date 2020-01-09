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

print("The table is missing. I only have a banch.")

while len(guests) > 2:
	byebye = guests.pop()
	print(f"Hi {byebye}, I cannot afford your appetite. See you next time.")

for guest in guests:
	print(f"Hi {guest}, I would like to invite you to dinner.")
