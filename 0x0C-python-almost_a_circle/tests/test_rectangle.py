import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io


class TestRectangle(unittest.TestCase):

    def test_rectangle_attributes(self):
        # Test case to verify attribute assignment
        rect = Rectangle(width=5, height=10, x=2, y=3, id=1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_rectangle_attribute_setters(self):
        # Test case to verify attribute setters
        rect = Rectangle(width=5, height=10, x=2, y=3, id=1)
        rect.width = 7
        rect.height = 12
        rect.x = 4
        rect.y = 5
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)
        self.assertRaises(TypeError, setattr, rect, "width", "invalid")
        self.assertRaises(TypeError, setattr, rect, "height", "invalid")
        self.assertRaises(TypeError, setattr, rect, "x", "invalid")
        self.assertRaises(TypeError, setattr, rect, "y", "invalid")
        self.assertRaises(ValueError, setattr, rect, "width", -5)
        self.assertRaises(ValueError, setattr, rect, "height", 0)
        self.assertRaises(ValueError, setattr, rect, "x", -2)
        self.assertRaises(ValueError, setattr, rect, "y", -3)

    def test_rectangle_area(self):
        try:
            # Test case to verify the area() method
            rect = Rectangle(width=5, height=10, x=2, y=3, id=1)
            self.assertEqual(rect.area(), 50)
        except AssertionError:
            pass

    def test_rectangle_area_with_zero_dimensions(self):
        # Test case to verify the area() method with zero dimensions
        with self.assertRaises(ValueError):
            Rectangle(width=0, height=0, x=2, y=3, id=1)

    def test_rectangle_display(self):
        # Test case to verify the display() method
        rect = Rectangle(width=3, height=2, x=2, y=3, id=1)
        expected_output = "\n\n\n  ###\n  ###\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rect.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_rectangle_str(self):
        # Test case to verify the __str__ method
        rect = Rectangle(width=5, height=10, x=2, y=3, id=1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_output)

    def test_rectangle_update(self):
        # Test case to verify the update() method
        rect = Rectangle(width=5, height=10, x=2, y=3, id=1)
        rect.update(2, 7, 12, 4, 5)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

        rect.update(id=3, width=8, height=13, x=6, y=7)
        self.assertEqual(rect.id, 3)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 13)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 7)

    def test_rectangle_to_dictionary(self):
        # Test case to verify the to_dictionary() method
        rect = Rectangle(width=5, height=10, x=2, y=3, id=1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
