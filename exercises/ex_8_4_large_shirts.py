def make_shirt(size='large', text='I love Python'):
	"""make a specified size of T-shirt and print text on it"""
	print(f"\nI will make a {size} T-shirt and print '{text}' on it.")

# make a shirt with all default value
make_shirt()

# make a small shirt with default text
make_shirt('medium')

# make all a customize shirt
make_shirt('small', 'DevOps')
