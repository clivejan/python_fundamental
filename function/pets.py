def describe_pet(animal_type='tiger', pet_name):
	"""Display information about a pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name}.")

describe_pet('planet', 'Earth')
describe_pet('galaxy', 'Solar system')

# order matters in positional arguments
describe_pet('Earth', 'planet')

# usgin keyword arguments
describe_pet(animal_type='planet', pet_name='Earth')

# the order of keyword arguments does not matter
describe_pet(pet_name='Earth', animal_type='planet')
