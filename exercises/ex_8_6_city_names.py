def city_country(city, country):
	"""Return a foratted string"""
	return f'"{city.title()}, {country.title()}"'

print(city_country('Toronto', 'Canada'))
print(city_country('Montreal', 'Canada'))
print(city_country('Taipei', 'Taiwan'))
