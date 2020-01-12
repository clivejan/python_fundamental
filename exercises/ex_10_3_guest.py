filename = 'ex_10_3_guest.txt'

name = input("Enter your name, I will steal your life: ")

with open(filename, 'w') as file_object:
	file_object.write(f"{name}\n")
