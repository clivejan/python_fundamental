filename = 'ex_10_5_programming_poll.txt'

with open(filename, 'a') as file_object:

	while True:
		reason = input("Why do you like programming? ('q' to quit) ")
		if reason == 'q':
			break
		file_object.write(f"{reason}\n")
