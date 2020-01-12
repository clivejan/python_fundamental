filename = 'ex_10_1_learning_python.txt'

with open(filename) as file_object:
	content = file_object.read()

content = content.replace('Python', 'C')
print(content.rstrip())
