vacations = {}

active = True

while active:
	name = input("What is your name: ")
	location = input("Where would you like to go next vacation? ")
	vacations[name] = location

	respond = input("Does anyone like to respond this poll? (yes/no) ")
	if respond == 'no':
		active = False

print("\n--- Polling Result ---")
for name, location in vacations.items():
	print(f"{name.title()} would like to go to {location} next vacation.")
