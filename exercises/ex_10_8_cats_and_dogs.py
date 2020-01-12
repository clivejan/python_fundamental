def show_content(filename):
	"""display filename's content"""
	try:
		with open(filename) as F:
			content = F.read()
	except FileNotFoundError:
		print(f"The file {filename} is not found.")
	else:
		print(content.rstrip())

filenames = ['ex_10_8_cats_and_dogs_cats.txt',
		'ex_10_8_cats_and_dogs_job.txt',
		'ex_10_8_cats_and_dogs_dogs.txt']
for filename in filenames:
	show_content(filename)
