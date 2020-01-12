filename = 'ex_10_4_guest_book.txt'

with open(filename, 'a') as file_object:

	while True:
		name = input("Please enter your name: ('q' to quit) ")
		if name == 'q':
			break
		print(f"Hi {name}.")
		file_object.write(f"{name}\n")
