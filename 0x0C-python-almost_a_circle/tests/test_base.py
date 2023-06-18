import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Define the absolute path for the file
        cls.filepath = os.path.join(os.getcwd(), "Rectangle.json")

    def tearDown(self):
        # Remove the file after each test
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    def test_id_assignment_with_id_argument(self):
        # Test case where id argument is provided
        obj = Base(id=1)
        self.assertEqual(obj.id, 1)

    def test_id_assignment_without_id_argument(self):
        # Test case where id argument is not provided
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        # Test case to verify the to_json_string() static method
        list_of_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        expectedJson = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(Base.to_json_string(list_of_dicts), expectedJson)

        empty_list = []
        self.assertEqual(Base.to_json_string(empty_list), "[]")

        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        # Test case to verify the from_json_string() static method
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        expected_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        self.assertEqual(Base.from_json_string(json_string), expected_dicts)

        empty_string = ""
        self.assertEqual(Base.from_json_string(empty_string), [])

        self.assertEqual(Base.from_json_string(None), [])

    def test_load_from_file_method(self):
        # Test case to verify the load_from_file() class method
        # Test with non-existent file
        instances = Rectangle.load_from_file()
        self.assertEqual(instances, [])

        # Test with existing file
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 4)
        Rectangle.save_to_file([rect1, rect2])
        instances = Rectangle.load_from_file()
        self.assertIsInstance(instances, list)
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertIsInstance(instances[1], Rectangle)
        self.assertEqual(instances[0].id, 3)
        self.assertEqual(instances[0].width, 1)
        self.assertEqual(instances[0].height, 2)
        self.assertEqual(instances[1].id, 4)
        self.assertEqual(instances[1].width, 3)
        self.assertEqual(instances[1].height, 4)

        # Clean up the file
        os.remove(self.filepath)


if __name__ == '__main__':
    unittest.main()
