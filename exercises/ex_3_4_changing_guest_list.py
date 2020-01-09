guests = ['David', 'Jeff', 'Mary']

for guest in guests:
	print(f"Hi {guest}, I would like to invite you to dinner.")

print(f"{guests[0]} can not make the dinner.")

guests[0] = 'Carrie'

for guest in guests:
	print(f"Hi {guest}, I would like to invite you to dinner.")
	