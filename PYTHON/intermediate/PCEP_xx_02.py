# ======== PCEP-30-XX ========= < > #
"""
PCEP : Certified Entry-Level Python Programmer certification shows that you are familiar with universal computer
Programming concepts like data types, containers, functions, conditions, and loops, as well as the most important
aspects of the Python programming language syntax, semantics, and the runtime environment.
"""

# Module 1
# Introduction to Python and computer programming;
# Module 2
# ata types, variables, basic input-output operations, and basic operators;
# Module 3
# Boolean values, conditional execution, loops, lists and list processing, logical and bitwise operations;
# Module 4
# Functions, tuples, dictionaries, exceptions, and data processing.


# ======= MODULE 1 ======= #
"""
Python Essentials 1:
Module 1
Introduction to Python and computer programming

In this module, you will learn about:

- the fundamentals of computer programming
- the difference between compilation and interpretation. 
- what distinguishes the different versions of Python.
"""

"""
- compiled language and interpreted language : Compiled languages are converted directly into machine code that the 
  processor can execute. Interpreters go through a program line by line and execute each command.

- The syntax of a programming language describes which character strings constitute a valid program.
- The semantics of a programming language describes what syntactically valid programs mean.
- Syntax concerns the form of the language, semantics concerns the meaning.
- The lexicon is simply the set of all the words and expressions of the language, and these words or expressions are
  called lexical elements.
- ex: Colorless green ideas sleep furiously.
- Guido Van Rossum (Creator of Python) : the name of the Python programming language comes from an old BBC television 
  comedy sketch series called Monty Python's Flying Circus.
  
# Cpython, Cython, Jython, Pypy 


- CPython, the most common Python distribution (others included PyPy and Jython) is an interpreter for Python 2 or 
Python 3.

- Cython is a Python extension that allows you to compile Python code. Python gives you easy development and Cython
gives you speed when you need it most. It's a team, not competitors.

- Another version of Python is called Jython.
"J" is for "Java". Imagine a Python written in Java instead of C. This is useful, for example, if you develop large and 
complex systems written entirely in Java and want to add some Python flexibility to them. 

- PyPy is rather a tool for people developing Python than for the rest of the users.
Python within a Python. In other words, it represents a Python environment written in a Python-like language named 
RPython (Restricted Python). It is actually a subset of Python.
"""

# ======= MODULE 2 ======= #
"""
Python Essentials 1:
Module 2
Data types, variables, basic input-output operations, basic operators

In this module, you will learn:

how to write and run simple Python programs;
what Python literals, operators, and expressions are;
what variables are and what are the rules that govern them;
how to perform basic input and output operations.
"""

# Types de variables // Literals are notations for representing some fixed values in code.

a = "Hello"  # String : str
b = 5  # Integer int
c = 1.5  # Floating number : float
d = True  # Boolean : bool

# Print // It prints/outputs a specified message to the screen/console window
# Input() // take user datas and return String : str
# Type conversion // data_type(data) ==> str(2)

"""
1. In Python strings the backslash "\" => \n (the newline character) starts a new output line.
2. Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted
after the first, the third is outputted after the second, etc.
3. Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used 
to identify them. The "end" and "sep" parameters can be used for formatting the output of the print() function. 
The "sep" => separator between the outputted arguments, e.g., print("H", "E", "L", "L", "O", sep="-") // 
the "end" => print at the end of the print state
"""

# Operators

"""
An expression is a combination of values and Operators are special symbols which are able to operate on the values 
** | - + | * /(float) | // % | + - (  Subexpressions in parentheses are always calculated first ans The exponentiation 
operator
uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.)
# += | -= |
"""

print((2 ** 4), (2 * 4.), (2 * 4))  # 16 8.0 8
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)  # 10.0
print()
e = 3
f = 2
g = (e ** 2 + f ** 2) ** 2.
print(g)
print(type(g))

# PCEP TRAP
"""
x = 3
y = 5
x, y, z = y, x, x
print(x, y, z ) # value don't change during execution

z = 0
y = 10
x = y < z and z > y or y > z and z < y # true or false = true 
# x  =  True and False # = False
"""


# ======= MODULE 3 ======= #
"""

Python Essentials 1:
Module 3
Boolean Values, Conditional Execution, Loops, Lists and List Processing, Logical and Bitwise Operations

In this module, you will cover the following topics:
making decisions in Python (if, if-else, if-elif,else)
how to repeat code execution using loops (while, for)
how to perform logic and bitwise operations in Python;
lists in Python (constructing, indexing, and slicing; content manipulation)
how to sort a list using bubble-sort algorithms;
multidimensional lists and their applications.
"""

# Conditions
print()

x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("x is not > a 5")

"""
if x == 10:
    break & continue keywords # Error : break word must be used in loops but not in conditions
    can use it if the conditions are in a loop ( PCEP )
"""

# Loops
# break - example
print()

# while
# Example 1
while True:
    print("Stuck in an infinite loop.")
    break

# Example 2

counter = 5
while counter > 2:  # 2 is out
    print(counter)
    counter -= 1

# for
# break - example // only in a loop

print("The break instruction:")
for i in range(0, 6):  # 6 is not include
    if i == 3:  # 3  is not include
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

"""
for i in range(1, 3):
    for u in range(1, 11):
        print(i, '*', u, '=', i * u, '\n')
        
"""
"""
for i in range(1, 20, 2):
    print(i) # Start, Stop, Step
"""
"""
for i in range(3):
    for u in range(1, 11): # repeat this loop 3 times
        print(u)
"""
# PCEP TRAP
"""
i = 0
while i < 2:
    i += 1
    print ("*")
else:
    print ("f") #else execute

i = 0
while i < i+2:
    i += 1
    print ("*")
else:
    print ("f") # infinity loop
"""


# DATA COLLECTIONS
# List
# create and call a list
a = ["john", "toto", "mike", "michael", "jenny", "ben"]
print(len(a))  # return number of elements
# Call the list => print(a)

"""
a = [i for i in range(0, 11)]  # create quick list (list comprehension )
a= []
for i in range(1, 11):  # create quick list
    a.append(i)
"""

# add or delete an element in the list
a.append("ben")  # add an element in the list, by default at the end
a.insert(0, 3)  # Insert an element in the list with index
del a[1:4]  # 4  is not include
del a[0]  # 4  delete element 0

# Slicing a part of a list
print(a[3])  # Call an index of an element in the list
print(a[0:3])  # Call a part of a list, from 0 to 2

# replace - change position and sort in the list - Copy a list
a[1] = a[5]  # Replace a value the element at index 1 by the element at index 5
a[0], a[6] = a[6], a[0]  # change position of the elements in the list 0 -> 1 and 1 -> 0

a = [1, 2, 3]  # New list
a.reverse()  # sort a list from the biggest integer to the smallest - from z to a for string
a.sort(reverse=True)  # sort a list from the biggest integer to the smallest - from z to a for string
a.sort()  # sort a list from the smallest integer to the biggest - from a to z for string

# sorted(a)  and  reversed(a)
"""
    a.sort() is used when you want to sort the original list in place, 
    while sorted(a) is used when you want to create a new sorted list
    without modifying the original list.
    
    sort() or reverse() are list methods, so they apply directly to an existing list and return none 
    while sorted() and reverse() can be used with any iterable (not just a list) and return a new iterable 
"""
"""
for child in range(len(my_family)):
    print("Child", child, " is", my_family[child])
"""

# Copy list
b = a[:]  # copy a list
c = a[
    -4:1]  # Slicing  Copy (- take the element from the two the beginning of an iterable // be careful of out of range exception)
"""
print(5 in a)
print(5 not in b)
"""

# Nested List
cells = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]  # Nested List
# print(cells) or print(cells[0][2])  The list //  print(cells[0]) the first included list  // print(cells[1]) the second
# print(cells[1][2])
"""
    for i in cells:
        print('List : ', i)  # Access to an element in the list

for i in cells:
    for u in i:
        print(u)  # Access to an element in the list included in the list
"""

nn = [i for i in range(0, 6) for j in range(3)]  # create one list with element 3 time with loop
nnn = [[i for i in range(0, 6)] for j in range(3)]  # create a list 3 time
print(nnn)

"""
short_l1 = [1, 2]
short_l2 = [3, 4]
print(short_l1 + short_l2)  # can use others operators
print()
"""

#  TRAP PCEP
"""
 # return error because of name 
mylist = [1, 2, 3, 4, 5]
def mylist(mylist):
    del mylist[3]
    mylist[0] = 10
print(mylist(mylist)) # error 
"""

"""
myList = [1, 2]
for v in range(2):
    myList.insert(-1, myList[v])
print(myList) # insert 1 two times who,is in range and is one of element of the list

l = [1, 2, 3, 6]
l.insert(-1, 5)
print(l)  # always insert before the last number 
"""


#  Further String Features
"""
Str can be used like list in python by using methods : .upper(), .lower(), .isnumeric()
you can print an element of a list by index like with list
"""
my_str = "i'm a string"
print(my_str.upper())
print(my_str[0])

# ======= MODULE 4 ======= #
"""
Python Essentials 1:
Module 4
Functions, Tuples, Dictionaries, Exceptions, and Data Processing

In this module, you will cover the following topics:

code structuring and the concept of function;
function invocation and returning a result from a function;
name scopes and variable shadowing;
tuples and their purpose, constructing and using tuples;
dictionaries and their purpose, constructing and using dictionaries;
exceptions – the try statement and the except clause, Python built-in exceptions, code testing and debugging.
"""

# DATA COLLECTIONS
# Tuple
"""
Lists are mutable (make modification : add, delete,...) and tuples are immutable ( can't make modification, but
you can assign the variable a new value, print elements by index ...) this is the difference between them
"""
my_tuple1 = ()
my_tuple2 = (1, 'boy')
# my_tuple = (1, 'boy',) my_tuple = 1, my_tuple = 1 my_tuple = (1,)
foo = (1, 2, 3)
print(foo.index(2))  # The index() method searches for an element in the tuple and returns the index by enter value
tup = (1, 'ridi', True)
print(4 in tup)

"""
- about tuples operations : loops, len(), conditions, use operators (+,-,*)
- you can use tuple in list and list in tuple and use loop and condition
- list still mutable in a tuple
- use list for same type of element and tuple for may type of element 
"""

# TRAP PCEP
"""
tup = (1, 2, 4, 8)
tup = tup[1:-1]
print(tup)
tup = tup[0]
print(tup)  # update the tuple and not make copy
"""
"""
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
print(tup) # print the new tuple 
tup = tup[-1]
print(tup) # print the value of the tuple in a variable 
"""

# DATA COLLECTIONS
# Dictionary

salutation = {
    'fr': 'salut',
    'en': 'Hi'
}

print(salutation)  # print the dic
print(salutation['fr'])  # return Value

"""
 - Dictionary stock key and value 
 - the key must be unique and can't be a list but value can (key is immutable)
 - you must use key to have is value but can't use value to have is key
 - you can use len(), del with dic 
"""
print()

grades = {}
grades['anne'] = 'A'
grades['jon'] = 'B'
grades.update({'anne': 'C'})
print(grades)
print()

#  Trap PCEP
"""
for k in grades:  # return key
    print(k)
for key in grades.keys():
    print(key)
for v in grades.values():
    print(v)
for i, u in grades.items():
    print('this the key:', i, 'and value: ', u)
"""
"""
dic = { 'one': 'two', 'three': 'one', 'two': 'three'}
v = 'one' # can take the value of a key and stock it in var
print(v)

for i in range(len(dic)):
    print(i)
    v = dic[v]
print(v)

dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']
for k in range(len(dct)):
    v = dct[v]
print(v) try me
"""


#  Function in Python
def strange_list_fun(n):
    strange_list = []
    for num in range(0, n):
        strange_list.insert(0, num)
    return strange_list
    # print('hello world')


print(strange_list_fun(5))

"""
    return keyword is used to getout of a function or for return a value from a function
    the instruction after return is ignored 
    it's not necessary to add a return if the function doesn't return a value. None is returned
    don't work outside a function
    can return many value (tuple)  
    
    def func_mult():
        val1 = 10
        val2 = "Hello"
        val3 = [1, 2, 3]
    return val1, val2, val3
    
    result1, result2, result3 = func_mult()
    print(result1)  # print 10
    
    result = func_mult()
    print(result)  # print (10, "Hello", [1, 2, 3])
"""

# Recursion

"""
def a(n, limit):
    if n > limit:
        return
    print("n:", n)
    a(n * n, limit)
a(2, 100000)
"""

# TRAP PCEP
"""
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 0

print(fun(fun(2)) + 1) #renvoie 1 
"""
"""
def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)

print(f(2))  # recursion 
"""
