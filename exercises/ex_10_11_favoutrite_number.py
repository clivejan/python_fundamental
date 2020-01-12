import json

filename = 'ex_10_11_favoutrite_number.json'
number = input("Please enter your favourite number: ")

with open(filename, 'w') as f:
	json.dump(number, f)
	print("I have saved your number.")
