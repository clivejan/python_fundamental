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

# using dictionary.keys() as a normal list
if 'erin' not in favourite_languages.keys():
	print(f"\nErin, please take our poll!")

# looping through a dictionary's keys in a particular order
for name in sorted(favourite_languages.keys()):
	print(f"{name.title()}, thank you gor taking the poll.")
print()

# looging through all values in a dictionary
print("The fllowing languages have been mentioned:")
for language in favourite_languages.values():
	print(language.title())
