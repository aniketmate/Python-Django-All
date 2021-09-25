
"""abs() returns absolute value of given number"""
print ("---------------------------------------built in function abs()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print(abs(-40))
print(abs(-23.33))
print(abs(3+6j))
# ---------------------------------------OUTPUT---------------------------------------
# 40
# 23.33
# 6.708203932499369

"""all() returns True if all elements in the iterable are True else it returns False"""

print ("---------------------------------------built in function all()---------------------------------------") #all must be true
print("---------------------------------------OUTPUT---------------------------------------")
l=[1,2,3,4,5]
print(all(l))
l1=[1,2,0,False]
print(all(l1))
l2=[]
print(all(l2))
---------------------------------------OUTPUT---------------------------------------
True
False
True

"""any() returns True if any elements in the iterable are True else it returns False"""

print ("---------------------------------------built in function any()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
l=[1,2,3,4,5]
print(all(l))
l1=[1,2,0,False]
print(all(l1))
l2=[]
print(all(l2))
---------------------------------------OUTPUT---------------------------------------
True
False
True



""" The ascii() method returns a string containing a printable representation of an object. It escapes the non-ASCII characters in the string using \x, \u or \U escapes."""

print ("---------------------------------------built in function ascii()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

randomList = ['Python', 'Pythön', 5]
print(ascii(randomList))
---------------------------------------OUTPUT---------------------------------------
'Python is interesting'
'Pyth\xf6n is interesting'
Pythön is interesting
['Python', 'Pyth\xf6n', 5]

""" The bin() method converts and returns the binary equivalent string of a given integer."""

print ("---------------------------------------built in function bin()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
number = 6
print('The binary equivalent of 6 is:', bin(number))

a=3
b=1
c=2
print(bin(a+b+c))
---------------------------------------OUTPUT---------------------------------------
The binary equivalent of 6 is: 0b110
0b110

"""The bool() function converts a value to Boolean (True or False) using the standard truth testing procedure."""
print ("---------------------------------------built in function bool()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
test = []
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = True
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))
---------------------------------------OUTPUT---------------------------------------
[] is False
[0] is True
None is False
True is True
Easy string is True

"""The bytearray() method returns a bytearray object which is an array of the given bytes."""
print ("---------------------------------------built in function bytearray()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

l = [1,2,3]
print(bytearray(l))
var = 10
print(bytearray(var))

string = "Python is interesting."
print(bytearray(string.encode()))

---------------------------------------OUTPUT---------------------------------------
bytearray(b'\x01\x02\x03')
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
bytearray(b'Python is interesting.')

"""The callable() method returns True if the object passed appears callable. If not, it returns False."""
print ("---------------------------------------built in function callable()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))

class A:
  def __call__(self):
    print('Hello World')

print(callable(A))

---------------------------------------OUTPUT---------------------------------------
False
True
True



"""The chr() method returns a character (a string) from an integer (represents unicode code point of the character)."""
print ("---------------------------------------built in function chr()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print(chr(97))
print(chr(65))
print(chr(-1))

---------------------------------------OUTPUT---------------------------------------
a
A
Traceback (most recent call last):
  File "e:/aniket mate/Assignment_05.py", line 152, in <module>
    print(chr(-1))
ValueError: chr() arg not in range(0x110000)

"""The compile() method returns a Python code object from the source (normal string, a byte string, or an AST object)."""
print ("---------------------------------------built in function chr()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')

exec(codeObejct)

---------------------------------------OUTPUT---------------------------------------
sum = 11

"""The classmethod() method returns a class method for the given function."""
print ("---------------------------------------built in function classmethod()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

class Person:
    age = 25
    @classmethod
    def printAge(cls):
        print('The age is:', cls.age)    

Person.printAge()

---------------------------------------OUTPUT---------------------------------------
The age is: 25


"""The complex() method returns a complex number when real and imaginary parts are provided, or it converts a string to a complex number."""
print ("---------------------------------------built in function complex()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
z = complex(2, -3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)

---------------------------------------OUTPUT---------------------------------------
(2-3j)
(1+0j)
0j
(5-9j)

"""The delattr() deletes an attribute from the object (if the object allows it)."""
print ("---------------------------------------built in function delattr()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
class Coordinate:
  x = 10
  y = -5
  z = 0

point1 = Coordinate() 

print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)

delattr(Coordinate, 'z')

print('--After deleting z attribute--')
print('x = ',point1.x)
print('y = ',point1.y)

print('z = ',point1.z)

---------------------------------------OUTPUT---------------------------------------
x =  10
y =  -5
z =  0
--After deleting z attribute--
x =  10
y =  -5
Traceback (most recent call last):
  File "e:/aniket mate/Assignment_05.py", line 231, in <module>
    print('z = ',point1.z)
AttributeError: 'Coordinate' object has no attribute 'z'

"""The dict() constructor creates a dictionary in Python."""
print ("---------------------------------------built in function dict()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
numbers = dict(x=5, y=0)
print('numbers =', numbers)

numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)


numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)


numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)

---------------------------------------OUTPUT---------------------------------------
numbers = {'x': 5, 'y': 0}
numbers1 = {'x': 4, 'y': 5}
numbers2 = {'x': 4, 'y': 5}
numbers3 = {'x': 4, 'y': 5, 'z': 8}


"""The dir() method tries to return a list of valid attributes of the object."""
print ("---------------------------------------built in function dir()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
class Person:
  def __dir__(self):
    return ['age', 'name', 'salary']
    
teacher = Person()
print(dir(teacher))

number = [1, 2, 3]
print(dir(number))

print('\nReturn Value from empty dir()')
print(dir())

---------------------------------------OUTPUT---------------------------------------
['age', 'name', 'salary']
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Return Value from empty dir()
['Person', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'number', 'teacher']

"""The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder."""
print ("---------------------------------------built in function divmod()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print('divmod(8, 3) = ', divmod(8, 3))
print('divmod(5, 5) = ', divmod(5, 5))
print('divmod(8.0, 3) = ', divmod(8.0, 3))
print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))

---------------------------------------OUTPUT---------------------------------------
divmod(8, 3) =  (2, 2)
divmod(5, 5) =  (1, 0)
divmod(8.0, 3) =  (2.0, 2.0)
divmod(7.5, 2.5) =  (3.0, 0.0)
divmod(2.6, 0.5) =  (5.0, 0.10000000000000009)


"""The enumerate() method adds counter to an iterable and returns it (the enumerate object)."""
print ("---------------------------------------built in function enumerate()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

---------------------------------------OUTPUT---------------------------------------
<class 'enumerate'>
[(0, 'bread'), (1, 'milk'), (2, 'butter')]
[(10, 'bread'), (11, 'milk'), (12, 'butter')]


"""The staticmethod() built-in function returns a static method for a given function."""
print ("---------------------------------------built in function staticmethod()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

class Mathematics:
    @staticmethod
    def addNumbers(x, y):
        return x + y

print('The sum is:', Mathematics.addNumbers(5, 10))
---------------------------------------OUTPUT---------------------------------------
The sum is: 15

"""The filter() method constructs an iterator from elements of an iterable for which a function returns true."""
print ("---------------------------------------built in function filter()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
random_list = [1, 'a', 0, False, True, '0']

filtered_list = filter(None, random_list)

print('The filtered elements are:')
for element in filtered_list:
    print(element)

    ---------------------------------------OUTPUT---------------------------------------
The filtered elements are:
1
a
True
0

"""The eval() method parses the expression passed to this method and runs python expression (code) within the program."""
print ("---------------------------------------built in function eval()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

x = 1
print(eval('x + 1'))
x = 3
print(eval('x * 5'))
x = 5
print(eval('x / 3'))
x = 4
print(eval('x - 1'))

---------------------------------------OUTPUT---------------------------------------
2
15
1.6666666666666667
3

"""The float() method returns a floating point number from a number or a string."""
print ("---------------------------------------built in function float()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")


print(float(10))


print(float(11.22))


print(float("-13.33"))


print(float("     -24.45\n"))


print(float("abc"))

---------------------------------------OUTPUT---------------------------------------
10.0
11.22
-13.33
-24.45
Traceback (most recent call last):
  File "e:/aniket mate/Assignment_05.py", line 399, in <module>
    print(float("abc"))
ValueError: could not convert string to float: 'abc'

"""The built-in format() method returns a formatted representation of the given value controlled by the format specifier."""
print ("---------------------------------------built in function format()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print(format(123.4567898, "f"))
print(format(1234, "*>+7,d"))
print(format(123.4567, "^-09.3f"))

---------------------------------------OUTPUT---------------------------------------
123.456790
*+1,234
0123.4570

"""The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable."""
print ("---------------------------------------built in function frozenset()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)

person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)

---------------------------------------OUTPUT---------------------------------------
The frozen set is: frozenset({'o', 'e', 'a', 'u', 'i'})
The frozen set is: frozenset({'age', 'sex', 'name'})

"""The getattr() method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function."""
print ("---------------------------------------built in function getattr()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)

---------------------------------------OUTPUT---------------------------------------
The age is: 23
The age is: 23

"""The globals() method returns the dictionary of the current global symbol table."""
print ("---------------------------------------built in function globals()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
globals()

--------------------------------------OUTPUT---------------------------------------

C:\Users\Mate>C:/Users/Mate/AppData/Local/Programs/Python/Python38-32/python.exe
Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 13:22:56) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>>

"""The exec() method executes the dynamically created program, which is either a string or a code object."""
print ("---------------------------------------built in function exec()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

---------------------------------------OUTPUT---------------------------------------
Sum = 15

"""The hasattr() method returns true if an object has the given named attribute and false if it does not."""
print ("---------------------------------------built in function hasattr()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
class Person:
    age = 23
    name = 'Adam'

person = Person()

print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))

---------------------------------------OUTPUT---------------------------------------
Person has age?: True
Person has salary?: False


"""The help() method calls the built-in Python help system."""
print ("---------------------------------------built in function help()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
help(list)
---------------------------------------OUTPUT---------------------------------------
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
-- More  --

"""The hex() function converts an integer number to the corresponding hexadecimal string."""
print ("---------------------------------------built in function hex()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
number = 435
print(number, 'in hex =', hex(number))

number = 0
print(number, 'in hex =', hex(number))

number = -34
print(number, 'in hex =', hex(number))

"""The hash() method returns the hash value of an object if it has one."""
print ("---------------------------------------built in function hash()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print('Hash for 181.23 is:',hash(181.23))
print('Hash for Python is:', hash('Python'))
---------------------------------------OUTPUT---------------------------------------
Hash for 181.23 is: 579773580
Hash for Python is: 697706477

"""The input() method reads a line from input, converts into a string and returns it."""
print ("---------------------------------------built in function input()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
inputString = input('Enter a string:')

print('The inputted string is:', inputString)
---------------------------------------OUTPUT---------------------------------------
Enter a string:aniket
The inputted string is: aniket

"""The id() function returns identity (unique integer) of an object."""
print ("---------------------------------------built in function id()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
a=5
print(id(a))
---------------------------------------OUTPUT---------------------------------------
1353955312

"""The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument)."""
print ("---------------------------------------built in function instance()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
class Foo:
  a = 5
  
fooInstance = Foo()

print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))

---------------------------------------OUTPUT---------------------------------------
True
False
True

"""The int() method returns an integer object from any number or string."""
print ("---------------------------------------built in function int()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

print("int(123) is:", int(123))
print("int(123.23) is:", int(123.23))
print("int('123') is:", int('123'))

---------------------------------------OUTPUT---------------------------------------
int(123) is: 123
int(123.23) is: 123
int('123') is: 123

"""The issubclass() function checks if the class argument (first argument) is a subclass of classinfo class (second argument)."""
print ("---------------------------------------built in function issubclass()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
class Polygon:
  def __init__(polygonType):
    print('Polygon is a ', polygonType)

class Triangle(Polygon):
  def __init__(self):

    Polygon.__init__('triangle')
    
print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))

---------------------------------------OUTPUT---------------------------------------
True
False
True
True

"""The Python iter() function returns an iterator for the given object."""
print ("---------------------------------------built in function iter()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)
print(next(vowels_iter))    
print(next(vowels_iter))    
print(next(vowels_iter))    
print(next(vowels_iter))    
print(next(vowels_iter))    

---------------------------------------OUTPUT---------------------------------------
a
e
i
o
u

"""The list() constructor returns a list in Python."""
print ("---------------------------------------built in function list()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print(list())
vowel_string = 'aeiou'
print(list(vowel_string))
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list))
---------------------------------------OUTPUT---------------------------------------
[]
['a', 'e', 'i', 'o', 'u']
['a', 'e', 'i', 'o', 'u']
['a', 'e', 'i', 'o', 'u']

"""The locals() method updates and returns a dictionary of the current local symbol table."""
print ("---------------------------------------built in function locals()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
locals()
---------------------------------------OUTPUT---------------------------------------

>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>>

"""The len() function returns the number of items (length) in an object."""
print ("---------------------------------------built in function len()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))

---------------------------------------OUTPUT---------------------------------------
[] length is 0
[1, 2, 3] length is 3
(1, 2, 3) length is 3
Length of range(1, 10) is 9

"""The Python max() function returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters."""
print ("---------------------------------------built in function max()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
number = [3, 2, 8, 5, 10, 6]
largest_number = max(number);

print("The largest number is:", largest_number)

languages = ["Python", "C Programming", "Java", "JavaScript"]
largest_string = max(languages);

print("The largest string is:", largest_string)

---------------------------------------OUTPUT---------------------------------------
The largest number is: 10
The largest string is: Python

"""The Python min() function returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters."""
print ("---------------------------------------built in function min()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
number = [3, 2, 8, 5, 10, 6]
smallest_number = min(number);

print("The largest number is:", smallest_number)

languages = ["Python", "C Programming", "Java", "JavaScript"]
largest_string = min(languages);

print("The largest string is:", largest_string)

---------------------------------------OUTPUT---------------------------------------
The largest number is: 2
The largest string is: C Programming

"""The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results."""
print ("---------------------------------------built in function map()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
def calculateSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)
numbersSquare = set(result)
print(numbersSquare)

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)


numbersSquare = set(result)
print(numbersSquare)

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))

--------------------------------------OUTPUT---------------------------------------
<map object at 0x01412EC8>
{16, 1, 4, 9}
<map object at 0x01412F88>
{16, 1, 4, 9}
[9, 11, 13]

"""The next() function returns the next item from the iterator."""
print ("---------------------------------------built in function next()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
random = [5, 9, 'cat']
random_iterator = iter(random)
print(random_iterator)
print(next(random_iterator))
print(next(random_iterator))
print(next(random_iterator))
---------------------------------------OUTPUT---------------------------------------
<list_iterator object at 0x01352E98>
5
9
cat

"""The memoryview() function returns a memory view object of the given argument."""
print ("---------------------------------------built in function memoryview()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
random_byte_array = bytearray('ABC', 'utf-8')
mv = memoryview(random_byte_array)
print(mv[0])
print(bytes(mv[0:2]))
print(list(mv[0:3]))
---------------------------------------OUTPUT---------------------------------------
65
b'AB'
[65, 66, 67]

"""The object() function returns a featureless object which is a base for all classes."""
print ("---------------------------------------built in function object()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
test = object()
print(type(test))
---------------------------------------OUTPUT---------------------------------------
<class 'object'>


"""The oct() function takes an integer number and returns its octal representation."""
print ("---------------------------------------built in function oct()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print('oct(10) is:', oct(10))
print('oct(0b101) is:', oct(0b101))
print('oct(0XA) is:', oct(0XA))

---------------------------------------OUTPUT---------------------------------------
oct(10) is: 0o12
oct(0b101) is: 0o5
oct(0XA) is: 0o12


"""The pow() function returns the power of a number."""
print ("---------------------------------------built in function pow()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print(pow(2, 2))    

print(pow(-2, 2))      

print(pow(2, -2))    

print(pow(-2, -2))    

---------------------------------------OUTPUT---------------------------------------
4
4
0.25
0.25

"""The print() function prints the given object to the standard output device (screen) or to the text stream file."""
print ("---------------------------------------built in function print()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print("Python is fun.")

a = 5
print("a =", a)

b = a
print('a =', a, '= b')

---------------------------------------OUTPUT---------------------------------------
Python is fun.
a = 5
a = 5 = b

"""The property() construct returns the property attribute."""
print ("---------------------------------------built in function property()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')

p = Person('Adam')
print(p.name)
p.name = 'John'
del p.name

---------------------------------------OUTPUT---------------------------------------
Getting name
Adam
Setting name to John
Deleting name


"""The range() type returns an immutable sequence of numbers between the given start integer to the stop integer."""
print ("---------------------------------------built in function range()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print(list(range(0)))

print(list(range(10)))

print(list(range(1, 10)))

---------------------------------------OUTPUT---------------------------------------
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]


"""The repr() function returns a printable representation of the given object."""
print ("---------------------------------------built in function repr()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
var = 'foo'

print(repr(var))
class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name )

print(repr(Person()))

---------------------------------------OUTPUT---------------------------------------
'foo'
'Hello Adam'

"""The reversed() function returns the reversed iterator of the given sequence."""
print ("---------------------------------------built in function reversed()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
seq_string = 'Python'
print(list(reversed(seq_string)))

seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))

seq_range = range(5, 9)
print(list(reversed(seq_range)))


seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))

---------------------------------------OUTPUT---------------------------------------
['n', 'o', 'h', 't', 'y', 'P']
['n', 'o', 'h', 't', 'y', 'P']
[8, 7, 6, 5]
[5, 3, 4, 2, 1]

"""The round() function returns a floating-point number rounded to the specified number of decimals."""
print ("---------------------------------------built in function round()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print(round(10))

print(round(10.7))

print(round(5.5))

---------------------------------------OUTPUT---------------------------------------
10
11
6

"""The set() builtin creates a set in Python."""
print ("---------------------------------------built in function set()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
print(set())

print(set('Python'))
print(set(('a', 'e', 'i', 'o', 'u')))

print(set(['a', 'e', 'i', 'o', 'u']))

print(set(range(5)))

---------------------------------------OUTPUT---------------------------------------
set()
{'h', 'o', 'n', 'y', 'P', 't'}
{'u', 'i', 'o', 'e', 'a'}
{'u', 'i', 'o', 'e', 'a'}
{0, 1, 2, 3, 4}



"""The setattr() function sets the value of the attribute of an object."""
print ("---------------------------------------built in function setattr()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
class Person:
    name = 'Adam'
    
p = Person()
print('Before modification:', p.name)

# setting name to 'John'
setattr(p, 'name', 'John')

print('After modification:', p.name)
---------------------------------------OUTPUT---------------------------------------
Before modification: Adam
After modification: John


"""The slice() function returns a slice object that can use used to slice strings, lists, tuple etc."""
print ("---------------------------------------built in function slice()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
py_string = 'Python'

print(py_string[0:3]) 

print(py_string[1:5:2]) 

---------------------------------------OUTPUT---------------------------------------
Pyt
yh


"""The sorted() function returns a sorted list from the items in an iterable."""
print ("---------------------------------------built in function sorted()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")

py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))

py_string = 'Python'
print(sorted(py_string))

py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))

---------------------------------------OUTPUT---------------------------------------
['a', 'e', 'i', 'o', 'u']
['P', 'h', 'n', 'o', 't', 'y']
['a', 'e', 'i', 'o', 'u']


"""The str() function returns the string version of the given object."""
print ("---------------------------------------built in function str()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
result = str(10)
print(result)
---------------------------------------OUTPUT---------------------------------------
10

"""The sum() function adds the items of an iterable and returns the sum."""
print ("---------------------------------------built in function sum()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum)

# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum)
---------------------------------------OUTPUT---------------------------------------
4.5
14.5

"""The tuple() builtin can be used to create tuples in Python."""
print ("---------------------------------------built in function tuple()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
t1 = tuple()
print('t1 =', t1)

# creating a tuple from a list
t2 = tuple([1, 4, 6])
print('t2 =', t2)

# creating a tuple from a string
t1 = tuple('Python')
print('t1 =',t1)

# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1 =',t1)

---------------------------------------OUTPUT---------------------------------------
t1 = ()
t2 = (1, 4, 6)
t1 = ('P', 'y', 't', 'h', 'o', 'n')
t1 = (1, 2)

"""The type() function either returns the type of the object or returns a new type object based on the arguments passed."""
print ("---------------------------------------built in function type()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
numbers_list = [1, 2]
print(type(numbers_list))

numbers_dict = {1: 'one', 2: 'two'}
print(type(numbers_dict))

class Foo:
    a = 0

foo = Foo()
print(type(foo))

---------------------------------------OUTPUT---------------------------------------
<class 'list'>
<class 'dict'>
<class '__main__.Foo'>


"""The vars() function returns the __dict__ attribute of the given object."""
print ("---------------------------------------built in function vars()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
class Foo:
  def __init__(self, a = 5, b = 10):
    self.a = a
    self.b = b
  
object = Foo()
print(vars(object))
---------------------------------------OUTPUT---------------------------------------
{'a': 5, 'b': 10}


"""The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it."""
print ("---------------------------------------built in function zip()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')


result = zip(numbersList, numbers_tuple)

result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

result_set = set(result)
print(result_set)

---------------------------------------OUTPUT---------------------------------------
{(3, 'THREE'), (2, 'TWO'), (1, 'ONE')}
{(1, 'one', 'ONE'), (2, 'two', 'TWO')}


"""The super() builtin returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class."""
print ("---------------------------------------built in function super()---------------------------------------")
print("---------------------------------------OUTPUT---------------------------------------")
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    
d1 = Dog()
---------------------------------------OUTPUT---------------------------------------
Dog has four legs.
Dog is a warm-blooded animal.
