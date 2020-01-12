class Restaurant:
	"""model a restaurant"""

	def __init__(self, restaurant_name, restaurant_type):
		"""Initialize restaurant's attributes"""
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type
		self.number_served = 0

	def describe_restaurant(self):
		"""display the resaurant's name and food type"""
		print(f"The {self.restaurant_name.title()} serves "
			f"{self.restaurant_type.title()} cuisine.")

	def open_restaurant(self):
		"""display whether the restaurant is opening"""
		print(f"The {self.restaurant_name.title()} is now opening.")

	def set_numner_served(self, number):
		"""setting the number of serverd customers"""
		self.number_served = number

	def increment_numner_served(self, amount):
		"""incrementing the number of serverd customers"""
		self.number_served += amount

class IceCreamStand(Restaurant):
	"""a simple attmpes to model a ice cream stand"""

	def __init__(self, restaurant_name, restaurant_type, favourite):
		"""Initialize the IceCreamStand attributes"""
		super().__init__(restaurant_name, restaurant_type)
		self.favourite = favourite

	def display_favourite(self):
		"""display all flavours"""
		for flavour in self.favourite:
			print(f"- {flavour}")

amazing_icecream = IceCreamStand('Amazing IceCream', 'IceCream', \
		['sock', 'booger', 'rock'])
amazing_icecream.display_favourite()
