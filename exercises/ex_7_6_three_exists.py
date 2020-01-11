active = True

while active:
	topping = input("What topping you want to add to your pizza "
	"('quit' to exit)? ")
	if topping == 'quit':
		active = False
	else:
		print(f"{topping} is adding to your pizza.")
