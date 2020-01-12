import random

available_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D']
result = []

# randomly select four items
for i in range(4):
	result.append(random.choice(available_choice))

print(f"Anyone ho has {result} wins the prize.")
