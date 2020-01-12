file = '../exception/alice.txt'

try:
	with open(file) as F:
		content = F.read()
except:
	print("There are something wrong. Contact the developer of Python.")
else:
	counts = content.count(' the '.lower())
	print(f"There are {counts} of ' the ' in the {file}.")
