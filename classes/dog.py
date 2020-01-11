class Dog:
	"""A simple attempt to model a dog"""

	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in resposes to a command"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command"""
		print(f"{self.name} rolled over!")

# making a instance from a class
my_dog = Dog('Willie', 6)


# accessing attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# calliing methods
my_dog.sit()
my_dog.roll_over()
