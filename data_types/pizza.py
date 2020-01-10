# store information about a pizza being ordered
pizza = {
	'crust': 'thich',
	'toppings': ['mushroms', 'extra cheese'],
}

# summarize the order
print(f"You ordered a {pizza['crust']}-curst pizza "
	"with the folling toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")
