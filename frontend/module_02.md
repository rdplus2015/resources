# Python Essentials 1: Module 2


## Data Types, Variables, Basic I/O, and Operators

In this module, you will learn how to:
- Write and run simple Python programs.
- Work with literals, operators, and expressions.
- Manage variables and basic input/output operations.

## Key Concepts:
- **Data Types**:
```python
  a = "Hello"  # str
  b = 5        # int
  c = 1.5      # float
  d = True     # bool
```

- **Basic I/O:**
```python 
print("Hello, World!")  # Output to console
user_input = input("Enter your name: ")  # Input from user
```
- **Type Conversion:**
```python
num_str = "123"
num = int(num_str)  # Converts string to integer
```

## String Handling

- In Python, strings use the backslash (`\`) as an escape character.
- For example, `\n` represents a **newline character**, which starts a new line in the output.

```python
print("Hello\nWorld!")  # Output:
# Hello
# World!
```

## Arguments in Python 

-   **Positional Arguments**: The meaning of arguments is determined by their position.
    
    Example:

    ```python
    def greet(first, second):
    print(first, second)

    greet("Hello", "World")  # Output: Hello World
    ```

- **Keyword Arguments**: The meaning of arguments is determined by the keyword that is used.

  Example:

  ```python
  print("H", "E", "L", "L", "O", sep="-")  # Output: H-E-L-L-O
  ```
Common keyword arguments in Python include:

-   `sep`: Specifies the separator between arguments in `print()`.
-   `end`: Specifies what to print at the end of the output.

    Example:

    ```python
    print("Hello", end="!")  # Output: Hello!
    ```

## Python Operators

-   An **expression** is a combination of values and operators.
-   **Operators** are special symbols that operate on values.

**Common Operators:**

| Operator | Description                  | Example         |
|----------|------------------------------|-----------------|
| +        | Addition                     | 2 + 3 => 5      |
| -        | Subtraction                  | 5 - 2 => 3      |
| *        | Multiplication               | 2 * 4 => 8      |
| /        | Division (Floating point)     | 9 / 3 => 3.0    |
| //       | Integer (floor) division      | 9 // 2 => 4     |
| %        | Modulus (Remainder)           | 5 % 3 => 2      |
| **       | Exponentiation               | 2 ** 3 => 8     |
| +=       | Addition and assignment       | x += 5          |
| -=       | Subtraction and assignment    | x -= 2          |


**Operator Precedence:**

  -   Subexpressions in parentheses are calculated first.
  -   The exponentiation operator (`**`) has **right-sided binding**.

**Practical Examples:**
  ```python
  result = 2 ** 2 ** 3
  print(result)  # Output: 256
  ``` 
  ```python
  print((2 ** 4), (2 * 4.), (2 * 4))  # Output: 16, 8.0, 8
  print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)  # Output: 10.0

  e = 3
  f = 2
  g = (e ** 2 + f ** 2) ** 2.
  print(g)  # Output: 625.0
  print(type(g))  # Output: <class 'float'>
  ```

  **PCEP Trap Example**

  -   In the Python Certified Entry-Level Programmer (PCEP) exam, you may encounter tricky variable swaps and logical statements.

  ```python
  x = 3
  y = 5
  x, y, z = y, x, x
  print(x, y, z)  # Output: 5, 3, 3

  z = 0
  y = 10
  x = y < z and z > y or y > z and z < y  # True or False = True
  print(x)  # Output: True
  ```
  Explanation:

  -   `x = y < z and z > y or y > z and z < y`
      -   This statement is evaluated as:
          -   `True or False = True`
          -   Hence, `x = True`.