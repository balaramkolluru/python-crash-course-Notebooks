import unittest
from survey import AnonymusSurvey

class TestAnonymusSurvey(unittest.TestCase):
	"""Tests for the class Anonymus Survey"""

	def test_store_single_response(self):
		"""Test that single response is stored properly"""
		question = "what language did you first learn to speak?"
		my_survey = AnonymusSurvey(question)
		my_survey.store_response('English')
		self.assertIn('English', my_survey.responses)

	def test_store_three_response(self):
		"""Test that three individual responses stored properly"""
		question = "what language did you first learn to speak?"
		my_survey = AnonymusSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']
		for response in responses:
			my_survey.store_response(response)

		for response in responses:
			self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
	unittest.main()