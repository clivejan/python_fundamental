class Restaurant:
	"""model a restaurant"""

	def __init__(self, restaurant_name, restaurant_type):
		"""Initialize restaurant's attributes"""
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type

	def describe_restaurant(self):
		"""display the resaurant's name and food type"""
		print(f"The {self.restaurant_name.title()} serves {self.restaurant_type.title()} cuisine.")

	def open_restaurant(self):
		"""display whether the restaurant is opening"""
		print(f"The {self.restaurant_name.title()} is now opening.")

# creating three objects
hot_star = Restaurant('Hot-Star', 'taiwan')
red_lobsters = Restaurant('Red Lobsters', 'american')
the_ledbury = Restaurant('The Ledbury', 'england')

# calling a specific method
hot_star.describe_restaurant()
red_lobsters.describe_restaurant()
the_ledbury.describe_restaurant()
