usernames = ['tzuyu', 'jennie', 'clive', 'irene', 'yuna']

for username in usernames:
	if username.lower() == 'clive':
		print(f"Hello {username.title()}, would you like to see a status report?")
	else:
		print(f"Hello {username.title()}, thank you for logging in again.")
