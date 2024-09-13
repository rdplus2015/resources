# Python Essentials 1: Module 3

### Boolean Values, Conditional Execution, Loops, Lists and List Processing, Logical and Bitwise Operations
---

### Key Concepts:
- Conditional statements (`if`, `if-else`, `if-elif-else`)
- Loop structures (`while`, `for`)
- Logic and bitwise operations
- Lists (construction, indexing, slicing)
- Sorting algorithms (e.g., bubble sort)
- Multidimensional lists

---

### 1. Conditional Execution

#### Example of Nested Conditions:
```python
x = 10

if x > 5:
    if x == 6:
        print("nested: x == 6")
    elif x == 10:
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("x is not > 5")
```
**Note**: Keywords like `break` and `continue` are used in loops, not in conditions. *(except if the condition is inside a loop)*

 
### 2. Loops

-  **Example of a `while` Loop:**
```python
while True:
    print("Stuck in an infinite loop.")
    break  # Exits the loop
```

- **Example of a Controlled `while` Loop:**
```python
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
```

- **`for` Loop with `break`:**
```python
for i in range(0, 6):  # Loop over 0 to 5
    if i == 3:
        break  # Stops loop at 3
    print("Inside the loop:", i)
print("Outside the loop.")
```

- `for` Loop with `continue`:
```python
for i in range(1, 6):
    if i == 3:
        continue  # Skips 3
    print("Inside the loop:", i)
print("Outside the loop.")
```

- **Nested Loops Example (Multiplication Table):**
```python
for i in range(1, 3):
    for u in range(1, 11):
        print(i, '*', u, '=', i * u, '\n')
```
```python
for i in range(3):
    for u in range(1, 11): # repeat this loop 3 times
        print(u)
```

- **Example with Step:**
```python
for i in range(1, 20, 2):  # Step by 2, Start, Stop, Step
    print(i)
```

- **`while` Loop with `else`:**
```python
i = 0
while i < 2:
    i += 1
    print("*")
else:
    print("Finished!")
```

**1. First While Loop - `else` Executes After Loop Completes**

```python
i = 0
while i < 2:
    i += 1
    print("*")
else:
    print("f")  # else executes after the loop
```

#### Explanation:

-   The `while` loop runs while `i < 2`.
-   `i` is incremented in each iteration.
-   The `else` block executes after the loop finishes.

    **Output**
    ```
    *
    *
    f
    ```
**2. Second While Loop - Infinite Loop**
```python
i = 0
while i < i + 2:
    i += 1
    print("*")
else:
    print("f")  # This will never execute because of an infinite loop
```

**Explanation:**

-   The condition `i < i + 2` will **always be true** because any number is always smaller than itself plus 2.
-   This creates an **infinite loop** where the condition never becomes false, and the loop never ends.
-   The `else` block is never reached, making this an **infinite loop trap**.

### 3. Lists
- **Creating and Accessing Lists:**

```python
a = ["john", "toto", "mike", "michael", "jenny", "ben"]
print(len(a))  # Output: 6 (number of elements)
print(a[3])  # Output: 'michael'
print(a[0:3])  # Output: ['john', 'toto', 'mike']

print(5 in a) # condition 
print(5 not in b) # condition 
```

- **List Comprehension Example:**

```python
a = [i for i in range(0, 11)]  # Creates a list [0, 1, 2, ..., 10]
```

- **Adding and Deleting Elements:**
```python

a.append("ben")  # Adds "ben" at the end
a.insert(0, 3)  # Inserts 3 at index 0
del a[1:4]  # Deletes elements from index 1 to 3 (4 is not included)
del a[0]  # Deletes the first element
```

- **List Slicing:**

```python
print(a[0:3])  # Slices a list from index 0 to 2
```

- **Copying and Sorting Lists:**

```python

b = a[:]  # Creates a copy of the list
a.reverse()  # Reverses the list
a.sort()  # Sorts the list in ascending order
a.sort(reverse=True)  # Sorts in descending order
```

- **Sorting vs. Creating a Sorted List:**

    - `a.sort()` sorts the original list in place.
    - `sorted(a)` creates a new sorted list without modifying the original.

- **Nested Lists:**

```python
cells = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
print(cells[1][2])  # Output: 'B3'
```

- **List Comprehension with Nested Loops:**

```python
a = [[i for i in range(0, 6)] for j in range(3)]  
print(a)  


b = [i for i in range(0, 6) for j in range(3)]  with element 3 time with loop
print(b)

for i in a:
        print('List : ', i) 

for i in b:
    for u in i:
        print(u)  
```

- **Replace and Change the Position of Elements in a List**

```python
a[1] = a[5]  # Replace the element at index 1 with the element at index 5
a[0], a[6] = a[6], a[0]  # Swap the elements at index 0 and index 6
```

- **Concatenating Lists**

```python
short_l1 = [1, 2]
short_l2 = [3, 4]
print(short_l1 + short_l2)  # Concatenate two lists using the + operator
print()
```

- **PCEP Trap (Potential Error)** 
In this example, there is a common mistake with naming conflicts. The list mylist is used both as a variable name and a function name, leading to an error.

```python

# This will return an error because of the name conflict
mylist = [1, 2, 3, 4, 5]

def mylist(mylist):
    del mylist[3]  # Delete element at index 3
    mylist[0] = 10  # Replace element at index 0 with 10

print(mylist(mylist))  # Error: 'mylist' is both a function and a variable name
```
- **Inserting Elements in a List**

```python

myList = [1, 2]
for v in range(2):
    myList.insert(-1, myList[v])  # Insert elements before the last element
print(myList)  # Output: [1, 1, 2, 1, 2]
```

In this example, 1 is inserted twice before the last element of the list.

```python

l = [1, 2, 3, 6]
l.insert(-1, 5)
print(l)  # Output: [1, 2, 3, 5, 6] - '5' is inserted before the last number (6)
```

The `insert()` function always inserts before the specified index. When using -1, it inserts before the last element.

- **Additional Notes**

    - Bitwise and Logical Operators: You can perform operations such as `&`, `|`, `^`, `~` for bitwise manipulations in Python.

    - Bubble Sort: Learn how to implement basic sorting algorithms like bubble sort for list processing.


### 4. String Manipulation
- **Strings as Lists:**

    Strings can be treated like lists. You can access characters using indexes and use methods like `.upper()`, `.lower()`, etc.

```python
my_str = "i'm a string"
print(my_str.upper())  # Output: "I'M A STRING"
print(my_str[0])  # Output: "i"
```