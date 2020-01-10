my_pizzas = ['Loaded Baked Potato', 'Macaroni And Cheese', 'Chicken Alfredo']
friend_pizzas = my_pizzas[:]

my_pizzas.append('my pizza')
friend_pizzas.append('friend pizza')

print("My favourite pizzas are:")
for pizza in my_pizzas:
	print(f"\t{pizza}")

print("MY friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(f"\t{pizza}")
