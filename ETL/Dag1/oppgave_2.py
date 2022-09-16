
"""
Exercise 1:
Write unit tests for the number_sorter function.
How many unit tests should you at least have to cover the function?
Hint: This method might be of use 
https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
Note that this function requires the arguments of the function to be after the 
function itself
E.g self.assertRaises(Exception, my_function, 1, 2)
Will call the function my_function(1,2) and expect that Exception is raised
Exercise 2:
Take a function that you have previously written in the AW Course, and create unit 
tests for it! 
You'll probably see that some functions are a lot harder to test than others, 
especially if they have many dependencies
"""
import unittest
def number_sorter(numbers, method):
    """ Sorts the list of numbers """
    if not isinstance(numbers, list):
        raise ValueError("Numbers must be a list!")
    if any([not isinstance(num, int) for num in numbers]):
        raise ValueError("All numbers in the list must be int!")
    if method == "sort_asc":
        return sorted(numbers)
    if method == "sort_desc":
        return sorted(numbers, reverse=True)
    raise ValueError("We have not implemented that method yet!")


class NumberSorterTest(unittest.TestCase):

    def test_string_input_yields_error(self):
        # Given
        numbers = 'asd'
        method = 'sort_asc'
        # When/Then
        self.assertRaises(ValueError, number_sorter, numbers, method)

    def test_sort_asc(self):
        # Given
        numbers = [5,1,7,1,2]
        expected = [1,1,2,5,7]
        # When
        result = number_sorter(numbers, method='sort_asc')
        self.assertEqual(expected, numbers, 'Numbers should be sorted ascending')

  
if __name__ == '__main__':
    unittest.main()