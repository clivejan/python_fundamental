favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phli': 'python',
}

#language = favourite_languages['sarah'].title()
#print(f"Sarah's favourite language is {language}.")

# looping through a dictionary by items()
for name, language in favourite_languages.items():
	print(f"{name.title()}'s favourite language is {language}.")
print()

# looping through all the keys in a dictionary
friends = ['phli', 'sarah']
for name in favourite_languages.keys():
	print(name.title())

	if name in friends:
		language = favourite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}.")
