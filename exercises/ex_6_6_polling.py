favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phli': 'python',
}

names = ['clive', 'sarah', 'david']

for name in names:
	if name in favourite_languages.keys():
		print(f"{name.title()}, thank you to response the poll.")
	else:
		print(f"Hi {name.title()}, please take the poll.")
