def make_shirt(size, text):
	"""make a specified size of T-shirt and print text on it"""
	print(f"\nI will make a {size} T-shirt and print '{text}' on it.")

# using positional arguments
make_shirt('large', 'I need a job')

# using keyword arguments
make_shirt(size='small', text='DevOps')
