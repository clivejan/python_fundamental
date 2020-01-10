available_toppings = ('mushrooms', 'olives', 'green pepper', 
	'pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['mushrooms', 'green peppers', 
	'extra cheese', 'job offer']
#requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print("Sorry, we are out of greent peppers rigth now.")
		elif requested_topping not in available_toppings:
			print(f"Sorry, we don't have {requested_topping}.")
		else:
			print(f"Adding {requested_topping}")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

