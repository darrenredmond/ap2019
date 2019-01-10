import unittest
from calculator import add, division, multiply, subtract

class CalculatorTest(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(4, add(2, 2))
        self.assertEqual(5, add(2, 3))
        self.assertEqual(8.3, add(2.8, 5.5))
        self.assertEqual('ab', add('a', 'b'))

    def testDivide(self):
        self.assertEqual(4, division(4, 1))
        self.assertEqual(3, division(6, 2))
        self.assertEqual(5.8, division(14.5, 2.5))

    def testMultiply(self):
        self.assertEqual(4, multiply(2, 2))
        self.assertEqual(9, multiply(3, 3))

    def testSubtract(self):
        self.assertEqual(0, subtract(2, 2))

unittest.main()
