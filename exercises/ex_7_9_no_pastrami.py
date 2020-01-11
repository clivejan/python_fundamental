sandwich_orders = ['ham', 'pastrami', 'eggs', 'jam', 'pastrami', \
	'tuna', 'corn', 'pastrami']

print(f"Origin orders: {str(sandwich_orders)}")

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print(f"Modified orders: {str(sandwich_orders)}")
