
# isinstance and is Operator

"""
class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class Landvehicle(Vehicle):
    def __init__(self, speed, w_count):
        super().__init__(speed)
        self.w_count = w_count


class Car(Landvehicle):
    pass


vehicle = Vehicle(60)
landvehicle = Landvehicle(60, 4)
car = Car(50, 4)

print(isinstance(landvehicle, Vehicle))
print(isinstance(landvehicle, Landvehicle))
print(isinstance(landvehicle, Car))


isinstance returns true if an object was created with a given clause, but it also returns true if the object was created
from a subclass of the class that we provide.


my_car_one = Car(50, 5)
my_car_two = my_car_one
print(my_car_one is my_car_two)


variables don't store objects directly.
object variables contain the address of an object in the memory, not the object itself
(store references to objects in the memory)

My new vehicle gets that reference and both variables point to the same object.
we can check it with 'is' Operator
object using one of the variables, that change will be visible in the second variable as well.

#  is and ==

a = 5
b = 5
print(a is b)  # return true

a = 5
b = 3
b += 2
print(a is b)  # return true

# The same however is not true about strings.

first_str = 'hello'
second_str = 'hello'
print(first_str is second_str)  # return True


if we define two string variables with the same content, The second variable actually points to the very same string as 
the first one.

first_str = 'hello'
second_str = 'hell'
second_str += 'o'
print(first_str is second_str)  # return False
print(first_str == second_str)  # return True


That's because whenever we try to modify an existing string, python instead creates a new one, even though both STR and 
second still contain identical strings. Now they are actually two separate objects in the memory.
the equality operator returns true because both variables contain the values 
"""

# MULTIPLE INHERITANCE

"""
it's a situation when a class has more than one super class.


class Vehicle:
    def __init__(self):
        pass

    def go(self):
        print('Iam going')

    def introduce(self):
        print('im a vehicle')


class Flyable:
    def __init__(self):
        pass

    def fly(self):
        print('Iam  flying')

    def introduce(self):
        print('Im a flyable')


class Airplane(Vehicle, Flyable):
    pass


airplane = Airplane()
airplane.introduce()  # Print : iam a vehicle

The answer is something called MRO or method resolution order. MRO explains how a given programming language tries to 
find the method that is currently needed.

- python looking in the object 
- not found, looking in the subclass from left to right
- not found, raise an error 

the general rule is to avoid using multiple inheritance at all. n fact, many programming languages do not allow multiple
inheritance at all.
Single inheritance is always simpler and easier to maintain with multiple inheritance.You have many options to mess up
and to make a mistake.
Treat multiple inheritance as the last resort when you don't have any other option left.


#  The __bases__ property

returns a tuple with all the base classes that the given class inherits from (directly). 

"""










"""
Python Essentials 2:
Module 4
Miscellaneous

In this module, you will learn about:

Generators, iterators and closures;
Working with file-system, directory tree and files;
Selected Python Standard Library modules (os, datetime, time, and calendar.)
"""

"""


# List comprehension

mylist = [i for i in range(1, 101)]
print(mylist)  # list comprehension feature

mylist2 = [i for i in range(1, 100) if i % 3 != 0]
print(mylist2)

mylist3 = [0 if i % 2 == 0 else 1 for i in range(0, 100)]
print(mylist3)

mylist4 = [i for i in range(0, 6) for j in range(0, 10)]
print(mylist4)

# LAMDA FUNCTION

# LAMBDA FUNCTION


func_l = lambda a: a + 1


def apply_func(elements, func):
    for element in elements:
        print(func(element))


apply_func([1, 2, 3, 4, 5], func_l)

"""

# LAMBDA WITH MAP & FILTER


"""

# MAP function
lambda_func = lambda i: i * 2

mylist = [1,2,3,4,5]
print(map(lambda_func, mylist))  # MAP function return an iterator.
# We can use list or next function to print elements
print(next(map(lambda_func, mylist)))  # print element one by one (note goood methode)
print(list(map(lambda_func, mylist)))  # print the entire list

print(list(map((lambda a: a*2), [1, 2, 3, 4, 5])))  # print all of this with one line of code


#  FIlter
to filter the elements of the sequence. Also return zn iterator 

print(list(filter(lambda a: a % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))  # FIlter the iterator znd return some specific value


emails_adresses = [
    'rdplus@gmail.com',
    'ridi-gmail.com',
]

print(list(filter(lambda y: '@' in y,  emails_adresses)))  # adresse email filter 

"""


# CLosures

"CLosure is a function defined inside a function that remembers the value of the other function"


# CLOSURE

def greet(text):
    def say_hello():  # that's nasted function
        print(text)
    return say_hello  # return the closure; That's because we don't want to invoke the function, just return


def make_multiply_closure(y):
    def multiply(x):
        return x * y

    return multiply


multiply_5 = make_multiply_closure(5)
multiply_12 = make_multiply_closure(12)

print(multiply_5(10))
print(multiply_5(20))

print(multiply_12())

"""
That nested function prints create becomes a closure 
the moment it references a variable from the out function 
If we didn't reference any variables from the grid function, print grid would simply be called a nested function
But when we access that text variable inside print grid, it immediately becomes a closure.
"""
"""
If you have a class that only has one custom method, you can typically replace it with a closure and the code will be shorter to read.
"""


# Generator (PCEP AND PCAP)

def gen():
    for num in range(1, 6):
        yield num


generator = gen()  # the function must be
#  print(next(generator))
#  print(next(generator))
"""
for x in generator:
    print(x)
"""
"""
gen_list = list(gen())
print(gen_list)
"""








#  ERROR MANAGEMENT
# Generator (PCEP AND PCAP)

"""
This is propagating exception 
"""

user_info = []



"""
def get_user_day_1(lst):
    day = int(input('please enter day 1 __ '))
    lst.append(day)
    return lst


def get_user_day_2(mylist):
    day = int(input('please enter day 1 __ '))
    mylist.append(day)
    return my_list


try:
    a = get_user_day_1(user_info)
    b = get_user_day_2(user_info)
    print(user_info)
except ValueError:
    print('value error caught')

#  Assertion

assertions are used for debugging or testing code or documenting code, tell to others developers what you expect in your
code 
never use it for validate user input or handle exception 

def little_calcul(number):
    assert (number != 0)
    return 0 / number


print(little_calcul(5))

"""
























# File Processing
# Print each character

"""
    try:
    stream = open('fileprocessingtest')  # Open the file and store it in a vairable
    counter = 0
    character = stream.read(1)
    while character != '':
        counter += 1
        print(character, end='-')
        character = stream.read(1)  # It's better to print element one by one
    stream.close()  # Always close the stream (protect your memory)
    print('the total of character is :', counter)
    print()

except Exception as e:
    print('An error has occurred:', e)

# Print per line

# Print each character
try:
    stream = open('fileprocessingtest')  # Open the file and store it in a vairable
    counter_l = 0
    line = stream.readline()
    while line != '':
        counter_l += 1
        print(line, end='_')
        line = stream.readline()  # It's better to print element one by one
    stream.close()  # Always close the stream (protect your memory)
    print('the total of line is :', counter_l)

except Exception as e:
    print('An error has occurred:', e)

try:
    stream = open('fileprocessingtest')
    lines = stream.readlines()  # return a list of string per line
    print('Content of lines var : ', lines)
    print('NUmber of element: ', len(lines))
    for line in lines:
        print(line, end='')
    stream.close()
except Exception as e:
    print('An error has occurred :', e)


try:
    stream = open('fileprocessingtest')
    lines = stream.readlines(2)
    while len(lines) != 0:
        for line in lines:
            print(line, sep='')
        lines = stream.readlines(2)
    stream.close()
except Exception as e:
    print('An error has occurred: ', e)


try:
    stream = open('fileprocessingtest')  # YOu don't need to close the stream with this method
    for line in stream:
        print(line, sep='')
except Exception as e:
    print('an error has occured : ', e)

"""
"""
  #  FIle writing

try:
    stream = open('todo-list-data.txt', 'w')  # You to use this syntax. after executing the code, the file will be rewrite
    line = stream.write('THis is what i write')
    stream.close()
except Exception as e:
    print('An error has occurred: ', e)
    
"""


# Binary file

"""
Recall that a bite is eight bits 
and with eight bits you are able to represent an integer number in the range from 0 to 255.

"""

data = bytearray(100)  # This line will create an array with 100 bytes and initially they will all equal zero.data
data[0] = 100  # Remember that the maximal integer you can store in a byte is to 255
data[1] = 120
try:
    stream = open('testb.bin', 'wb')  # Write in a binary file syntax
    stream.write(data)
    stream.close()
except Exception as e:
    print('An error has occurred', e)


try:
    bf = open('testb.bin', 'rb')  # Syntax for read binary file
    byte_array = bf.read()
    bf.close()
except Exception as e:
    print('An error has occured:', e)

print(byte_array)  # not pretty

print()

for byte in byte_array:
    print(hex(byte), end='')  # Read as hexadecimal

print()

for byte in byte_array:
    print(int(byte), end=' ')  # read as integer

try:
    bf = open('testb.bin', 'rb')  # Syntax for read binary file
    byte_array = bf.read(10)  # can read a limited number of byte 
    bf.close()
except Exception as e:
    print('An error has occured:', e)

print()

for byte in byte_array:
    print(int(byte), end=' ')  # read as integer

# Predefined Stream

"""
When you start any program in Python, 
there are actually three predefined streams that don't need any properties and files. used with sys module 
"""

# -
