def city_country(city, country, population=''):
	"""Return a formatted city country string"""
	if population:
		well_formatted = f"{city.title()}, {country.title()} - population {population}."
	else:
		well_formatted = f"{city.title()}, {country.title()}"
	return well_formatted
