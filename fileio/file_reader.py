# using with as for letting python closes file autimatically
with open('pi_digits.txt') as file_object:

# reading an entire fil
#	contents = file_object.read()
# removing trail newline added by read()
#print(contents.rstrip())

# reading file line by line
	for line in file_object:
		print(line.rstrip())
