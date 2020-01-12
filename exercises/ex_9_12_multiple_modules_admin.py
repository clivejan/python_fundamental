from ex_9_12_multiple_modules_user import User

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
