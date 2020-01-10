rivers = {
	'nile': 'Tanzania, Uganda, Rwanda, Burundi,' \
		'the Democratic Republic of the Congo, Kenya, Ethiopia, Eritrea,' \
		'South Sudan, Sudan and Egypt',
	'amazon': 'Brazil, Peru, Bolivia, Colombia, Ecuador,'\
	'Venezuela and Guyana',
	'yangtze': 'China',
}

for river in rivers:
	print(f"The {river.title()} through {rivers[river]}.")
print()

for river in rivers.keys():
	print(river)
print()

for country in rivers.values():
	print(country)
print()