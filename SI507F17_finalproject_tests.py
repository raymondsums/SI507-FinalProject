import unittest
from SI507F17_finalproject import *

class CodeTests(unittest.TestCase):
	def setUp(self):
		self.cached = CACHE_DICTION
		self.shortlist = shortlist
		self.bearer_token = bearer_token
		self.business_dict = business_dict
		self.res_01 = res_01
		self.res_02 = res_02

	def test_cache(self):
		self.assertEqual(type(self.cached),dict)

	def test_cache_ident(self):
		self.assertNotEqual((self.cached).keys(),'')

	def test_bearer_token(self):
		self.assertEqual(type(self.bearer_token),str)

	def test_business_dict_1(self):
		self.assertEqual(type(self.business_dict),dict)

	def test_business_dict_2(self):
		self.assertEqual(type(self.business_dict['Review_Count']),int)

	def test_business_dict_3(self):
		self.assertEqual(type(self.business_dict['Rating']),float)

	def test_business_dict_4(self):
		self.assertLessEqual(self.business_dict['Rating'],5)

	def test_business_dict_5(self):
		self.assertIn('$',self.business_dict['Price'])

	def test_business_dict_6(self):
		self.assertEqual(type(self.business_dict['ID']),str)

	def test_business_dict_7(self):
		self.assertEqual(type(self.business_dict['Name']),str)

	def test_business_dict_8(self):
		self.assertEqual(type(self.business_dict['City']),str)

	def test_shortlist(self):
		self.assertEqual(len(self.shortlist),50)

	def test_shortlist_2(self):
		self.assertEqual(type(self.shortlist),list)

	def test_shortlist_3(self):
		self.assertEqual(len(shortlist[0]),5)

	def test_res_id(self):
		self.assertEqual(self.res_01,self.res_02)

	def tearDown(self):
		pass

if __name__ == "__main__":
	unittest.main(verbosity=2)
