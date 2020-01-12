import unittest

from name_function import get_formatted_name

class NamesTestCases(unittest.TestCase):
	"""Tests from 'name_function.py'"""

	def test_first_last_name(self):
		"""Do names like 'John Doe' work?"""
		formatted_name = get_formatted_name('john', 'doe')
		# Verify that a result matches the result you expected to receive.
		self.assertEqual(formatted_name, 'John Doe')

if __name__ == '__main__':
	unittest.main()
