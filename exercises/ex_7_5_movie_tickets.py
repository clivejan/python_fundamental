age = ''

while True:
	age = input("How old are you ('quit' to exit)? ")
	if age == 'quit':
		break
	else:
		age = int(age)
		if age < 3:
			price = 0
		elif age < 12:
			price = 10
		elif age > 12:
			price = 15
		print(f"You have to pay ${price} for your movie ticket.")
