sandwich_orders = ['ham', 'eggs', 'jam', 'tuna', 'corn']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich  = sandwich_orders.pop()
	print(f"I made your {current_sandwich} sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\nnFinished sandwich:")
for sandwich in finished_sandwiches:
	print(sandwich)
