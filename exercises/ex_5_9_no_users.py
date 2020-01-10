usernames = []

if usernames:
	for username in usernames:
		if username.lower() == 'clive':
			print(f"Hello {username.title()}, would you like to see a status report?")
		else:
			print(f"Hello {username.title()}, thank you for logging in again.")
else:
	print("It's a tragedy. There has no any user.")
