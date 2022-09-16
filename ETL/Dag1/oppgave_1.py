
"""
Exercise:
1. Write at least one unit test for each method of the Calculator class.
   Afterwards, run `coverage run -m unittest 000_testing.py`, then run `coverage 
report` to see the test coverage. 
2. The div method in the Calculator class is poorly implemented. If we divide by 
zero, we will get an error.
   Most calculators return "inf" when dividing by zero, so ours should do that as 
well.
   First, try using the calculator class to divide by zero and see what error you 
get.
   Then, write a test that gives the behaviour that we want (i.e that when you 
divide by zero you get "inf" back)
   Try running the test now. It should fail since we haven't implemented the fix 
yet.
   After seeing it fail, fix the div method so that the test passes.
  
"""
import unittest

class Calculator:
    """
    The calculator class can be used like this:
    calc = Calculator()
    result = calc.add(1,2)
    print(result) => prints 3 
    """
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        if b == 0:
            return 'inf'
        return a/b


class CalculatorTest(unittest.TestCase):

    def test_div_by_zero(self):
        # Given
        calc = Calculator()
        expected = "inf"
        # When
        res = calc.div(1, 0)

        # Then
        self.assertEqual(expected, res, 'Divide by zero should give inf')


    def test_add(self):

        calc = Calculator()

        # Given
        a, b = 2, 3
        expected = 5
        # When 
        result = calc.add(a, b)
        # Then
        self.assertEqual(expected, result, 'add is not correct')

    def test_sub(self):

        calc = Calculator()

        # Given
        a, b = 2, 3
        expected = -1
        # When
        result = calc.sub(a, b)
        # Then
        self.assertEqual(expected, result, 'sub is not correct')

    def test_mul(self):

        calc = Calculator()

        # Given
        a, b = 2, 3
        expected = 6
        # When
        result = calc.mul(a, b)
        # Then
        self.assertEqual(expected, result, 'mul is not correct')

    def test_div(self):

        calc = Calculator()

        # Given
        a, b = 2, 3
        expected = 2/3
        # When
        result = calc.div(a, b)
        # Then
        self.assertEqual(expected, result, 'div is not correct')


if __name__ == '__main__':
    unittest.main()
