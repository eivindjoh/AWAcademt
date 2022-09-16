
"""
Exercise (Hard):
Sometimes, functions contain calls to other functions that are outside our control.
For instance, it might be a database call, a request to an API or the use of 
another library.
If it is hard for us to control these functions, we can use Mocks to simulate their
behaviour.
In the case below, the day_description function uses the datetime library to get 
the current day.
The problem is, that when we test this it will only work on the day we are 
currently at! 
Here we can use mocks to help us simulate the different days.
In this example, we have a file day_description.py that imports the date function.
A mock can replace this function when we test.
See https://docs.python.org/3/library/unittest.mock-examples.html#partial-mocking
"""
import unittest
from unittest.mock import patch
from day_description import day_description
from datetime import date

class MockTests(unittest.TestCase):
    def test_christmas_day(self):
        # This will fail since we haven't mocked date.today() yet!
        # Patch with a mock object to fix this!
        with patch('day_description.date') as mock_date:
            mock_date.today.return_value = date(2021, 12, 24) 
            description = day_description()
            self.assertEqual(description, "Merry Christmas!")
    
    def test_thursday_description(self):
        # This will fail since we haven't mocked date.today() yet!
        # Patch with a mock object to fix this!
        with patch('day_description.date') as mock_date:
            mock_date.today.return_value = date(2022, 8, 11)
            description = day_description()
            self.assertEqual(description, "Today it is Thursday")

if __name__ == '__main__':
   unittest.main()