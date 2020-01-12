class Employee:
	"""represent a employee"""

	def __init__(self, first, last, salary):
		"""Initialize the Employee class"""
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, amount=5000):
		"""raise salary"""
		self.salary += amount
