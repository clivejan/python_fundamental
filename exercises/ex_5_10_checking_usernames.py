current_users = ['tzuyu', 'jennie', 'clive', 'irene', 'yuna']
new_users = ['nayeon', 'jisoo', 'clive', 'joy', 'wonyoung']

# make sure current users in list are all lower letters
for i in range(len(current_users)):
	 current_users[i] = current_users[i].lower()

# checking whether the new username is available
for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"Opps! {new_user.title()}, ask to your parent to give you a new name.")
	else:
		print(f"Hi {new_user.title()}, welcome.")
