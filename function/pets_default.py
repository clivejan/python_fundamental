# positinoal arguments have to be set before default arguments
def describe_pet(pet_name, animal_type='tiger'):
	"""Display information about a pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name}.")

describe_pet('kitty')
describe_pet(pet_name='kiki')

# if argument is explicit assigned, the deault value will ve ignored
describe_pet('micky', 'dog')
