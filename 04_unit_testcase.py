#https://pypi.org/project/pytest-html/

#Creating Add function for addition
import unittest

def add(a, b):
    return a + b
#Creating multi function for multiplication
def multi(a,b):
  return a*b

#Creating Class for Unit Testing
class test_class(unittest.TestCase):
    def test_add(self):
      self.assertEqual(10, add(7, 3))
    def test_multi(self):
      self.assertEqual(25,multi(5,5))
    def test_sum(self):
        k = 20
        l = 40
        m = 90
        sum = k + l + m
        self.assertEqual(150, sum)
        print("UNIT TEST VALIDATIONS")

        print("dddddddddddd")
        
    
# # create a test suite  for test_class using  loadTestsFromTestCase()
# suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
# #Running test cases using Test Cases Suit..
# unittest.TextTestRunner(verbosity=2).run(suite)