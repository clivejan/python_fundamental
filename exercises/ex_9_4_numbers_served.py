class Restaurant:
	"""model a restaurant"""

	def __init__(self, restaurant_name, restaurant_type):
		"""Initialize restaurant's attributes"""
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type
		self.number_served = 0

	def describe_restaurant(self):
		"""display the resaurant's name and food type"""
		print(f"The {self.restaurant_name.title()} serves {self.restaurant_type.title()} cuisine.")

	def open_restaurant(self):
		"""display whether the restaurant is opening"""
		print(f"The {self.restaurant_name.title()} is now opening.")

	def set_numner_served(self, number):
		"""setting the number of serverd customers"""
		self.number_served = number

	def increment_numner_served(self, amount):
		"""incrementing the number of serverd customers"""
		self.number_served += amount

# create a object
restaurant = Restaurant('Hot-Star', 'taiwan')

print(restaurant.number_served)

# set the served number directory
restaurant.number_served = 10
print(restaurant.number_served)

# set the served number through a method
restaurant.set_numner_served(15)
print(restaurant.number_served)

# increment the served number through a method
restaurant.increment_numner_served(5)
print(restaurant.number_served)
