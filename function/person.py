def build_person(first_name, last_name, age=None):
	"""return a dictionary of information"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

devops = build_person('chihwei', 'chan')
print(devops)

devops = build_person('chihwei', 'chan', 40)
print(devops)
