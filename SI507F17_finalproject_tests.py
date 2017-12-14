import unittest
import SI507F17_finalproject.py

class CodeTests(unittest.TestCase):
	def setUp(self):
		self.cached = CACHE_FNAME
		self.shortlist = shortlist

	def test1(self):
		self.assertEqual(type(self.cached),json)

	def test_pop(self):
		self.assertEqual(len(self.shortlist),46)

	def test3(self):
		pass

	def tearDown(self):
		pass

if __name__ == "__main__":
	unittest.main(verbosity=2)
