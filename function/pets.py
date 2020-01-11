def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name}.")

describe_pet('planet', 'Earth')
describe_pet('galaxy', 'Solar system')

# order matters in positional arguments
describe_pet('Earth', 'planet')

# usgin keyword arguments
describe_pet(animal_type='planet', pet_name='Earth')