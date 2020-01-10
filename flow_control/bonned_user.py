bonned_users = ['andrew', 'carolina', 'david']

# checking whether a value in a list
name = 'david'
if name in bonned_users:
	print(f'Oops! {name.title()}, you got some troubles.')

# checknig whether a value is not ib a list
name = 'clive'
if name not in bonned_users:
	print(f'Hi, {name}. Welcome back.')
