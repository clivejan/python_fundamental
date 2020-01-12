# add two user input numbers together
print("Enter two numbers, I'll add them together. ('q' to quit)")

while True:
	number1 = input("Enter first number: ")
	if number1 == 'q':
		break
	number2 = input("Enter second number: ")
	if number2 == 'q':
		break

	try:
		result = int(number1) + int(number2)
	except ValueError:
		print("You have to enter two integers!")
	else:
		print(result)
