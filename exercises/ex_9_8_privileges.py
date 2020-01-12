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

class Privileges:
	"""model the privilegs"""

	def __init__(self):
		"""Initialize the pivileges attributes"""
		self.privilegs = ['hire employee', 'promote employee', \
		 	'fire employee']
	
	def show_privileges(self):
		"""display all privileges the admin has"""
		for privilege in self.privilegs:
			print(privilege)

class Admin(User):
	"""a simple attemps to model an admin user"""
	def __init__(self, first_name, last_name, location):
		"""Initialize the admin's attributes"""
		super().__init__(first_name, last_name, location)
		self.privileges = Privileges()	

clive = Admin('chihwei', 'chan', 'montreal')
clive.privileges.show_privileges()
