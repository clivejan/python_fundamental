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

my_dream_car = Car('audi', 'q5', 2019)
print(my_dream_car.get_descriptive_name())
my_dream_car.read_odometer()

# modifying an attribute's value directly
my_dream_car.odometer_reading = 23
my_dream_car.read_odometer()

# modifying an attribute's value through a method
my_dream_car.update_odometer(20)
my_dream_car.update_odometer(46)
my_dream_car.read_odometer()

# incrementing an attribute's value through a method
my_used_car = Car('Hyundai', "Matrix", 2005)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

