favourite_places = {
	'clive': ['toronto', 'vancouver', 'montreal'],
	'carrie': ['toronto', 'niagara', 'quebec city'],
	'tzuyu': ['seuol', 'tokyo', 'tainan'],
}

for name, cities in favourite_places.items():
	print(f"\n{name.title()}'s favourite cites are:")
	for city in cities:
		print(f"\t{city}")
