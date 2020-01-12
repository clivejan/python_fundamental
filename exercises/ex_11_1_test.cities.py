import unittest

from ex_11_1_city_functions import city_country

class TestCityCountry(unittest.TestCase):
	"""Creating test cases"""

	def test_city_conutry(self):
		"""Do city like 'Montreal, Canada' work?"""
		formatted_city = city_country('montreal', 'canada')
		self.assertEqual(formatted_city, 'Montreal, Canada')

if __name__ == '__main__':
	unittest.main()
