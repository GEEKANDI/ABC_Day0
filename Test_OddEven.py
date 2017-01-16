import unittest

import OddEven

class test_odd_or_even(unittest.TestCase):
	def test_even(self):
		self.assertTrue(64%2==0)
