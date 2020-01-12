import json

def get_stroed_username(filename):
	"""Get storted username if available"""
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username(filename):
	"""Prompt for a new username"""
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def verify_user(filename ,username):
	saved_user = get_stroed_username(filename)
	if saved_user == username:
		return True
	return False

def greet_user(filename, username):
	"""Great the user by name"""
	if verify_user(filename, username):
		print(f"Welcome back, {username}.")
	else:
		username = get_new_username(filename)
		print(f"We'll remember you when you come back, {username}!")

filename = 'ex_10_13_verify_user.json'
username = input("What is your name? ")
greet_user(filename, username)
