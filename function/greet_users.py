def greet_users(names):
	"""print a simple greeting to each user in the list"""
	for name in names:
		print(f"Hello, {name.title()}!")

usernames = ['clive', 'carrie', 'tzuyu']
greet_users(usernames)
