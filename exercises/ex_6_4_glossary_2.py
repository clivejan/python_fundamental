data_type = {
	'string': 'strings are sequences of character data.',
	'integer': 'a whole number',
	'float': 'a number with decimal point',
	'list': 'a sequence of ordered data',
	'dictionary': 'a key value pair strucuture'
}

for term in data_type.keys():
	print(f"{term}: {data_type[term]}\n")
