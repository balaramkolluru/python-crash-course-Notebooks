import unittest
from name_function import get_formatted_name

class NamesTestcase(unittest.TestCase):
	"""Tests for function name_fucntion.py"""
	def test_first_last_name(self):
		"""Do names like janes joplin Works?"""
		formatted_name = get_formatted_name('janes', 'joplin')
		self.assertEqual(formatted_name, 'Janes Joplin')

	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
	unittest.main()