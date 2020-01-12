import unittest

from ex_11_2_city_functions import city_country

class TestCityCountry(unittest.TestCase):
	"""Creating test cases"""

	def test_city_conutry(self):
		"""Do city like 'Montreal, Canada' work?"""
		formatted_city = city_country('montreal', 'canada')
		self.assertEqual(formatted_city, 'Montreal, Canada')

	def test_city_conutry_population(self):
		"""Do city like 'Montreal, Canada - population 1780000.' work?"""
		formatted_city = city_country('montreal', 'canada', 1780000)
		self.assertEqual(formatted_city, 'Montreal, Canada '
			'- population 1780000.')

if __name__ == '__main__':
	unittest.main()
