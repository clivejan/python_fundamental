age = 40

if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'toddler'
elif age < 13:
	stage = 'kid'
elif age < 20:
	stage = 'teenager'
elif age < 65:
	stage = 'adult'
elif age >= 65:
	stage = 'elder'

print(f"You are in the stage of {stage}.")
