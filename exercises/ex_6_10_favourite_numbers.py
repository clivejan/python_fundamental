favourite_numbers = {
	'nayeon': [24, 9],
	'sana': [22, 12],
	'mina': [22, 37],
	'dahyun': [7, 21],
	'tzuyu': [20, 25],
}

for name, numbers in favourite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")
