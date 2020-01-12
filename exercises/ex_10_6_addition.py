# add two user input numbers together

print("Enter two numbers, I'll add them together.")
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

try:
	result = int(number1) + int(number2)
except ValueError:
	print("You have to enter two integers!")
else:
	print(result)
