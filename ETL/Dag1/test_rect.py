from audioop import add
import unittest

class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        ''' Returns the area of the rectangle'''
        return self.height * self.width

    def circumference(self):
        return 2 * self.height + 2 * self.width
    
rect = Rectangle(5, 10)
print(rect)
print(rect.height)
print(rect.width)
print(rect.area())


from unittest import TestCase

class TestRectangle(TestCase):

    def test_init_rectangle(self):
        rect = Rectangle(2,3)

        self.assertEqual(rect.height, 2, 'height not initialized correctly')
        self.assertEqual(rect.width, 3, 'width not initialized correctly')

    def test_area(self):

        # Given
        rectangle = Rectangle(5, 10)
        expected = 50

        # When
        result = rectangle.area()

        # Then
        self.assertEqual(expected, result, 'Rectangle area should be height * width')


    def test_circumference(self):

        # Given
        rectangle = Rectangle(5, 10)
        expected_circumference = 30

        # When
        result = rectangle.circumference()

        #Then
        self.assertEqual(expected_circumference, result, 'Rectangle circumference should be 2*height + 2*width')


    def test_circumference_2(self):

        # Given
        rectangle = Rectangle(10, 10)
        expected_circumference = 40

        # When
        result = rectangle.circumference()

        #Then
        self.assertEqual(expected_circumference, result, 'Rectangle circumference should be 2*height + 2*width')

    def test_add(self):
        # Given
        a, b = 2, 3
        expected = 6

        # When
        result = add(a, b)

        #Then
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()

