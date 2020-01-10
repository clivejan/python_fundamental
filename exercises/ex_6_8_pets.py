doggy = {'type': 'tiger', 'owner': 'clive'}
catty = {'type': 'lion', 'owner': 'carrie'}
jaguar = {'type': 'panther', 'owner': 'tzuyu'}

pets = [doggy, catty, jaguar]

for pet in pets:
	print(f"{pet['owner'].title()} has a {pet['type']} as a pet.")
