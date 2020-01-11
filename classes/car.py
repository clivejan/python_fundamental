class Car:
	"""A simple attemp to represent a car"""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		# setting a default value for an attribute
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""print a statement showing the car's mileage"""
		print(f"This car has {self.odometer_reading} miles on it.")

my_dream_car = Car('audi', 'q5', 2019)
print(my_dream_car.get_descriptive_name())
my_dream_car.read_odometer()
