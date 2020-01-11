topping = ''

while True:
	topping = input("What topping you want to add to your pizza "
	"('quit' to exit)? ")
	if topping == 'quit':
		break
	else:
		print(f"{topping} is adding to your pizza.")
