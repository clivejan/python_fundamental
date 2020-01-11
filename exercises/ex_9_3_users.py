class User:
	"""model a user"""

	def __init__(self, first_name, last_name, location):
		"""Initialize a user"""
		self.first_name = first_name
		self.last_name = last_name
		self.location = location

	def describe_user(self):
		"""make a sentence to describe a user"""
		print(f"\n{self.first_name.title()} {self.last_name.title()} "
			f"is from {self.location.title()}.")

	def greet_user(self):
		"""make a sentence to greey a user"""
		print(f"How are you doing {self.first_name.title()}?")

# creating serveal instances
clive = User('chihwei', 'chan', 'taipei')
carrie = User('naiwen', 'ku', 'taichung')
tzuyu = User('tzuyu', 'chou', 'tainai')

# calling methods
clive.describe_user()
clive.greet_user()

carrie.describe_user()
carrie.greet_user()

tzuyu.describe_user()
tzuyu.greet_user()
