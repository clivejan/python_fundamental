my_foods = ['pizza', 'falafel', 'carrot cake']
firent_foods = my_foods[:]

my_foods.append('cannoli')
firent_foods.append('ice cream')

print("My favourite foods are: ")
for food in my_foods:
	print(f"\t{food}")

print("\nMy friend\'s favourite foods are:")
for food in firent_foods:
	print(f"\t{food}")
