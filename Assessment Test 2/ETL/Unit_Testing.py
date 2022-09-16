import unittest

"""

The unittest module is a standard package for unit testing.
Structure: Test class with test functions. One test function = one test case.
All files with name like "test*" will run.

Standard test case structure:

    Given: Set up or build any test data and/or prerequisite.
    When: Tested functionality runs.
    Then: Assert whether results are as expected.

Writing tests may require to refactoring your code..

"""

class Calculator:
    """
    The calculator class can be used like this:
    cal = Calculator()
    result = calc.add(1,2)
    print(result) => prints 3
    """

    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if not b:
            return "inf"
        return a / b


class CalculatorTest(unittest.TestCase):
    
    def test_div_by_zero(self):
        
        calc = Calculator()

        #Given
        a, b = 1, 0
        expected = "inf"
        #When
        res = calc.div(a, b)
        #Then
        self.assertEqual(expected, res, "Divide by zero should give inf")

    def test_add(self):

        calc = Calculator()

        #Given
        a, b = 1, 2
        expected = 3
        #When
        res = calc.add(a, b)
        #Then
        self.assertEqual(expected, res, "something is wrong with the add function")
    
    def test_sub(self):

        calc = Calculator()

        #Given
        a, b = 1, 2
        expected = -1
        #When
        res = calc.sub(a, b)
        #Then
        self.assertEqual(expected, res, "something is wrong with the sub function")

    def test_mul(self):

        calc = Calculator()

        #Given
        a, b = 1, 2
        expected = 2
        #When
        res = calc.mul(a, b)
        #Then 
        self.assertEqual(expected, res, "something is wrong with the mul function")

    def test_div(self):

        calc = Calculator()

        #Given
        a, b = 2, 2
        expected = 1
        #When
        res = calc.div(a, b)
        #Then
        self.assertEqual(expected, res, "something is wrong with the div function")


if __name__ == "__main__":
    unittest.main()