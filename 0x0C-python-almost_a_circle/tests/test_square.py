import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_attributes(self):
        # Test case to verify attribute assignment
        square = Square(size=5, x=2, y=3, id=1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_square_attribute_setters(self):
        # Test case to verify attribute setters
        square = Square(size=5, x=2, y=3, id=1)
        square.size = 7
        square.x = 4
        square.y = 5
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)
        self.assertRaises(TypeError, setattr, square, "size", "invalid")
        self.assertRaises(TypeError, setattr, square, "x", "invalid")
        self.assertRaises(TypeError, setattr, square, "y", "invalid")
        self.assertRaises(ValueError, setattr, square, "size", -5)
        self.assertRaises(ValueError, setattr, square, "x", -2)
        self.assertRaises(ValueError, setattr, square, "y", -3)

    def test_square_area(self):
        # Test case to verify the area() method
        square = Square(size=5, x=2, y=3, id=1)
        self.assertEqual(square.area(), 25)

    def test_square_update(self):
        # Test case to verify the update() method
        square = Square(size=5, x=2, y=3, id=1)
        square.update(2, 7, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

        square.update(id=3, size=8, x=6, y=7)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

    def test_square_str(self):
        # Test case to verify the __str__ method
        square = Square(size=5, x=2, y=3, id=1)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(square), expected_output)

    def test_square_size_getter(self):
        # Test case to verify the size getter
        square = Square(size=5)
        self.assertEqual(square.size, 5)

    def test_square_size_setter(self):
        # Test case to verify the size setter
        square = Square(size=5)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

        self.assertRaises(TypeError, setattr, square, "size", "invalid")
        self.assertRaises(ValueError, setattr, square, "size", -5)

    def test_square_update_args_kwargs(self):
        # Test case to verify the update() method with *args and **kwargs
        square = Square(size=5, x=2, y=3, id=1)

        square.update(size=10)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

        square.update(size=20, x=4, y=5)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)
        self.assertEqual(square.id, 1)

    def test_square_update_args_skipped_kwargs(self):
        # Test case to verify the update() method with *args
        # skipped if **kwargs exists
        square = Square(size=5, x=2, y=3, id=1)
        square.update(size=7, x=4, y=5)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_square_update_args_empty_kwargs(self):
        # Test case to verify the update() method with *args and empty **kwargs
        square = Square(size=5, x=2, y=3, id=1)
        square.update()
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_to_dictionary(self):
        # Test case to verify the to_dictionary() method
        square = Square(size=5, x=2, y=3, id=1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
