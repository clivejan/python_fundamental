import json

filename = 'ex_10_12_favourite_number_remembered.json'

try:
	with open(filename) as f:
		number = json.load(f)
except FileNotFoundError:
	number = input("Please enter your favourite number: ")
	with open(filename, 'w') as f:
		json.dump(number, f)
	print("I have saved your number.")
else:
	print(f"I knnow your favourite number. It's {number}.")
