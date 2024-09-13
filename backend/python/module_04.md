
# Python Essentials 1: Module 4
**Functions, Tuples, Dictionaries, Exceptions, and Data Processing**

## Data collections 
## Tuple

Tuples are immutable, meaning you cannot modify them after creation, unlike lists, which are mutable. However, you can reassign a tuple to a new value.
```python
my_tuple1 = ()  # empty tuple
my_tuple2 = (1, 'boy')  # tuple with different data types
foo = (1, 2, 3)
print(foo.index(2))  # returns the index of the value 2
tup = (1, 'ridi', True)
print(4 in tup)  # checks if 4 is in the tuple, returns False
```

### Tuple Operations:

- You can use loops, `len()`, and conditions on tuples.
- Tuples can be concatenated using `+` or repeated using `*`.
- You can nest tuples inside lists and vice versa.
- list still mutable in a tuple
- use list for same type of element and tuple for may type of element 

**Common Tuple Mistakes (PCEP Trap):**

```python
tup = (1, 2, 4, 8)
tup = tup[1:-1]  # slicing the tuple
print(tup)  # prints (2, 4)

tup = tup[0]
print(tup)  # prints 2, assigning a single value to tup
```


## Dictionary
Dictionaries store key-value pairs. The keys must be unique and immutable, while the values can be any data type, including lists.

```python

salutation = {
    'fr': 'salut',
    'en': 'Hi'
}

print(salutation)  # print the dictionary
print(salutation['fr'])  # access the value using the key
```
Dictionaries allow various operations such as len(), del, and more.


```python

grades = {}
grades['anne'] = 'A'
grades['jon'] = 'B'
grades.update({'anne': 'C'})  # updates the value for 'anne'
print(grades)
```

### Looping Through a Dictionary:

```python

for k in grades:  # loop through keys
    print(k)
for key in grades.keys():  # another way to loop through keys
    print(key)
for v in grades.values():  # loop through values
    print(v)
for i, u in grades.items():  # loop through key-value pairs
    print('Key:', i, 'Value:', u)
```

**Common Dictionary Mistakes (PCEP Trap):**

```python

dic = { 'one': 'two', 'three': 'one', 'two': 'three'}
v = 'one'
for i in range(len(dic)):
    v = dic[v]
print(v)  # prints the final value after iterating+
```
```python
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']
for k in range(len(dct)):
    v = dct[v]
print(v) 
```

## Functions in Python

Functions allow you to encapsulate logic and reuse code. Use return to output a value from a function. Any code after return inside a function is ignored.

```python
def strange_list_fun(n):
    strange_list = []
    for num in range(0, n):
        strange_list.insert(0, num)  # inserts numbers in reverse order
    return strange_list

print(strange_list_fun(5))  # returns [4, 3, 2, 1, 0]
```

### Function Return:

- You can return multiple values as a tuple.

```python

def func_mult():
    val1 = 10
    val2 = "Hello"
    val3 = [1, 2, 3]
    return val1, val2, val3

result1, result2, result3 = func_mult()  # unpacking the tuple
print(result1)  # prints 10
print(result2)  # prints Hello
print(result3)  # prints [1, 2, 3]
```

### Recursion

Recursion is when a function calls itself. It can be used to solve problems like factorial, Fibonacci series, etc.

```python

def a(n, limit):
    if n > limit:
        return
    print("n:", n)
    a(n * n, limit)  # recursive call
a(2, 100000)  # recursive function call with a limit
```

**Common Recursion Mistakes (PCEP Trap):**

```python

def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)

print(f(2))  # prints 3 (2 + 1 + 0)
```
```python
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 0

print(fun(fun(2)) + 1) #renvoie 1 
```