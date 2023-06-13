**0x0A. Python - Inheritance

* 0-lookup.py : a function that returns the list of available attributes and methods of an object
* 1-my_list.py : class MyList that inherits from list which define a Public instance method: def print_sorted(self): that prints a sorted list
	* tests/1-my_list.txt : test file for the class MyList
* 2-is_same_class.py : a function that returns True if the object is exactly an instance of the specified class ; otherwise False
* 3-is_kind_of_class.py : a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
* 4-inherits_from.py : a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
* 5-base_geometry.py : an empty class
* 6-base_geometry.py : a class BaseGeometry (based on 5-base_geometry.py) with :
	* Public instance method: def area(self): that raises an Exception with the message area() is not implemented
* 7-base_geometry.py : a class BaseGeometry (based on 6-base_geometry.py) with :
	* Public instance method: def area(self): that raises an Exception with the message area() is not implemented
	* Public instance method: def integer_validator(self, name, value): that validates value:
		- name is always a string
		- if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
		- if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
* 8-rectangle.py : a class Rectangle that inherits from BaseGeometry (7-base_geometry.py) with:
	* Instantiation with width and height: def __init__(self, width, height):
	* width and height must be private. No getter or setter
	* width and height must be positive integers, validated by integer_validator
* 9-rectangle.py : a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py) with :
	* Instantiation with width and height: def __init__(self, width, height)::
	* width and height must be private. No getter or setter
	* width and height must be positive integers validated by integer_validator
	* the area() method must be implemented
	* print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
* 10-square.py :  a class Square that inherits from Rectangle (9-rectangle.py):
	* Instantiation with size: def __init__(self, size)::
	* size must be private. No getter or setter
	* size must be a positive integer, validated by integer_validator
	* the area() method must be implemented
* 11-square.py : a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py) with :
	* Instantiation with size: def __init__(self, size):
	* size must be private. No getter or setter
* size must be a positive integer, validated by integer_validator
* the area() method must be implemented
* print() should print, and str() should return, the square description: [Square] <width>/<height>
* 100-my_int.py : a class MyInt that inherits from int:
	* MyInt is a rebel. MyInt has == and != operators inverted
* 101-add_attribute.py : a function that adds a new attribute to an object if it's possible:
	* Raise a TypeError exception, with the message can't add new attribute if the object can't have new attribute
