# PCAP-30-03

PCAP™ – Certified Associate in Python Programming certification focuses on the Object-Oriented Programming approach
to Python, and shows that the individual is familiar with the more advanced aspects of programming,
including the essentials of OOP, the essentials of modules and packages, the exception handling mechanism in OOP,
advanced operations on strings, list comprehensions, lambdas, generators, closures, and file processing.


## Module 1
### Modules, Packages and PIP;

- importing and using Python modules;
- using some of the most useful Python standard library modules;
- constructing and using Python packages;
- PIP (Python Installation Package) and how to use it to install and uninstall ready-to-use packages from PyPI.


# MODULE USING AND INVOCATION 

a module is a file containing Python definitions and statements (var & func).
instruction can be anywhere but must be placed before the first use of the module's entities 
(Instances, methods ...)

- ## Importing a module

```python
import sys  # import all entities from the sys module

sys.exit()  # using the module, need to specify the namespace
```

```python
from sys import exit  # import only the exit entity from the sys module

exit()  # using the exit method from the sys module, doesn't need the namespace

"""
This is the recommended method because you can see exactly which methods from the module are imported, making your 
code clear and easy to understand.
"""
```

```python
def exit():  # definition of an exit() function
    print('I want to exit')

exit()  # using the locally defined exit() function
```
```text
The sys prefix can distinguish our own function from the sys entity (exit), but in cases where we don't need to specify 
the namespace, your own code takes priority if something has exactly the same name as an entity; imported entities will be overwritten.
name space: is a space in which names exist
```
```python
from sys import * 
exit()

"""
You don't have to use the namespace with this syntax, but all entities from a module are imported, which can create 
many conflicts in your code.
"""
```
```python
from sys import exit as e
e()

# To manage a module with a long name, but it may lead to reduced readability.
```

- ## Additional Notes

```python
for name in dir(os):
    print(name) # Check the content of a random module
```

```python
if __name__ == '__main__':
    print('module file has been executed')
else:
    print('module has been imported')

"""
When working with modules in Python, the if __name__ == '__main__': block serves as a useful tool to differentiate 
between code that should be run when a script is executed directly versus code that should be run when a script is imported as a module.
This is useful for testing functions in the module.
"""
```

```python
#!/usr/bin/env python3  
"""
The shebang line (#!) specifies the interpreter that should be used to execute the script. It's particularly
useful in Unix-like operating systems.
"""

_my_var = "hello"     # Weak internal use indicator
__my_var = "hidden"   # Strong indicator for private use (name mangling)
__var__ = "special"   # Reserved for magic methods
```
##  Sys Module

The `sys` module provides access to some variables and functions that interact with the Python interpreter.

### Key Functions and Attributes

- **`sys.path.append(path)`**
  - Adds a specified directory to the Python path, allowing modules in that directory to be imported.
  - **Example Usage:**
    ```python
    import sys
    
    # Add upper directory to the path variable
    sys.path.append('..//module-test')

    # Add directory in the path variable (same directory as the main file)
    sys.path.append('module-test')

    # Import a module inside the folder
    import module_test
    ```

- **Absolute Path Example:**
  - `absolute_path = 'c\user...'`  
  - Refers to a specific location on the hard disk.

## Math Module

The `math` module provides mathematical functions.

### Key Functions

- **`ceil(x)`**
  - Returns the smallest integer greater than or equal to `x`.
  - **Example:** `math.ceil(2.9)` returns `3`.

- **`floor(x)`**
  - Returns the largest integer less than or equal to `x`.
  - **Example:** `math.floor(2.9)` returns `2`.

- **`trunc(x)`**
  - Removes the decimal part and returns the integer.
  - **Note:** Similar to `round()` but does not round the number.

- **`factorial(x)`**
  - Returns the factorial of `x`, which is the product of all positive integers less than or equal to `x`.
  - **Example:** `math.factorial(5)` returns `120`.

- **`sqrt(x)`**
  - Returns the square root of `x`.
  - **Example:** `math.sqrt(9)` returns `3.0`.
  - **Note:** The result is always a float.

- **`hypot(x, y)`**
  - Returns the hypotenuse of a right-angled triangle with sides `x` and `y`.
  - **Example:** `math.hypot(3, 4)` returns `5.0`.


## Random Module

The `random` module implements pseudo-random number generators for various distributions.

### Key Functions

- **`random.seed(a=None)`**
  - Initializes the random number generator. The seed determines the base of the random sequence. Different seeds will produce different sequences of random numbers.

- **`random.random()`**
  - Returns a random floating-point number in the interval `[0.0, 1.0)`.

- **`random.randint(a, b)`**
  - Returns a random integer `N` such that `a <= N <= b`.

- **`random.choice(sequence)`**
  - Returns a randomly selected element from a non-empty sequence.
  - **Note:** An element can be selected more than once if called multiple times.

- **`random.sample(population, k)`**
  - Returns a list of `k` unique elements chosen from the population sequence.
  - **Note:** Elements are not repeated in the result.

- **`random.randrange(start, stop[, step])`**
  - Returns a randomly selected element from the range `start` to `stop` with a step of `step`.
  - **Example:** `random.randrange(0, 10, 4)` can produce numbers `0`, `4`, or `8`.

## Platform Module

The `platform` module provides functions to access underlying platform information 
i.e., hardware, operating system, and interpreter version information.)

### Key Functions

- **`platform.system()`**
  - Returns the name of the operating system.
  - **Example:** On Windows, it returns `'Windows'`.

- **`platform.platform()`**
  - Returns a string describing the platform, including the operating system and version.
  - **Example:** `'Linux-4.15.0-142-generic-x86_64-with-Ubuntu-18.04-bionic'`.

- **`platform.platform(aliased=False, terse=False)`**
  - When `aliased` is `True`, it may use alternative names for some systems.
  - When `terse` is `True`, it returns a brief form of the platform string.

- **`platform.machine()`**
  - Returns the machine type, such as the processor architecture.
  - **Example:** `'x86_64'` for a 64-bit architecture.

- **`platform.processor()`**
  - Returns the processor name.
  - **Example:** `'Intel64 Family 6 Model 142 Stepping 10, GenuineIntel'`.

- **`platform.python_implementation()`**
  - Returns the Python implementation name.
  - **Example:** `'CPython'`.

- **`platform.python_version_tuple()`**
  - Returns the Python version as a tuple `(major, minor, micro)`.
  - **Example:** `('3', '8', '12')`.

- **`platform.version()`**
  - Returns the system's release version as a single string.
  - **Example:** `'#24~20.04.1-Ubuntu SMP Mon Sep 12 06:14:01 UTC 2022'`.


### Additional Notes

- **Comparison of Version Functions**:
  - `platform.python_version_tuple()` provides the Python version. for example: ('3', '8', '12') 
  - `platform.version()` provides the system's release version. For example #24~20.04.1-Ubuntu SMP Mon Sep 12 06:14:01 UTC 2022
  - Important for differentiation in exams like PCAP.

  
# Python Packages Cheat Sheet

## Overview of Python Packages

A package is a collection of Python modules organized within a directory. It is used to structure code into logical components.

### Key Concepts

- **Package Creation:**
  - A package is created by simply creating a folder and placing modules inside it.
  - The folder can contain an `__init__.py` file to initialize the package, but this file is optional in Python 3 and later.

- **Importing Modules from Packages:**
  - **With Namespace:**
    ```python
    import my_application.utilities.helpers.modulename
    ```
    - Requires using the namespace (full path) to access functions or variables.

  - **Without Namespace:**
    ```python
    from my_application.utilities.helpers.modulename import my_function
    ```
    - Directly imports specific functions or variables without needing the full path.

### Examples of Package Importing

#### Method 1: Adding to `sys.path`

```python
import sys

# Add package directory to the Python path
sys.path.append('my_project/utility_modules')

# Import modules
import math_helpers
from string_helpers import process_string

# Access module contents
print(math_helpers.calculate_area())  # Needs a namespace
print(process_string("Hello World"))  # No namespace needed
print('\\n')
```

#### Method 2: Importing with Full Package Path

```python
import my_project.utility_modules.math_helpers
from my_project.utility_modules.string_helpers import process_string

# Access module contents
print(my_project.utility_modules.math_helpers.calculate_area())
print(process_string("Hello World"))
print('\\n')
```

### Method 3: Importing the Entire Package

Note: This is generally discouraged as it imports the entire package and does not directly access specific modules.
```python
import my_project.utility_modules

# Access module contents (not recommended)
print(my_project.utility_modules.math_helpers.calculate_area())
```


# PyPI / Pip

pip is the package management tool for Python. It is used to install and manage Python libraries and modules
from the Python Package Index (PyPI) or other repositories.

## Basic Commands

- `pip help`  
  Displays general help for pip. For help on a specific operation, use `pip help <operation>`, e.g., `pip help install`.

- `pip list`  
  Shows a list of Python packages installed so far.

- `pip show <package_name>`  
  Provides detailed information about an installed package, including its dependencies.

- `pip search <anystring>`  
  Searches through PyPI to find a desired package.

- `python -m pip install --upgrade pip`
  The complete method to update pip

## Package Installation and Management

- `pip install <package_name>`  
  Installs a package from PyPI. For example, `pip install pygame`.

- `pip install --user <package_name>`  
  Installs the package in the user’s directory rather than the system-wide directory (admin). For example, `pip install --user pygame`.

- `pip install -U <package_name>`  
  Updates a locally installed package.

- `pip install <package_name>==<package_version>`  
  Installs a specific version of a package. For example, `pip install pygame==1.9.2`.

- `pip uninstall <package_name>`  
  Uninstalls a package. For example, `pip uninstall pygame`.


## Resources

This content is beyond the scope of the PCAP exam but may be very useful if you work with Python. There are many modules written for Python by both professional developers and enthusiasts. But how can you find out what modules are available? Where can you find their code? One of the best sources of Python modules is the Python Package Index, or PyPI, available at [https://pypi.org/](https://pypi.org/).
PyPI is a repository full of Python modules; you can browse and download them as needed. Have fun!
