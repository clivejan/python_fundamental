cities = {
	'toronto':{
		'country': 'canada',
		'population': 2_930_000,
		'fact': 'Toronto is the provincial capital of Ontario.',
	},
	'vancouver':{
		'country': 'canada',
		'population': 675_200,
		'fact': 'Vancouver is a coastal seaport city in western Canada.',
	},
	'montreal':{
		'country': 'canada',
		'population': 1_780_000,
		'fact': 'Montreal is the most populous municipality '\
		'in the Canadian province of Quebec.',
	},
}

for city, city_info in cities.items():
	print(f"\nAbout {city.title()}:")
	print(f"\tCountry: {city_info['country']}")
	print(f"\tPopulation: {city_info['population']}")
	print(f"\tFact: {city_info['fact']}")

