import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Test for the AnonymousSurvey"""

	def setUp(self):
		"""
		Create a survey adn a set of responses for use in all test motheds.
		"""
		question = "What language did you first learn to speak? "
		self.my_sruvey = AnonymousSurvey(question)
		self.responses = ['Chinese', 'English', 'Python']

	def test_store_single_response(self):
		"""Test that a single response is stored perperly."""
		self.my_sruvey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_sruvey.response)

	def test_store_three_respinses(self):
		"""Test that three individual responses are stored perperly."""
		for response in self.responses:
			self.my_sruvey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_sruvey.response)

if __name__ == '__main__':
	unittest.main()
