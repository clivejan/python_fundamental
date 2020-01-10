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
