**0x09. Python - Everything is object

* 0-answer.txt : the function used to print the type of an object
* 1-answer.txt : the function used to get the variable identifier
* 2-answer.txt : a = 89, b = 100, do a and b point to the same object?
* 3-answer.txt : a = 89, b = 89, do a and b point to the same object?
* 4-answer.txt : a = 89, b = a, do a and b point to the same object?
* 5-answer.txt : a = 89, b = a + 1, do a and b point to the same object?
* 6-answer.txt : What do these 3 lines print
				>>> s1 = "Best School"
				>>> s2 = s1
				>>> print(s1 == s2)
* 7-answer.txt : What do these 3 lines print?
				>>> s1 = "Best"
				>>> s2 = s1
				>>> print(s1 is s2)
* 8-answer.txt : What do these 3 lines print?
				>>> s1 = "Best School"
				>>> s2 = "Best School"
				>>> print(s1 == s2)
* 9-answer.txt : What do these 3 lines print?
				>>> s1 = "Best School"
				>>> s2 = "Best School"
				>>> print(s1 is s2)
* 10-answer.txt : What do these 3 lines print?
				>>> l1 = [1, 2, 3]
				>>> l2 = [1, 2, 3] 
				>>> print(l1 == l2)
* 11-answer.txt : What do these 3 lines print?
				>>> l1 = [1, 2, 3]
				>>> l2 = [1, 2, 3] 
				>>> print(l1 is l2)
* 12-answer.txt : What do these 3 lines print?
				>>> l1 = [1, 2, 3]
				>>> l2 = l1
				>>> print(l1 == l2)
* 13-answer.txt : What do these 3 lines print?
				>>> l1 = [1, 2, 3]
				>>> l2 = l1
				>>> print(l1 is l2)
* 14-answer.txt : What does this script print?
				l1 = [1, 2, 3]
				l2 = l1
				l1.append(4)
				print(l2)
* 15-answer.txt : What does this script print?
				l1 = [1, 2, 3]
				l2 = l1
				l1 = l1 + [4]
				print(l2)
* 16-answer.txt : What does this script print?
				def increment(n):
					n += 1

				a = 1
				increment(a)
				print(a)
* 17-answer.txt : What does this script print?
				def increment(n):
					n.append(4)
			
			l = [1, 2, 3]
			increment(l)
			print(l)
* 18-answer.txt :  What does this script print?
				def assign_value(n, v):
					n = v

				l1 = [1, 2, 3]
				l2 = [4, 5, 6]
				assign_value(l1, l2)
				print(l1)
* 19-copy_list.py : a function def copy_list(l): that returns a copy of a list
* 20-answer.txt : a = (), Is a a tuple?
* 21-answer.txt : a = (1, 2), Is a a tuple?
* 22-answer.txt : a = (1), Is a a tuple?
* 23-answer.txt : a = (1, ), Is a a tuple?
* 24-answer.txt : What does this script print?
				a = (1)
				b = (1)
				a is b
* 25-answer.txt : What does this script print?
				a = (1, 2)
				b = (1, 2)
				a is b
* 26-answer.txt : What does this script print?
				a = ()
				b = ()
				a is b
* 27-answer.txt : Will the last line of this script print 139926795932424?
				>>> id(a)
				139926795932424
				>>> a
				[1, 2, 3, 4]
				>>> a = a + [5]
				>>> id(a)
* 28-answer.txt : Will the last line of this script print 139926795932424?
				>>> a
				[1, 2, 3]
				>>> id (a)
				139926795932424
				>>> a += [4]
				>>> id(a)
* 100-magic_string.py : a function magic_string() that returns a string "BestSchool" n times the number of the iteration
* 101-locked_class.py : a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name
* 103 : a = 1
		b = 1
		Assuming we are using a CPython implementation of Python3 with default options/configuration:
	* 103-line1.txt : How many int objects are created by the execution of the first line of the script?
	* 103-line2.txt : How many int objects are created by the execution of the second line of the script
* 104 : a = 1024 
		b = 1024 
		del a 
		del b 
		c = 1024

		Assuming we are using a CPython implementation of Python3 with default options/configuration: 

		* How many int objects are created by the execution of the first line of the script?

		* How many int objects are created by the execution of the second line of the script ?

		* After the execution of line 3, is the int object pointed by a deleted?

		* After the execution of line 4, is the int object pointed by b deleted?

		* How many int objects are created by the execution of the last line of the script ?
* 105 : print("I") 
		print("Love") 
		print("Python")

		Assuming we are using a CPython implementation of Python3 with default options/configuration:

		* Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)

		* Why?


