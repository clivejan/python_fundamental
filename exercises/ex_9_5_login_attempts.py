class User:
	"""model a user"""

	def __init__(self, first_name, last_name, location):
		"""Initialize a user"""
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		"""make a sentence to describe a user"""
		print(f"\n{self.first_name.title()} {self.last_name.title()} "
			f"is from {self.location.title()}.")

	def greet_user(self):
		"""make a sentence to greey a user"""
		print(f"How are you doing {self.first_name.title()}?")

	def increment_login_attempt(self):
		"""incrementing the login attempts by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""resetting the login attempts to 0"""
		self.login_attempts = 0

# creating a instances
clive = User('chihwei', 'chan', 'taipei')

# verify methods related to login attemps
print(clive.login_attempts)
clive.increment_login_attempt()
clive.increment_login_attempt()
clive.increment_login_attempt()
print(clive.login_attempts)
clive.reset_login_attempts()
print(clive.login_attempts)
