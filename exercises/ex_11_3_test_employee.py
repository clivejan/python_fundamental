import unittest

from ex_11_3_employee import Employee

class TestEmployee(unittest.TestCase):
	"""Create a TestEmployee test cases"""

	def setUp(self):
		"""create attributes for all test cases"""
		self.clive = Employee('chihwei', 'chan', 60000)

	def test_give_default_raise(self):
		"""Do salary raise from 60000 to 65000 by default amount"""
		self.clive.give_raise()
		self.assertEqual(self.clive.salary, 65000)

	def test_give_custom_raise(self):
		"""Do salary raise from 60000 to 70000 by given amount"""
		self.clive.give_raise(10000)
		self.assertEqual(self.clive.salary, 70000)

if __name__ == '__main__':
	unittest.main()
