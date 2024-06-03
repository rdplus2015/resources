# ======== PCAP-30-03 ========= < > #

"""
PCAP™ – Certified Associate in Python Programming certification focuses on the Object-Oriented Programming approach
to Python, and shows that the individual is familiar with the more advanced aspects of programming,
including the essentials of OOP, the essentials of modules and packages, the exception handling mechanism in OOP,
advanced operations on strings, list comprehensions, lambdas, generators, closures, and file processing.
"""

# Module 1
# Modules, Packages and PIP;

# Module 2
# Strings, string and list methods, and exceptions;

# Module 3
# Object-Oriented Programming

# Module 4
# Miscellaneous (generators, iterators, closures, file streams, processing text and binary files,
# the os, time, datetime, and calendar module)


# ======= MODULE 1 ======= #
"""

Modules, Packages and PIP

In this module, you will learn about:

- importing and using Python modules;
- using some of the most useful Python standard library modules;
- constructing and using Python packages;
- PIP (Python Installation Package) and how to use it to install and uninstall ready-to-use packages from PyPI.

"""

#  MODULE USING AND INVOCATION #

"""
    a module is a file containing Python definitions and statements (var & func).
    instruction can be anywhere but must be placed before the first use of the module's entities 
    (Instances, methods ...)
"""

"""
import sys

from name in dir(module_name): 
    print(name) 
# Check the content of a random module 
"""

"""
import sys  # Module invocation : syntax 1 ==> import all entities from sys module 
def exit():
    print('i wanna exit')

exit()
sys.exit() # module using 
"""

"""
# from sys import exit  # Module invocation : syntax 2 ==> import only exit entity from sys module 
def exit():
    print('i wanna exit')

exit()
exit() # function from sys module
"""

"""
- The sys prefix can distinguish our own function and the sys entity (exit), is having his own namespace
- We can specify the exact entities from the module that we are interested Here, 
  we don't need to specify the namespace, Your own code has the priority if somthing has the very same name with 
  an entity, imported entities will be overwritten
"""

"""
from sys import * // you don't have to put the namespace with this syntax, but all entities from a random module 
are imported and can make a lot of conflicts in our code 
"""

"""
# You can use alias for handle module with long name 
- import sys as s // handle module with long name
- from sys import exit as ex
- can causes lower readability  "
"""

"""
if __name__ == '__main__':
    print('module executed in the main file')
    # _my_super var_ = 'hi' # by convention doubles underscore tell to the module user to don't modify the var (warning)
    # !usr/bin/env python3  // tell  some environment to use python -- for universal audience
    # use  three quote to explain what your module do 
else :
    print('module executed in the module file')
"""

# SYS MODULE

"""
import sys
sys.path.append('..//module-test') # add upper directory in the path variable
sys.path.append('module-test') # add directory in the path variable (same directory with main file) and import the 
module inside the folder after.
import module-test1  //  importation of the module inside the folder 
absolute_path = 'c\\user...' # path from the hard disk 
"""

# Math module

"""
# ceil() : return nearst integer // print(math.ceil(2.9))
# floor() :  return the nearest integer never greater than the number //
# trunc() : remove the decimal part et return the integer // same than round()
# factorial() : it's the multiplication of all positive integer  less than or equal to the given number //
# sqrt() : return the square root of a number //  return float
# hypot() :  return the hypotenuse // two arguments 
"""

# random Module

"""
# random.seed() // The choice of seed determines the "base" of the random sequence, and a different seed will lead to a 
different sequence of random numbers.
# random.random()  and # random.randit() 
In summary, random.randint(a, b) generates random integers in a specified interval, 
while random.random() generates random floating point numbers in the interval [0.0, 1.0).

# random.choice(sequence) // choosing from a sequence and can take one element two times
# random.sample() // take a sequence and number of element that must be taken without duplicate
# print(random.randrange(0, 10, 4))  produces an integer number x, which is taken from the range start ≤ x < stop with 
step step. Note: the start argument defaults to 0 and the step argument defaults to 1
It can randomly decide to return elements with indexes 0 and 1, and you will get ['Martin', 'John']. However, 
it can also randomly pick indexes 0 and 2, in which case you will get ['Martin', 'Martin'].  
"""

# platform Module


""" 
# platform.platform() and # platform.system() 
In summary, platform.system() simply returns the name of the operating system, 
while platform.platform() returns a text string describing the full platform in more detail, including additional 
information such as system version operating.

# platform.platform(aliased = False, Terse = False) // return alternative test if it fund or standar text.  
return brief form (terse)
# platform.machine() This function returns the hardware machine type, usually as a text string representing 
the processor architecture (for example, "x86_64" for a 64-bit architecture or "armv7l" for an ARM architecture).
# platform.processor() This function returns the processor name as a text string.

# platform.py_implementation() // the implementation of your python version
# platform.py_version_tuple() // the version of your python

"""

"""
    In the previous video, we've discussed platform.python_version_tuple(), which returns your Python version 
    as a 3-element tuple, for example: ('3', '8', '12') // There's also another function that looks similar: 
    platform.version(). This function, in turn, returns your system's release version as a single string, 
    for example: #24~20.04.1-Ubuntu SMP Mon Sep 12 06:14:01 UTC 2022
    Keep in mind not to confuse these two functions for the PCAP exam!
"""

# PYTHON PACKAGES

"""
- a package is a folder that content similar modules. for create it we just to create a folder and name it 
- __init__.py : file to initialize a package (optional since py3)
- import folder1.folder_b.folder3.modulename  // put namespace or alias
- from folder1.folder_b.folder3.modulename import my_fun // don't need to put namespace 
"""

"""
import sys

# method 1 
sys.path.append('pkg/modules5_6')  # add to the path variable
import module5
from module6 import b

print(module5.a)  # Need a name space
print(b)  # don't need the name space
print('\n')

# method 2
import pkg.modules5_6.module5
from pkg.modules5_6.module6 import b

print(pkg.modules5_6.module5.a)
print(b)
print('\n')
"""

"""
# methode 3  //  very bad way, don't import the modules inside the package 
import pkg.modules5_6
print(pkg.modules5_6.module5.a)
"""

# == PYPI / PIP  == #

"""
pip help // pip help operation (pip help install) 
pip list // If you want to know what Python packages have been installed so far
pip show package_name // command that can tell you more about any of the installed packages  (dependencies)

The power of pip comes from the fact that it’s actually a gateway to the Python software universe. Thanks to that, 
you can browse and install any of the hundreds of ready-to-use packages gathered in the PyPI repositories. 

pip search anystring // search through PyPI in order to find a desired package. 

 --user : install to user account and not in the system like admin  // pip install pygame  :  pip install --user pygame
 pip show pygame  // pip list pygame 

 pip install -U package_name // update a locally installed package
 pip install package_name==package_version / pip install pygame==1.9.2 //  install a user-selected version of a package
 pip uninstall package_name // pip uninstall pygame

"""

"""
    This content is outside the scope of the PCAP examination, but it may be very useful if you work with Python. I’ve
    mentioned that there are lots of modules written for Python by both professional Python developers and Python 
    enthusiasts. But how can you find out what modules are available? Where can you find their code? One of the best 
    sources of Python modules is the Python Package Index, or PyPI.It is available at https://pypi.org/.

It is a repository full of Python modules, you can browse them and download them as you need. Have fun!
"""

# ======= MODULE 2 ======= #

"""
Python Essentials 2:
Module 2
Strings, String and List Methods, Exceptions

In this module, you will learn about:

Characters, strings and coding standards;
Strings vs. lists – similarities and differences;
Lists methods;
String methods;
Python's way of handling runtime errors;
Controlling the flow of errors using try and except;
Hierarchy of exceptions.
"""

#  Part 1 INTERNAL STR REPRESENTATION (ENCODING SYSTEM)
"""
user => Str and computer stock it like unique number (Character encoding)
Character encoding :
    a process used in computing to represent text characters as binary numbers.
    Character encoding is essential to ensure that textual characters are correctly represented and interpreted when 
    stored, transmitted, and displayed by computers. Choosing the right encoding is crucial to ensuring the integrity 
    and readability of text data.

When characters don't display correctly, it often indicates that the file or text is being interpreted using the wrong 
character encoding or code page. In the past, different code pages were used to represent characters in 
different languages, leading to compatibility issues when transferring or displaying text between systems that use 
different encodings.

Unicode was developed to address this issue by providing a universal character encoding standard capable of representing
virtually all characters from all writing systems. Unicode supports millions of characters and assigns each character a 
unique code point, eliminating the need for different code pages for different languages.

By using Unicode, developers can ensure that their software and systems can handle text in multiple languages without 
encountering encoding-related issues. Additionally, Unicode allows for the representation of 
various scripts, symbols, and characters from different languages and writing systems, making it an essential standard 
for internationalization and multilingual support in software development.

ASCII (American Standard Code for Information Interchange) and Unicode are both character encoding standards, but they 
serve different purposes and have different scopes:
    ASCII is limited to representing characters from the English alphabet and some basic symbols commonly used 
    in English text.

    Unicode is a much newer and more comprehensive character encoding standard that was developed to address the 
    limitations of ASCII. It provides a unified system for representing characters from all writing systems used around 
    the world, including characters from languages such as Chinese, Arabic, Hindi, Japanese, and many others.

Implement unicode is specific computer by using UTF-8 : compatible with ASCII
UTF-8 (Unicode Transformation Format-8) is one of the variable-length encoding schemes used to represent Unicode while 
ensuring compatibility with existing ASCII encoding. This means that ASCII characters can be represented in 
UTF-8 identically, while UTF-8 can also represent Unicode characters outside the ASCII range using a variable number of 
bytes. In summary, UTF-8 extends the encoding capabilities of ASCII to include the full set of Unicode characters.
characters. 
"""

#  BASIC STRING OPERATIONS

name = 'ridi'
print('length', len(name), name[1], name[2:3], sep='-')  # different way to print str in python

# get the Unicode code of a character / get the character corresponding to a given Unicode code
print(ord('a'), chr(97), sep='-')
print(min('abc'), max('abc'), sep='-')  # lowest code point (unicode) # Highest code point (unicode)

# string are immutable / can't use del() can just be replaced
# a line is counted like a character in python, same than space
str_C = '''line 1
line 2'''
print(str_C, len(str_C), end='-')

# // * + operator overload  // concatenation and multiplication
a = '1'
b = '2'
print(a + b * 2, (a + b) * 2, sep='-')  # respect priority of operation in the first case

# Searching inside string (find, rfind, index => string methods, can't be used with int)
print(a.index('l'))  # return the index of the first given letter (occurrence) in the string
print(a.find('l'))  # return the index but will not raise index error ( will return -1)
print(a.rfind('l'))  # return the index  last occurrence of the letter l in the str
print(a.find('hi', 10))  # search  from x / searches for the first occurrence of the substring "hi"
print(a.find('l', 10, 15))  # search from x to y

# isalnum() isalpha() isdigit() isupper(), islower(), isspace() => character testing methods, return True or False
s = "Hello123"
print(s.isalnum())  # True, because all characters are alphanumeric
print(s.isalpha())  # False, because there are numbers

#  List methods
# Join and split strings
a = '123'
b = '-abc'
c = ''.join([a, b])
print(c, type(c), c.split(), sep='-')

# Sorted() create a  new list as a copy
# Sort() Modify the original list

# string comparison
"""
string are egal in python where they are exactly same, when they are different,
python compare the first different ASCII code
"""

# PART 2: EXCEPTION AND ASSERTION

#try:
#  the peace of code where the exception can occur

#except ValueError:
# You can catch a particular exception with keywords - ValueError, or ZeroDvisionError

#except:
# cath all others error that can occur
# Exception Hierarchy and propagating exception (image)


"""
    In python exception are propagated through functions, with one try - except block you can handle many exceptions
    when many function are called each others.
"""

"""
SyntaxError is not a subclass of the Exception class, although you can catch a manually raised SyntaxError, you cannot
catch a SyntaxError that is thrown due to a syntax error in the code itself.
"""

"""
1. BaseException 
    use internally by python and servers more as a template for others specific exception types
    1A. Exception       1B. SystemExit      1C.KeyboardInterrupt(...)
      1B.SystemExit (when we call a methode sys.exit() for close or terminate the program)
      1C.KeyboardInterrupt (Is raised when user press a key combination that causes an interrupt yo yhe executing script
    
1A. Exception : 
    is like BaseException, use as template (only for internal python Exception), but Exception can be used for our own
    exception and many builds python Exception 
        2A.ArithmeticError        2B.LookupError         2C.TypeError        2D.ValueError(...)
            2A.ArithmeticError (based class for a variety of math, arithmetic error. eg: ZeroDivisionError(...)
            
    2A.ArithmeticError
            2A1. ZeroDivisionError
    2B.LookupError
           2B1. IndexError      2B2. KeyError
"""

# ASSERTION
"""
    assertions are certain assumptions in our program that we think should always be true.
    These are conditions that we assume should always be true for this specific function to work correctly.
    In general, assertions are used for debugging and testing your code.
    You can add assertions as sanity checks at the beginning of a function to make sure that it receives
    This way you can communicate to other developers what you expect in your functions.   
"""
"""
    def calcul_inverse(number):
    assert (number != 0), 'The number can not be 0'
    return 1/number
"""

# you can use else and finally in try - except block

#else block
"""
    if you use else block, The block will be executed only if the except block doesn't 
    get executed In other words, the else block is run when no exception is raised in the try block and that's pretty
    (if there is no error. In case of error, else block will not be executed)
    this feature is not very used
"""

#finally
"""
    The general rule is that the final block is executed always, no matter if an exception is raised or not
    no matter if a raised exception is handled or not.
    So note that in both situations the final block is executed before the function finishes and returns
    this feature is used generally when we work with external resources such as database or text file
    eg: we want to take some information in you DB, no matter if the code work or no, we have to close the DB (finally)
"""

# The raise keyword
"""
    Python allows you to raise exceptions on your own : 
    - When you write tests to check your programs, you can raise exceptions to verify how your piece of code will behave
    if during the execution of your program, python suddenly raise a real exception
    
    - The second use case is when you want to make another part of the program responsible for handling the exception.
    can be good for large application
"""

"""

def return_bigger(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError
    if b > a:
        return b
    else:
        return a
"""

#Exception as Object
#Create Own Exception


# ======= MODULE 3 ======= #

"""
Python Essentials 2:
Module 3
Object-Oriented Programming

In this module, you will learn about:

Basic concepts of object-oriented programming (OOP)
The differences between the procedural and object approaches (motivations and profits)
Classes, objects, properties, and methods;
Designing reusable classes and creating objects;
Inheritance and polymorphism;
Exceptions as objects.
"""

# introduction

"""
Procedural Programming divides the program into small programs and refers to them as functions. 
Object Oriented Programming divides the program into small parts and refers to them as objects. 
Available data is capable of moving freely within the system from one function to another.

class : template for create object of the same type can contain :
    - Attributes (variable)
    - Methods (functions)
    - we instantiate object from the class / object are instances of class 
"""


#  CLASSES AND OBJECTS

class Student:
    def __init__(self, s_name, s_age, s_grade):  # constructor
        self.name = s_name  # retrieve value pass in the argument and pass it to the constructor
        self.age = s_age
        self.grade = s_grade

    def introduce(self):
        print('Hello i\'m a student, my name is', self.name, 'my grade is', self.grade, 'and i\'m', self.age)


new_student = Student('ridi', 21, 5)  # create object
print(new_student.introduce())  # call method
print(new_student.name)  # call  attribute

"""
    -   Constructor is a special method, call automatically when an object is created 
        for initialise attributes (proprieties of the object, define in a class) __init__()
    -   Self, make reference to the object itself, when you call methods, you call it from the object itself (self)
    -   self passed in a method allow you to access at class attributes 
"""


#  ENCAPSULATION ET ABSTRACTION


class Car:
    def __init__(self, model, color, initial_speed=0):
        self.model = model
        self.color = color
        if initial_speed < 0:
            self.__speed = 0  # Private attribute
        else:
            self.__speed = initial_speed

    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        print('The current speed is', self.__speed)


ridi_car = Car('tucson', 'silver', -5)
ridi_car.speed_up()
ridi_car.speed_up()
ridi_car.show_speed()

'''
    ENCAPSULATION : The object should keep their state private and only expose a set of only public functions 
    utside of the class.

    We put the Speed of the instance as a private attribute, user can't access and modify this  out of the class
    but exposed two public methods to manipulate the property in a way we previously defined.
'''

'''
    ABSTRACTION : Abstraction says that objects should keep the details of how they work to themselves and only expose
    some high level operations to the outside world.

    You don't need to know that the details of how your phone works. it's hidden from you.
    You only get access to some high level operations, like making a phone call or sending a text message.
    the details are abstracted from you.
'''


#  INSTANCE VARIABLE


class Dog:
    def __init__(self, named, age=0):
        self.name = named
        self.__age = age  # private attribute. it's a warning by convention but can be accessed

    def introduce(self):
        print('Im a dog, my name is', self.name, 'my age is', self.__age)


dog1 = Dog('pet', 2)
dog1.introduce()

dog2 = Dog('borg', 5)
dog2.introduce()

dog1.color = 'red'  # Instance variable closely related to a specific object
# del dog1.name    # Delete an attribute from the constructor
print(dog2.__dict__)  # check know which instance variables are available in a given object in a given place in the code
print(dog1.__dict__)  # __dict shows only instance variable and not class variable
# __dict__  works with class
# print(dog1._Dog__age)  # Access to a private attribute that are not really private
# name mangling not work if we use the __ outside the class


# CLASS VARIABLE

"""
a class variable is property that exist in just one copy share across all objects. it's store in the class itself
a Class variable exist even if you don't create any object of that class
"""


class Cat:
    counter = 0

    def __init__(self, namedd, age=0):
        self.name = namedd
        self.__age = age  # private attribute. it's a warning by convention but can be accessed
        Cat.counter += 1


cat1 = Cat('matou', 2)
cat2 = Cat('toutou', 2)

print(cat1.counter)  # 3 access to the class variable
print(cat1.counter)  # 3 access to the class variable
print(Cat.counter)  # 3 access to the class variable
# Give 3 ; that's because there is always exactly one copy of a class variable that is shared across all objects
# Can be private, deleted or mangling

# print(hasattr(Cat, 'name'))
if hasattr(Cat, 'name'):
    print('yes')  # Check if a class has an attribute
else:
    print('no')

# __dict__ store only instance variable ; you need to check in the class itself to see what class variable is available
# print(Cat.__name__) Only return the class name (can't be used with object)
# type(Cat).__name__ this combination do the same thing
# Dog.__module__ return the name of the module who contain the class

"""
Instance variable will overwrite class variable with the same name outside the class. And local variable 
can't be accessible outside the class. all of these can be printed in the class without any problems 
"""

# METHODS

"""
    - Function inside the class 
    - can be private (mangling) or public 
    - we can use the __dict__ with class name (not object name) property to see all methods of a given class 
"""

"""
class Teacher:
    def __init__(self, name):
        self.name = name

    def __str__(self):  # The __str__ method should return a single string representation of the object. 
        return 'Object : ' + self.name


teacher1 = Teacher('ridi')
print(teacher1)  # __main__.Teacher object at 0x7f862e357d90> default implementation of __str__ of a class or object

it print the internal object identifier used by Python, and it may be different for each object on each machine
the result of the print statement may not be very helpful if we want to debug our code. so we have to change 
the implementation

__str__ was create to give the string representation of a given object. when you print the object, that methode is
automatically called.
"""


# INHERITANCE


class Vehicle:  # Main class and subclass of itself
    def __init__(self, speed):
        self.speed = speed

    hello_message = 'hello, be careful, this is your car'  # define class variable
    print(hello_message)


class Landvehicle(Vehicle):  # subclass of Vehicle
    def __init__(self, speed, color):  # we have to have speed in argument because of the constructor import :
        # inheritance of instance variables from the constructor
        # Vehicle.__init__(self, speed)  # import of Vehicle class constructor to inherit is properties
        # tou can,t import superclass constructor if there is just self argument
        # args order is defined by subclass order. not super class
        super().__init__(speed)
        self.color = color

    def speed_up(self):  # methode for increase the speed of the car
        self.speed += 15


class Car(Landvehicle):  # subclass of Vehicle and Landvehicle
    def super_speed(self):
        print('super speed activated')
        super().speed_up()
        super().speed_up()  # invoked method from the parent class
        # don't need constructor


# When you define a constructor in a subclass you have ti define one for all superclass and all arguments
# super().i__init__(all arguments)


my_car = Car(5, 'red')  # create a new object
print(my_car.__dict__)
my_car.super_speed()  # Activation of super speed
my_car.speed_up()  # we can invoke the method directly  here
print(my_car.__dict__)

mercedes = Car(5, 'red')  # inheritance priority of class are progressive, from the direct class to the indirect
print(issubclass(Car, Landvehicle))  # check if x is subclass of y


#  POLYMORPHISM AND METHODS OVERRIDING


class Animal:
    def __init__(self):
        self.species = 'general'

    def produce_sound(self):
        print('General  animal sound')

    def present(self):
        print('i can do the following sound ')
        self.produce_sound()
        print('species = ' + self.species)


class Dog(Animal):
    def __init__(self):
        self.species = 'wolf dog '

    def produce_sound(self):
        print('Wolf Wolf sound')


my_pet_1 = Animal()
my_pet_2 = Dog()

print(my_pet_1.present())
print()
print(my_pet_2.present())

"""
 when you try to access a property or a method in an object, Python will first try to find that entity inside the object
 itself. If it fails, it then tries to find it in all the classes involved in the object inheritance line from
 bottom to top with the most general class at the very end method, overriding helps achieve one of the four
 core concepts of object oriented programming : Polymorphism 

 In the most general sense, polymorphism means the ability of classes to take different forms. Usually when we talk 
 about polymorphism, we talk about method overriding.

 Even though both objects are animals, one of them is more specific and changes the behavior of the superclass, 
 and that's an example of polymorphism.

 The dog class inherits the present method from the animal superclass, but when it's time to call the
 produce sound method, the dog object actually uses its own version of the method.
 That's because we use the produce sound invocation with the self reference, which always points to the current object.
 As a result, Python always tries to find the matching method within the object itself, and the end result is that even 
 though both objects use the present method, they actually behave differentially because behind the scenes 
 they were created using different classes.
"""

