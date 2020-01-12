def count_words(filename):
	"""counting the approximate number of words in a file"""
	try:
		with open(filename, encoding='utf-8') as F:
			content = F.read()
	except FileNotFoundError:
		#print(f"Sorry, the file {filename} does not exist.")
		pass
	else:
		words = content.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'found_a_job.txt', 'division_calculator.py']
for filename in filenames:
	count_words(filename)
