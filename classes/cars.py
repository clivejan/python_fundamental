"""A class that can be used to represent a car"""

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

	def update_odometer(self, mileage):
		"""
		set the odometer reading to the given value
		reject the change if it attempt to roll the odometer back
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cannot roll back an odometer!")

	def increment_odometer(self, miles):
		"""add the giev amount to the odometer reading"""
		self.odometer_reading += miles

class Battery:
	"""a simple attempt to model a battery for an electric car"""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""print a statement describing the battery size"""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""print a stetement about the range this battery provides"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
	"""represent aspects of a car, specific to eletirc vehicles"""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class"""
		super().__init__(make, model, year)
		"""These initialize attributes specific to an electric car"""
		self.battery = Battery()