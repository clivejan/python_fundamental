import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Test for the AnonymousSurvey"""

	def test_store_single_response(self):
		"""Test that a single response is stored perperly."""
		question = "What language did you first learn to speak? "
		my_sruvey = AnonymousSurvey(question)
		my_sruvey.store_response('Python')
		self.assertIn('Python', my_sruvey.response)

	def test_store_three_respinses(self):
		"""Test that three individual responses are stored perperly."""
		question = "What language did you first learn to speak? "
		my_sruvey = AnonymousSurvey(question)

		responses = ['Chinese', 'English', 'Python']
		for response in responses:
			my_sruvey.store_response(response)

		for response in responses:
			self.assertIn(response, my_sruvey.response)

if __name__ == '__main__':
	unittest.main()
