favourite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phli': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
	if len(languages) > 1:
		print(f"\n{name.title()}'s favourite languages are:")
	elif len(languages) == 1:
		print(f"\n{name.title()}'s favourite languages is:")
	for language in languages:
		print(f"\t{language.title()}")
