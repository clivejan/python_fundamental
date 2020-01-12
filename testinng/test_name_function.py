import unittest

from name_function import get_formatted_name

class NamesTestCases(unittest.TestCase):
	"""Tests from 'name_function.py'"""

	def test_first_last_name(self):
		"""Do names like 'John Doe' work?"""
		formatted_name = get_formatted_name('john', 'doe')
		# Verify a result matches the result you expected to receive.
		self.assertEqual(formatted_name, 'John Doe')

	def test_first_middle_last_name(self):
		"""Do names like 'John Anonymous Doe' work?"""
		formatted_name = get_formatted_name('john', 'doe', 'anonymous')
		self.assertEqual(formatted_name, 'John Anonymous Doe')

if __name__ == '__main__':
	unittest.main()
