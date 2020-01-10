clive = {'first_name': 'chihwei', 'last_name': 'chan',
	'age': 40, 'city': 'montreal',}
carrie = {'first_name': 'naiwen', 'last_name': 'ku',
	'age': 33, 'city': 'taipei',}
tzuyu = {'first_name': 'tzuyu', 'last_name': 'chou',
	'age': 20, 'city': 'seuol',}

people = [clive, carrie, tzuyu]

for person in people:
	full_name = f"{person['first_name']} {person['last_name']}"
	print(f"\nFull Name: {full_name.title()}")
	print(f"\tAge: {person['age']}")
	print(f"\tCity: {person['city'].title()}")
