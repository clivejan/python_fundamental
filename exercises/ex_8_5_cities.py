def describe_city(city, country='Canada'):
	"""Describe a city belong to which country"""
	print(f"{city.title()} is in {country.title()}")

describe_city('Toronto')
describe_city(city='Montreal')
describe_city('Taipei', 'Taiwan')
