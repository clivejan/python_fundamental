import random

class Lottery:
	"""model a lottery"""

	def __init__(self, available_choice, choice_number):
		"""initialize the lottery"""
		self.available_choice = available_choice
		self.choice_number = choice_number

	def quick_play(self):
		"""retunn a random choice for lottery"""
		result = []
		for i in range(self.choice_number):
			result.append(random.choice(self.available_choice))
		return result

# set the lottery
available_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D']
choice_number = 4

lottery = Lottery(available_choice, choice_number)

# get the win ticket
winner = lottery.quick_play()

# find put how difficult
i = 0
while True:
	my_ticket = lottery.quick_play()
	i += 1
	if my_ticket == winner:
		break

print(f"I won the ticket after {i} tries.")
