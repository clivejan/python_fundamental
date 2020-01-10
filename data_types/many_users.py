users = {
	'clive': {
		'first': 'chihwei',
		'last': 'chan',
		'location': 'montreal',
	},
	'carrie': {
		'first': 'naiwen',
		'last': 'ku',
		'location': 'taipei',
	},
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	
	fullname = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull name: {fullname.title()}")
	print(f"\tLocation: {location.title()}")
