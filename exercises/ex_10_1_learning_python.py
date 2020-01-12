filename = 'ex_10_1_learning_python.txt'

with open(filename) as file_object:
	# print the entire content
	content = file_object.read()
	print(content)

	# print the content line by line
	file_object.seek(0, 0)
	for line in file_object:
		print(line.rstrip())

	# print the connten outside the with block
	file_object.seek(0, 0)
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
