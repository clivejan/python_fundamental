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

# create a object
restaurant = Restaurant('Hot-Star', 'taiwan')

# access the attributes and call the methods
print(restaurant.restaurant_name)
print(restaurant.restaurant_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
