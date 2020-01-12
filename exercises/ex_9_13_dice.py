"""
A set of attributes and methods to represent a dice
"""
import random

class Die:
	"""represent a die"""

	def __init__(self, sides=6):
		"""initialize a die"""
		self.sides = sides

	def roll_die(self):
		"""retuen the result of roll a die"""
		result = random.randint(1, self.sides)
		return result

# create a 6-sides die and roll it 10 times
die = Die()
for i in range(10):
	print(die.roll_die(), end=' ')
print()

# create a 10 sides die and roll it 10 times
die = Die(10)
for i in range(10):
	print(die.roll_die(), end=' ')
print()

# create a 20-sides die and roll it 10 times
die = Die(20)
for i in range(10):
	print(die.roll_die(), end=' ')
print()
